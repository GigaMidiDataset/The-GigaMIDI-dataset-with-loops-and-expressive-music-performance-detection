"""The GigaMIDI dataset."""  # noqa:N999

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING, Literal

import datasets

if TYPE_CHECKING:
    from collections.abc import Sequence

    from datasets.utils.file_utils import ArchiveIterable

_CITATION = ""
_DESCRIPTION = "A large-scale MIDI symbolic music dataset."
_HOMEPAGE = "https://github.com/Metacreation-Lab/GigaMIDI"
_LICENSE = "CC0, also see https://www.europarl.europa.eu/legal-notice/en/"
_SUBSETS = ["all-instruments-with-drums", "drums-only", "no-drums"]
_SPLITS = ["train", "validation", "test"]
_BASE_DATA_DIR = ""
_N_SHARDS_FILE = _BASE_DATA_DIR + "n_shards.json"
_MUSIC_PATH = (
    _BASE_DATA_DIR + "{subset}/{split}/GigaMIDI_{subset}_{split}_{shard_idx}.tar"
)
_METADATA_PATH = _BASE_DATA_DIR + "{subset}/metadata_{subset}_{split}.json"
_METADATA_FEATURES = {
    "sid_matches": datasets.Sequence(
        {"sid": datasets.Value("string"), "score": datasets.Value("float16")}
    ),
    "mbid_matches": datasets.Sequence(
        {
            "sid": datasets.Value("string"),
            "mbids": datasets.Sequence(datasets.Value("string")),
        }
    ),
    "artist_scraped": datasets.Value("string"),
    "title_scraped": datasets.Value("string"),
    "genres_scraped": datasets.Sequence(datasets.Value("string")),
    "genres_discogs": datasets.Sequence(
        {"genre": datasets.Value("string"), "count": datasets.Value("int16")}
    ),
    "genres_tagtraum": datasets.Sequence(
        {"genre": datasets.Value("string"), "count": datasets.Value("int16")}
    ),
    "genres_lastfm": datasets.Sequence(
        {"genre": datasets.Value("string"), "count": datasets.Value("int16")}
    ),
    "median_metric_depth": datasets.Sequence(datasets.Value("int16")),
    # "loops": datasets.Value("string"),
}
_VERSION = "1.0.0"


"""def cast_metadata_to_python(
    metadata: dict[str, Any],
    features: dict[str, datasets.Features] | None = None,
) -> dict:
    if features is None:
        features = _METADATA_FEATURES
    metadata_ = {}
    for feature_name, feature in features.items():
        data = metadata.get(feature_name, None)
        if (
            data
            and isinstance(feature, datasets.Sequence)
            and isinstance(feature.feature, (datasets.Sequence, dict))
        ):
            if isinstance(feature.feature, datasets.Sequence):
                metadata_[feature_name] = [
                    cast_metadata_to_python(
                        {feature_name: sample}, {feature_name: feature.feature}
                    )
                    for sample in data
                ]
            else:
                metadata_[feature_name] = {
                    cast_metadata_to_python(
                        {feature_name_: sample}, feature.feature
                    )
                    for sample in data
                    for feature_name_ in feature.feature
                }
        else:
            metadata_[feature_name] = data

    return metadata_"""


class GigaMIDIConfig(datasets.BuilderConfig):
    """BuilderConfig for GigaMIDI."""

    def __init__(
        self,
        name: str,
        subsets: Sequence[
            Literal[
                "all-instruments-with-drums",
                "all-instruments-no-drums",
                "drums-only",
            ]
        ]
        | None = None,
        **kwargs,
    ) -> None:
        """
        BuilderConfig for GigaMIDI.

        Args:
        ----
            name: `string` or `List[string]`:
                name of the dataset subset. Must be either "drums" for files containing
                only drum tracks, "music" for others or "all" for all.
            subsets: `Sequence[string]`: list of subsets to use. It is None by default
                and resort to the `name` argument to select one subset if not provided.
            **kwargs: keyword arguments forwarded to super.

        """
        if name == "all":
            self.subsets = _SUBSETS
        elif subsets is not None:
            self.subsets = subsets
            name = "_".join(subsets)
        else:
            self.subsets = [name]

        super().__init__(name=name, **kwargs)


class GigaMIDI(datasets.GeneratorBasedBuilder):
    """The GigaMIDI dataset."""

    VERSION = datasets.Version(_VERSION)
    BUILDER_CONFIGS = [  # noqa:RUF012
        GigaMIDIConfig(
            name=name,
            version=datasets.Version(_VERSION),
        )
        for name in ["all", *_SUBSETS]
    ]
    DEFAULT_WRITER_BATCH_SIZE = 256

    def _info(self) -> datasets.DatasetInfo:
        features = datasets.Features(
            {
                "md5": datasets.Value("string"),
                "music": {
                    "path": datasets.Value("string"),
                    "bytes": datasets.Value("binary"),
                },
                "is_drums": datasets.Value("bool"),
                **_METADATA_FEATURES,
            }
        )
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
            version=_VERSION,
        )

    def _split_generators(
        self, dl_manager: datasets.DownloadManager | datasets.StreamingDownloadManager
    ) -> list[datasets.SplitGenerator]:
        n_shards_path = Path(dl_manager.download_and_extract(_N_SHARDS_FILE))
        with n_shards_path.open() as f:
            n_shards = json.load(f)

        music_urls = defaultdict(dict)
        for split in _SPLITS:
            for subset in self.config.subsets:
                music_urls[split][subset] = [
                    _MUSIC_PATH.format(subset=subset, split=split, shard_idx=f"{i:04d}")
                    for i in range(n_shards[subset][split])
                ]

        meta_urls = defaultdict(dict)
        for split in _SPLITS:
            for subset in self.config.subsets:
                meta_urls[split][subset] = _METADATA_PATH.format(
                    subset=subset, split=split
                )

        # dl_manager.download_config.num_proc = len(urls)

        meta_paths = dl_manager.download_and_extract(meta_urls)
        music_paths = dl_manager.download(music_urls)

        local_extracted_music_paths = (
            dl_manager.extract(music_paths)
            if not dl_manager.is_streaming
            else {
                split: {
                    subset: [None] * len(music_paths[split][subset])
                    for subset in self.config.subsets
                }
                for split in _SPLITS
            }
        )

        return [
            datasets.SplitGenerator(
                name=split_name,
                gen_kwargs={
                    "music_shards": {
                        subset: [
                            dl_manager.iter_archive(shard) for shard in subset_shards
                        ]
                        for subset, subset_shards in music_paths[split_name].items()
                    },
                    "local_extracted_shards_paths": local_extracted_music_paths[
                        split_name
                    ],
                    "metadata_paths": meta_paths[split_name],
                },
            )
            for split_name in _SPLITS
        ]

    def _generate_examples(
        self,
        music_shards: dict[str, Sequence[ArchiveIterable]],
        local_extracted_shards_paths: dict[str, Sequence[dict]],
        metadata_paths: dict[str, Path],
    ) -> dict:
        if not (
            len(metadata_paths)
            == len(music_shards)
            == len(local_extracted_shards_paths)
        ):
            msg = "The number of subsets provided are not equals"
            raise ValueError(msg)

        for subset in self.config.subsets:
            if len(music_shards[subset]) != len(local_extracted_shards_paths[subset]):
                msg = "the number of shards must be equal to the number of paths"
                raise ValueError(msg)

            is_drums = subset == "drums"
            with Path(metadata_paths[subset]).open() as file:
                metadata = json.load(file)

            for music_shard, local_extracted_shard_path in zip(
                music_shards[subset], local_extracted_shards_paths[subset]
            ):
                for music_file_name, music_file in music_shard:
                    md5 = music_file_name.split(".")[0]
                    path = (
                        str(Path(str(local_extracted_shard_path)) / music_file_name)
                        if local_extracted_shard_path
                        else music_file_name
                    )

                    metadata_ = metadata.get(md5, {})
                    yield (
                        md5,
                        {
                            "md5": md5,
                            "music": {"path": path, "bytes": music_file.read()},
                            "is_drums": is_drums,
                            "sid_matches": [
                                {"sid": sid, "score": score}
                                for sid, score in metadata_.get("sid_matches", [])
                            ],
                            "mbid_matches": [
                                {"sid": sid, "mbids": mbids}
                                for sid, mbids in metadata_.get("mbid_matches", [])
                            ],
                            "artist_scraped": metadata_.get("artist_scraped", None),
                            "title_scraped": metadata_.get("title_scraped", None),
                            "genres_scraped": metadata_.get("genres_scraped", None),
                            "genres_discogs": [
                                {"genre": genre, "count": count}
                                for genre, count in metadata_.get(
                                    "genres_discogs", {}
                                ).items()
                            ],
                            "genres_tagtraum": [
                                {"genre": genre, "count": count}
                                for genre, count in metadata_.get(
                                    "genres_tagtraum", {}
                                ).items()
                            ],
                            "genres_lastfm": [
                                {"genre": genre, "count": count}
                                for genre, count in metadata_.get(
                                    "genres_lastfm", {}
                                ).items()
                            ],
                            "median_metric_depth": metadata_.get(
                                "median_metric_depth", None
                            ),
                            # "loops": metadata_.get("loops", None),
                        },
                    )

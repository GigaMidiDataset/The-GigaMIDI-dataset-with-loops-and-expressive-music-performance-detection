---
annotations_creators: []
license:
- cc-by-4.0
- other
pretty_name: GigaMIDI
size_categories: []
source_datasets: []
tags: []
task_ids: []
---

# Dataset Card for GigaMIDI

## Table of Contents

- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [How to use](#how-to-use)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
<!--  - [Citation Information](#citation-information) -->

## Dataset Description

<!-- - **Homepage:** https://metacreation.net/GigaMIDI -->
- **Repository:** Anonymized during the peer review process
<!-- - **Paper:**  -->
- **Point of Contact:** Anonymized during the peer review process

### Dataset Summary

The GigaMIDI dataset is a corpus of over 1 million MIDI files covering all music genres.

We provide three subsets: `drums-only`, which contain MIDI files exclusively containing drum tracks, `no-drums` for MIDI files containing any MIDI program except drums (channel 10) and `all-instruments-with-drums` for MIDI files containing multiple MIDI programs including drums. The `all` subset encompasses the three to get the full dataset.

## How to use

The `datasets` library allows you to load and pre-process your dataset in pure Python at scale. The dataset can be downloaded and prepared in one call to your local drive by using the `load_dataset` function.

```python
from datasets import load_dataset

dataset = load_dataset("Metacreation/GigaMIDI", "all-instruments-with-drums", trust_remote_code=True)
```

You can load combinations of specific subsets by using the `subset` keyword argument when loading the dataset:

```Python
from datasets import load_dataset

dataset = load_dataset("Metacreation/GigaMIDI", "music", subsets=["no-drums", "all-instruments-with-drums"], trust_remote_code=True)
```

Using the datasets library, you can also stream the dataset on-the-fly by adding a `streaming=True` argument to the `load_dataset` function call. Loading a dataset in streaming mode loads individual samples of the dataset at a time, rather than downloading the entire dataset to disk.

```python
from datasets import load_dataset

dataset = load_dataset(
    "Metacreation/GigaMIDI", "all-instruments-with-drums", trust_remote_code=True, streaming=True
)

print(next(iter(dataset)))
```

*Bonus*: create a [PyTorch dataloader](https://huggingface.co/docs/datasets/use_with_pytorch) directly with your own datasets (local/streamed).

### Local

```python
from datasets import load_dataset
from torch.utils.data.sampler import BatchSampler, RandomSampler

dataset = load_dataset("Metacreation/GigaMIDI", "all-instruments-with-drums", trust_remote_code=True, split="train")
batch_sampler = BatchSampler(RandomSampler(dataset), batch_size=32, drop_last=False)
dataloader = DataLoader(dataset, batch_sampler=batch_sampler)
```

### Streaming

```python
from datasets import load_dataset
from torch.utils.data import DataLoader

dataset = load_dataset("Metacreation/GigaMIDI", "all-instruments-with-drums", trust_remote_code=True, split="train")
dataloader = DataLoader(dataset, batch_size=32)
```

### Example scripts

MIDI files can be easily loaded and tokenized with [Symusic](https://github.com/Yikai-Liao/symusic) and [MidiTok](https://github.com/Natooz/MidiTok) respectively.

```python
from datasets import load_dataset

dataset = load_dataset("Metacreation/GigaMIDI", "all-instruments-with-drums", trust_remote_code=True, split="train")
```

The dataset can be [processed](https://huggingface.co/docs/datasets/process) by using the `dataset.map` and  `dataset.filter` methods.

```Python
from pathlib import Path
from datasets import load_dataset
from miditok.constants import SCORE_LOADING_EXCEPTION
from miditok.utils import get_bars_ticks
from symusic import Score

def is_score_valid(
    score: Score | Path | bytes, min_num_bars: int, min_num_notes: int
) -> bool:
    """
    Check if a ``symusic.Score`` is valid, contains the minimum required number of bars.

    :param score: ``symusic.Score`` to inspect or path to a MIDI file.
    :param min_num_bars: minimum number of bars the score should contain.
    :param min_num_notes: minimum number of notes that score should contain.
    :return: boolean indicating if ``score`` is valid.
    """
    if isinstance(score, Path):
        try:
            score = Score(score)
        except SCORE_LOADING_EXCEPTION:
            return False
    elif isinstance(score, bytes):
        try:
            score = Score.from_midi(score)
        except SCORE_LOADING_EXCEPTION:
            return False

    return (
        len(get_bars_ticks(score)) >= min_num_bars and score.note_num() > min_num_notes
    )

dataset = load_dataset("Metacreation/GigaMIDI", "all-instruments-with-drums", trust_remote_code=True, split="train")
dataset = dataset.filter(
    lambda ex: is_score_valid(ex["music"]["bytes"], min_num_bars=8, min_num_notes=50)
)
```

## Dataset Structure

### Data Instances

A typical data sample comprises the `md5` of the file which corresponds to its file name, a `music` entry containing dictionary mapping to its absolute file `path` and `bytes` that can be loaded with `symusic` as `score = Score.from_midi(dataset[sample_idx]["music"]["bytes"])`.
Metadata accompanies each file, which is introduced in the next section.

A data sample indexed from the dataset may look like this (the `bytes` entry is voluntarily shorten):

```python
{
    'md5': '0211bbf6adf0cf10d42117e5929929a4',
    'music': {'path': '/Users/nathan/.cache/huggingface/datasets/downloads/extracted/cc8e36bbe8d5ec7ecf1160714d38de3f2f670c13bc83e0289b2f1803f80d2970/0211bbf6adf0cf10d42117e5929929a4.mid', 'bytes': b"MThd\x00\x00\x00\x06\x00\x01\x00\x05\x01\x00MTrk\x00"},
    'is_drums': False,
    'sid_matches': {'sid': ['065TU5v0uWSQmnTlP5Cnsz', '29OG7JWrnT0G19tOXwk664', '2lL9TiCxUt7YpwJwruyNGh'], 'score': [0.711, 0.8076, 0.8315]},
    'mbid_matches': {'sid': ['065TU5v0uWSQmnTlP5Cnsz', '29OG7JWrnT0G19tOXwk664', '2lL9TiCxUt7YpwJwruyNGh'], 'mbids': [['43d521a9-54b0-416a-b15e-08ad54982e63', '70645f54-a13d-4123-bf49-c73d8c961db8', 'f46bba68-588f-49e7-bb4d-e321396b0d8e'], ['43d521a9-54b0-416a-b15e-08ad54982e63', '70645f54-a13d-4123-bf49-c73d8c961db8'], ['3a4678e6-9d8f-4379-aa99-78c19caf1ff5']]},
    'artist_scraped': 'Bach, Johann Sebastian',
    'title_scraped': 'Contrapunctus 1 from Art of Fugue',
    'genres_scraped': ['classical', 'romantic'],
    'genres_discogs': {'genre': ['classical', 'classical---baroque'], 'count': [14, 1]},
    'genres_tagtraum': {'genre': ['classical', 'classical---baroque'], 'count': [1, 1]},
    'genres_lastfm': {'genre': [], 'count': []},
    'median_metric_depth': [0, 0, 0, 0]
}
```

### Data Fields

The GigaMIDI dataset comprises the [MetaMIDI dataset](https://www.metacreation.net/projects/metamidi-dataset). Consequently, the GigaMIDI dataset also contains its [metadata](https://github.com/jeffreyjohnens/MetaMIDIDataset) which we compiled here in a convenient and easy to use dataset format. The fields of each data entry are:

* `md5` (`string`): hash the MIDI file, corresponding to its file name;
* `music` (`dict`): a dictionary containing the absolute `path` to the downloaded file and the file content as `bytes` to be loaded with an external Python package such as symusic;
* `is_drums` (`boolean`): whether the sample comes from the `drums` subset, this can be useful when working with the `all` subset;
* `sid_matches` (`dict[str, list[str] | list[float16]]`): ids of the Spotify entries matched and their scores.
* `mbid_matches` (`dict[str, str | list[str]]`): ids of the MusicBrainz entries matched with the Spotify entries.
* `artist_scraped` (`string`): scraped artist of the entry;
* `title_scraped` (`string`): scraped song title of the entry;
* `genres_scraped` (`list[str]`): scraped genres of the entry;
* `genres_discogs` (`dict[str, list[str] | list[int16]]`): Discogs genres matched from the [AcousticBrainz dataset](https://multimediaeval.github.io/2018-AcousticBrainz-Genre-Task/data/);
* `genres_tagtraum` (`dict[str, list[str] | list[int16]]`): Tagtraum genres matched from the [AcousticBrainz dataset](https://multimediaeval.github.io/2018-AcousticBrainz-Genre-Task/data/);
* `genres_lastfm` (`dict[str, list[str] | list[int16]]`): Lastfm genres matched from the [AcousticBrainz dataset](https://multimediaeval.github.io/2018-AcousticBrainz-Genre-Task/data/);
* `median_metric_depth` (`list[int16]`):
<!--* `loop` (`string`): -->

### Data Splits

The dataset has been subdivided into portions for training (`train`), validation (`validation`) and testing (`test`).

The validation and test splits contain each 10% of the dataset, while the training split contains the rest (about 80%).

## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

## Considerations for Using the Data

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

Public Domain, [CC-0](https://creativecommons.org/share-your-work/public-domain/cc0/)

<!--### Citation Information

```
@inproceedings{
}
```-->

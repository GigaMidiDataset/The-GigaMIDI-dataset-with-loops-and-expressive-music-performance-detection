#!/usr/bin/python3 python

"""Measuring the length of GigaMIDI files in bars."""

if __name__ == "__main__":
    from pathlib import Path

    import numpy as np
    from datasets import concatenate_datasets, load_dataset
    from matplotlib import pyplot as plt
    from miditok.constants import SCORE_LOADING_EXCEPTION
    from miditok.utils import get_bars_ticks
    from symusic import Score
    from tqdm import tqdm
    from transformers import set_seed

    from utils.GigaMIDI.GigaMIDI import _SUBSETS
    from utils.utils import path_data_directory_local_fs

    SEED = 777
    NUM_FILES = 5000
    NUM_HIST_BINS = 25
    X_AXIS_LIM_BARS = 300
    X_AXIS_LIM_BEATS = X_AXIS_LIM_BARS * 4
    set_seed(SEED)
    FIGURES_PATH = Path("scripts", "analysis", "figures")

    # Measuring lengths in bars/beats
    dist_lengths_bars = {}
    for subset_name in _SUBSETS:
        subset = concatenate_datasets(
            list(
                load_dataset(
                    str(path_data_directory_local_fs() / "GigaMIDI"),
                    subset_name,
                    trust_remote_code=True,
                ).values()
            )
        ).shuffle()
        dist_lengths_bars[subset_name] = []

        idx = 0
        with tqdm(total=NUM_FILES, desc=f"Analyzing `{subset_name}` subset") as pbar:
            while len(dist_lengths_bars[subset_name]) < NUM_FILES and idx < len(subset):
                try:
                    score = Score.from_midi(subset[idx]["music"]["bytes"])
                    dist_lengths_bars[subset_name].append(len(get_bars_ticks(score)))
                    pbar.update(1)
                except SCORE_LOADING_EXCEPTION:
                    pass
                finally:
                    idx += 1

    # Plotting length (bars) distribution
    for subset_name in dist_lengths_bars:
        dist_arr = np.array(dist_lengths_bars[subset_name])
        dist_lengths_bars[subset_name] = dist_arr[
            np.where(dist_arr <= X_AXIS_LIM_BARS)[0]
        ]
    fig, ax = plt.subplots()
    ax.hist(
        dist_lengths_bars.values(),
        bins=NUM_HIST_BINS,
        density=True,
        label=dist_lengths_bars.keys(),
    )
    ax.grid(axis="y", linestyle="--", linewidth=0.6)
    ax.legend(prop={"size": 10})
    ax.set_ylabel("Density")
    ax.set_xlabel("Duration in bars")
    fig.savefig(
        FIGURES_PATH / "GigaMIDI_duration_bars.pdf", bbox_inches="tight", dpi=300
    )
    plt.close(fig)

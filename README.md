# The-GigaMIDI-dataset-with-loops-and-expressive-music-performance-detection
# Summary 
Research in computational creativity and music information retrieval (MIR) gained significant traction with the progress of deep learning. This research and the resulting applications require data to train models that can perform tasks such as music generation or transcription efficiently and with good performances.
The majority of the public music datasets contain audio data. Meanwhile, musical instrument digital interface (MIDI) data presents advantages over audio, such as providing a convenient way to align music and consider its original features, such as tempo, time signature, or effects, that are absent from audio. In the era of data-driven models, however, the existing symbolic music datasets are relatively small by number of files and file sizes.
Moreover, there is only a limited amount of metadata and algorithms to differentiate expressive symbolic music data performed by a musician from non-expressive data that can be assimilated to music scores.
To address these challenges, we present the GigaMIDI dataset, a comprehensive corpus comprising over 1.43M MIDI files, 5.3M tracks, and 1.8B notes, along with annotations for loops and metadata for expressive performance detection. The GigaMIDI dataset is openly accessible on the Hugging Face hub [https://huggingface.co/datasets/h5ecv89/anon] in a user-friendly way.
To measure their expressiveness, we introduced a new heuristic called note onset median metric level (NOMML), which allowed us to identify 69% non-expressive and 31% expressive MIDI tracks.
Detecting loops, or repetitions of musical patterns, presents a challenge when tracks exhibit expressive timing variations, as repeated patterns may not be strictly identical. To address this issue, we integrate our NOMML heuristic with a MIDI-based loop detection method specifically designed for non-expressive music tracks, which allows for the identification of 7M loops.

# Instruction for using the note onset median metric level (NOMML)
Using with the command line
usage: python main.py [-h] --folder FOLDER [--force] [--nthreads NTHREADS]
Install and import Libraries for the NOMML code: os, glob, json, random, numpy, tqdm, Pool
symusic library is used for MIDI parsing.
# 

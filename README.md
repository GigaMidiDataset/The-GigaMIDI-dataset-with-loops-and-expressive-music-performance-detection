# GitHub Repository of Paper titled "The GigaMIDI dataset with loops and expressive music performance detection"
# Summary 
Research in artificial intelligence applications in music computing has gained significant traction with the progress of deep learning. Musical instrument digital interface (MIDI) data and its associated metadata are fundamental for the advancement of models that execute tasks such as music generation and transcription with optimal efficiency and high-performance quality. The majority of the public music datasets contain audio data, and symbolic music datasets are comparatively small. However, MIDI data presents advantages over audio, such as providing an editable version of musical content independent of its sonic rendering. MIDI data can be quantized or interpreted with variations in micro-timing and velocity, but there is only a limited amount of metadata and algorithms to differentiate expressive symbolic music data performed by a musician from non-expressive data that can be assimilated into music scores. To address these challenges, we present the GigaMIDI dataset, a comprehensive corpus comprising over 1.43M MIDI files, 5.3M tracks, and 1.8B notes, along with annotations for loops and metadata for expressive performance detection. To detect expressiveness, which tracks reflect human interpretation, we introduced a new heuristic called note onset median metric level (NOMML), which allowed us to identify with 99.5\% accuracy that 31\% of GigaMIDI tracks are expressive. Detecting loops, or repetitions of musical patterns, presents a challenge when tracks exhibit expressive timing variations, as repeated patterns may not be strictly identical. To address this issue, we mark MIDI loops for non-expressive music tracks, which allows us to identify 7M loops. The GigaMIDI dataset is accessible for research purposes on the Hugging Face hub [https://huggingface.co/datasets/h5ecv89/anon] in a user-friendly way for convenience and reproducibility.

# Instruction for using the code for note onset median metric level (NOMML) heuristic
## Install and import Libraries for the NOMML code: <br /> 
Imported libraries: os, glob, json, random, numpy, tqdm, Pool, symusic (pip install required for numpy, tqdm and symusic) <br />
Note: symusic library is used for MIDI parsing.

## Using with the command line  <br />
usage: python main.py [-h] --folder FOLDER [--force] [--nthreads NTHREADS]  <br />

# Instruction for the MIDI-based music loop detection method <br />

# Analysis of Evaluation Set and Optimal Threshold Selection
The Analysis of Evaluation Set and Optimal Threshold Selection.zip archive contains CSV files corresponding to our training set, which were utilized to identify optimal thresholds for each heuristic in expressive music performance detection. These files include percentile calculations used to determine the optimal thresholds. The rationale behind employing percentiles from the data distribution is to delineate the boundary between non-expressive and expressive tracks based on the values of our heuristic features.

# Acknowledgement
Anonymized upon de-anonymization during the peer review process.

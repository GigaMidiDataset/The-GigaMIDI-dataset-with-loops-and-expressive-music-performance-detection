#!/usr/bin/python3 python

"""
Counts the programs in the MegaMIDI dataset.

Results:
Program -1 (Drums): 61400 (0.226%)
Program 0 (Acoustic Grand Piano): 41079 (0.151%)
Program 1 (Bright Acoustic Piano): 2511 (0.009%)
Program 2 (Electric Grand Piano): 891 (0.003%)
Program 3 (Honky-tonk Piano): 572 (0.002%)
Program 4 (Electric Piano 1): 2156 (0.008%)
Program 5 (Electric Piano 2): 1466 (0.005%)
Program 6 (Harpsichord): 1727 (0.006%)
Program 7 (Clavi): 621 (0.002%)
Program 8 (Celesta): 407 (0.001%)
Program 9 (Glockenspiel): 1167 (0.004%)
Program 10 (Music Box): 405 (0.001%)
Program 11 (Vibraphone): 1898 (0.007%)
Program 12 (Marimba): 924 (0.003%)
Program 13 (Xylophone): 440 (0.002%)
Program 14 (Tubular Bells): 717 (0.003%)
Program 15 (Dulcimer): 133 (0.000%)
Program 16 (Drawbar Organ): 883 (0.003%)
Program 17 (Percussive Organ): 874 (0.003%)
Program 18 (Rock Organ): 1627 (0.006%)
Program 19 (Church Organ): 520 (0.002%)
Program 20 (Reed Organ): 158 (0.001%)
Program 21 (Accordion): 997 (0.004%)
Program 22 (Harmonica): 808 (0.003%)
Program 23 (Tango Accordion): 343 (0.001%)
Program 24 (Acoustic Guitar (nylon)): 3478 (0.013%)
Program 25 (Acoustic Guitar (steel)): 7235 (0.027%)
Program 26 (Electric Guitar (jazz)): 3503 (0.013%)
Program 27 (Electric Guitar (clean)): 4416 (0.016%)
Program 28 (Electric Guitar (muted)): 2767 (0.010%)
Program 29 (Overdriven Guitar): 3219 (0.012%)
Program 30 (Distortion Guitar): 3253 (0.012%)
Program 31 (Guitar Harmonics): 299 (0.001%)
Program 32 (Acoustic Bass): 3075 (0.011%)
Program 33 (Electric Bass (finger)): 6316 (0.023%)
Program 34 (Electric Bass (pick)): 831 (0.003%)
Program 35 (Fretless Bass): 3110 (0.011%)
Program 36 (Slap Bass 1): 354 (0.001%)
Program 37 (Slap Bass 2): 298 (0.001%)
Program 38 (Synth Bass 1): 1477 (0.005%)
Program 39 (Synth Bass 2): 887 (0.003%)
Program 40 (Violin): 1558 (0.006%)
Program 41 (Viola): 672 (0.002%)
Program 42 (Cello): 909 (0.003%)
Program 43 (Contrabass): 750 (0.003%)
Program 44 (Tremolo Strings): 666 (0.002%)
Program 45 (Pizzicato Strings): 2260 (0.008%)
Program 46 (Orchestral Harp): 1304 (0.005%)
Program 47 (Timpani): 2109 (0.008%)
Program 48 (String Ensembles 1): 9898 (0.036%)
Program 49 (String Ensembles 2): 3749 (0.014%)
Program 50 (SynthStrings 1): 3028 (0.011%)
Program 51 (SynthStrings 2): 740 (0.003%)
Program 52 (Choir Aahs): 5394 (0.020%)
Program 53 (Voice Oohs): 2101 (0.008%)
Program 54 (Synth Voice): 1288 (0.005%)
Program 55 (Orchestra Hit): 460 (0.002%)
Program 56 (Trumpet): 5559 (0.020%)
Program 57 (Trombone): 4676 (0.017%)
Program 58 (Tuba): 2099 (0.008%)
Program 59 (Muted Trumpet): 649 (0.002%)
Program 60 (French Horn): 3926 (0.014%)
Program 61 (Brass Section): 2340 (0.009%)
Program 62 (Synth Brass 1): 994 (0.004%)
Program 63 (Synth Brass 2): 449 (0.002%)
Program 64 (Soprano Sax): 544 (0.002%)
Program 65 (Alto Sax): 3359 (0.012%)
Program 66 (Tenor Sax): 2479 (0.009%)
Program 67 (Baritone Sax): 1081 (0.004%)
Program 68 (Oboe): 2669 (0.010%)
Program 69 (English Horn): 499 (0.002%)
Program 70 (Bassoon): 2029 (0.007%)
Program 71 (Clarinet): 4666 (0.017%)
Program 72 (Piccolo): 1202 (0.004%)
Program 73 (Flute): 4962 (0.018%)
Program 74 (Recorder): 434 (0.002%)
Program 75 (Pan Flute): 1034 (0.004%)
Program 76 (Blown Bottle): 133 (0.000%)
Program 77 (Shakuhachi): 205 (0.001%)
Program 78 (Whistle): 359 (0.001%)
Program 79 (Ocarina): 345 (0.001%)
Program 80 (Lead 1 (square)): 1422 (0.005%)
Program 81 (Lead 2 (sawtooth)): 2021 (0.007%)
Program 82 (Lead 3 (calliope)): 913 (0.003%)
Program 83 (Lead 4 (chiff)): 127 (0.000%)
Program 84 (Lead 5 (charang)): 259 (0.001%)
Program 85 (Lead 6 (voice)): 281 (0.001%)
Program 86 (Lead 7 (fifths)): 84 (0.000%)
Program 87 (Lead 8 (bass + lead)): 876 (0.003%)
Program 88 (Pad 1 (new age)): 931 (0.003%)
Program 89 (Pad 2 (warm)): 1222 (0.004%)
Program 90 (Pad 3 (polysynth)): 725 (0.003%)
Program 91 (Pad 4 (choir)): 669 (0.002%)
Program 92 (Pad 5 (bowed)): 260 (0.001%)
Program 93 (Pad 6 (metallic)): 241 (0.001%)
Program 94 (Pad 7 (halo)): 364 (0.001%)
Program 95 (Pad 8 (sweep)): 508 (0.002%)
Program 96 (FX 1 (rain)): 204 (0.001%)
Program 97 (FX 2 (soundtrack)): 87 (0.000%)
Program 98 (FX 3 (crystal)): 271 (0.001%)
Program 99 (FX 4 (atmosphere)): 478 (0.002%)
Program 100 (FX 5 (brightness)): 754 (0.003%)
Program 101 (FX 6 (goblins)): 121 (0.000%)
Program 102 (FX 7 (echoes)): 301 (0.001%)
Program 103 (FX 8 (sci-fi)): 144 (0.001%)
Program 104 (Sitar): 206 (0.001%)
Program 105 (Banjo): 474 (0.002%)
Program 106 (Shamisen): 135 (0.000%)
Program 107 (Koto): 164 (0.001%)
Program 108 (Kalimba): 224 (0.001%)
Program 109 (Bag pipe): 87 (0.000%)
Program 110 (Fiddle): 243 (0.001%)
Program 111 (Shanai): 33 (0.000%)
Program 112 (Tinkle Bell): 110 (0.000%)
Program 113 (Agogo): 53 (0.000%)
Program 114 (Steel Drums): 181 (0.001%)
Program 115 (Woodblock): 143 (0.001%)
Program 116 (Taiko Drum): 235 (0.001%)
Program 117 (Melodic Tom): 187 (0.001%)
Program 118 (Synth Drum): 362 (0.001%)
Program 119 (Reverse Cymbal): 1228 (0.005%)
Program 120 (Guitar Fret Noise, Guitar Cutting Noise): 346 (0.001%)
Program 121 (Breath Noise, Flute Key Click): 72 (0.000%)
Program 122 (Seashore, Rain, Thunder, Wind, Stream, Bubbles): 407 (0.001%)
Program 123 (Bird Tweet, Dog, Horse Gallop): 85 (0.000%)
Program 124 (Telephone Ring, Door Creaking, Door, Scratch, Wind Chime): 185 (0.001%)
Program 125 (Helicopter, Car Sounds): 158 (0.001%)
Program 126 (Applause, Laughing, Screaming, Punch, Heart Beat, Footstep): 185 (0.001%)
Program 127 (Gunshot, Machine Gun, Lasergun, Explosion): 208 (0.001%)
"""

if __name__ == "__main__":
    from random import shuffle

    import numpy as np
    from miditok.constants import MIDI_INSTRUMENTS, SCORE_LOADING_EXCEPTION
    from symusic import Score
    from tqdm import tqdm
    from transformers.trainer_utils import set_seed

    from utils.baseline import is_score_valid, mmm

    set_seed(mmm.seed)

    NUM_FILES = 100000
    mmm.tokenizer.config.programs = list(range(-1, 128))

    # Iterate over files
    dataset_files_paths = mmm.dataset_files_paths
    shuffle(dataset_files_paths)
    dataset_files_paths = dataset_files_paths[:NUM_FILES]
    all_programs = []
    for file_path in tqdm(dataset_files_paths, desc="Analyzing files"):
        try:
            score = Score(file_path)
        except SCORE_LOADING_EXCEPTION:
            continue
        if is_score_valid(score):
            score = mmm.tokenizer.preprocess_score(score)
            all_programs += [
                track.program if not track.is_drum else -1 for track in score.tracks
            ]

    all_programs = np.array(all_programs)
    for program in range(-1, 128):
        num_occurrences = len(np.where(all_programs == program)[0])
        ratio = num_occurrences / len(all_programs)
        print(  # noqa: T201
            f"Program {program} ("
            f"{'Drums' if program == -1 else MIDI_INSTRUMENTS[program]['name']}): "
            f"{num_occurrences} ({ratio:.3f}%)"
        )

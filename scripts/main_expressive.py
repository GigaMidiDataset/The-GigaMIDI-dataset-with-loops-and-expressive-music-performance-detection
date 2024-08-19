from loops_nomml.process_file import detect_loops
import os
from datasets import Dataset, load_dataset

DATA_PATH = "D:\\Documents\\GigaMIDI"
METADATA_NAME = "Expressive_Performance_Detection_NOMML_gigamidi_tismir.csv"
SHARD_SIZE = 20000
OUTPUT_NAME = "gigamidi_expressive_loops_no_quant"

if __name__ == "__main__":
    metadata_path = os.path.join(DATA_PATH, METADATA_NAME)
    output_path = os.path.join(DATA_PATH, OUTPUT_NAME)
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    dataset = load_dataset("csv", data_files=metadata_path)['train']
    print(f"loaded {len(dataset)} tracks")
    dataset_expressive = dataset.filter(lambda row: row['medianMetricDepth'] == 12)
    print(f"filtered to {len(dataset_expressive)} expressive tracks")
    dataset_with_time_signature = dataset_expressive.filter(lambda row: row['hasTimeSignatures'])
    print(f"filtered to {len(dataset_with_time_signature)} expressive tracks with time signatures")

    unique_files = dataset_with_time_signature.unique('filepath')
    unique_files = [{"file_path": os.path.join(DATA_PATH, file_path), "file_name": file_path} for file_path in unique_files]
    unique_files_dataset = Dataset.from_list(unique_files)
    print(f"filtered to {len(unique_files_dataset)} unique MIDI files, expressive with time signatures")
    unique_files_dataset = unique_files_dataset.shuffle(seed=42)

    num_shards = int(round(len(unique_files_dataset) / SHARD_SIZE))
    print(f"Splitting dataset in {num_shards} shards")
    print(f"Saving shards to {output_path}")
    for shard_idx in range(num_shards):
        shard = unique_files_dataset.shard(num_shards=num_shards, index=shard_idx)
        shard = shard.map(
            detect_loops,
            remove_columns=['file_path', 'file_name'],
            batched=True,
            batch_size=1,
            writer_batch_size=1,
            num_proc=8
        )

        csv_path = os.path.join(output_path, OUTPUT_NAME + "_" + str(shard_idx) + ".csv")
        shard.to_csv(csv_path)

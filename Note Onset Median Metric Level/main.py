import os
import glob
import json
import random
import numpy as np
from tqdm import tqdm
from multiprocessing import Pool
from symusic import Score

def load_json(path, default=[]):
	with open(path, "r") as f:
		return json.load(f)

def dump_json(x, path):
	with open(path, "w") as f:
		json.dump(x, f, indent=4)

def get_metric_depth(time, tpq, max_depth=6):
	for i in range(max_depth):
		period = tpq / int(2**i)
		if time % period == 0:
			return 2*i
	for i in range(max_depth):
		period = tpq * 2 / (int(2**i) * 3)
		if time % period == 0:
			return 2*i + 1
	return max_depth * 2

def get_median_metric_depth(path):
	mf = Score(path)
	median_metric_depths = []
	for track in mf.tracks:
		metric_depths = [get_metric_depth(event.time, mf.tpq) for event in track.notes]
		if len(metric_depths) > 0:
			median_metric_depths.append( int(np.median(metric_depths)) )
	return path, median_metric_depths

def worker(args):
	try:
		return get_median_metric_depth(*args)
	except Exception as e:
		print("FAILED : ", e)
		return None

def main(folder, force=False, nthreads=8):
	output_path = os.path.basename(folder).lower() + ".json"
	if os.path.exists(output_path) and force==False:
		return load_json(output_path)

	paths = [glob.glob(folder + f"/**/*.{ext}", recursive=True) for ext in ["mid", "midi", "MID"]]
	paths = [p for sublist in paths for p in sublist]
	random.shuffle(paths)

	count = 0
	result = {}
	p = Pool(nthreads)
	filter_none = lambda x : x != None
	for path,median_metric_depths in filter(filter_none,tqdm(p.imap_unordered(worker, [(p,) for p in paths]),total=len(paths))):
		result[os.path.relpath(path, folder)] = median_metric_depths
		if (count % 50000 == 0):
			dump_json(result, output_path)
		count += 1
	dump_json(result, output_path)
	return result

if __name__ == "__main__":

	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("--folder", type=str, default="", required=True)
	parser.add_argument("--force", action="store_true")
	parser.add_argument("--nthreads", type=int, default=8)
	args = parser.parse_args()
	main(args.folder, force=args.force, nthreads=args.nthreads)
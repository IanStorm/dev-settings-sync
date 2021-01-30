#!/usr/bin/python3
import filecmp
import os
import sys

import common

def _get_non_matching_files():
	non_matching_files = []
	for rel_filepath in common.get_overlapping_files():
		file_1 = os.path.join(common.SYNC_DIR, rel_filepath)
		file_2 = os.path.join(common.MNT_DIR, rel_filepath)
		if not filecmp.cmp(file_1, file_2):
			non_matching_files.append(rel_filepath)
	return non_matching_files

def main():
	non_matching_files = _get_non_matching_files()
	if len(non_matching_files) != 0:
		for rel_filepath in non_matching_files:
			print(u'"', rel_filepath , u'" files do not match.', sep='')
		sys.exit(1)
	else:
		print(u'All overlapping files are up-to-date.')
		sys.exit(0)

if __name__ == '__main__':
	main()

#!/usr/bin/python3
import os
import shutil
import sys

import common

def main():
	for rel_filepath in common.get_overlapping_files():
		src_filepath = os.path.join(common.DEV_ENV_DIR, rel_filepath)
		dst_filepath = os.path.join(common.MNT_DIR, rel_filepath)
		shutil.copyfile(src_filepath, dst_filepath)
		print(u'Updated "', rel_filepath, u'" successfully.', sep='')
	sys.exit(0)

if __name__ == '__main__':
	main()

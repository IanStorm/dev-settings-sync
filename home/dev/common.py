import os

MNT_DIR = u'/mnt/'
SYNC_DIR = u'/opt/dev-settings-sync/'

def get_overlapping_files():
	overlapping_files = []
	for rel_filepath in _get_sync_rel_filepaths():
		mnt_filepath = os.path.join(MNT_DIR, rel_filepath)
		if os.path.isfile(mnt_filepath):
			overlapping_files.append(rel_filepath)
	return overlapping_files

def _get_sync_rel_filepaths():
	sync_rel_filepaths = []
	for subdir, dirs, files in os.walk(SYNC_DIR):
		for filename in files:
			filepath = os.path.join(subdir, filename)
			rel_filepath = os.path.join('.', os.path.relpath(filepath, SYNC_DIR))
			sync_rel_filepaths.append(rel_filepath)
	return sync_rel_filepaths

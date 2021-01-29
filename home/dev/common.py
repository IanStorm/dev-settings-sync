import os

DEV_ENV_DIR = u'/opt/dev-env/'
MNT_DIR = u'/mnt/'

def get_overlapping_files():
	overlapping_files = []
	for rel_filepath in _get_dev_env_rel_filepaths():
		mnt_filepath = os.path.join(MNT_DIR, rel_filepath)
		if os.path.isfile(mnt_filepath):
			overlapping_files.append(rel_filepath)
	return overlapping_files

def _get_dev_env_rel_filepaths():
	dev_env_rel_filepaths = []
	for subdir, dirs, files in os.walk(DEV_ENV_DIR):
		for filename in files:
			filepath = os.path.join(subdir, filename)
			rel_filepath = os.path.join('.', os.path.relpath(filepath, DEV_ENV_DIR))
			dev_env_rel_filepaths.append(rel_filepath)
	return dev_env_rel_filepaths

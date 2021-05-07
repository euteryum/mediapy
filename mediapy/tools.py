import os
from pathlib import Path


## Private methods
def _pathExists(filePath):
	return os.path.exists(filePath)

def _ppError(msg):
	star_length = 13 + len(msg)    #13 represents length of hard-coded Error decoration
	print("*" * star_length)
	print("** Error: %s **" % msg)
	print("*" * star_length)


## Public methods
def makeDirectory(filePath):
	try:
		if not _pathExists(filePath):
			os.makedirs(filePath)
		else:
			msg = "Directory already exists."
			return _ppError(msg)
	except (IOError, OSError):
		msg = "Directory cannot be created!  Possibly permission error?"
		return _ppError(msg)

def osPathSplitHelper(pathToFile):
	pathObj           = Path(pathToFile)

	parentDir         = str(pathObj.parent)
	filename, fileExt = os.path.splitext(pathObj.name)

	return (parentDir, filename, fileExt)
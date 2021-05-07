################################################################################################################
################################################################################################################
## REFERENCE  :  https://truemansworld.blogspot.com/2021/04/gta-iii-trailer-maker.html
##               https://stackoverflow.com/questions/5585872/python-image-frames-to-video
##               https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python
## AUTHOR     :  euteryu
## Created on :  18/04/21
################################################################################################################
## WINDOWS:
## (path)  ==>  
## (venv)  ==>  C:\Users\minse\Desktop\Python_misc\python-virtual-environments\Movie\Scripts\activate.bat
##
## LINUX:
## (path)  ==>  ~/Python/Projects/mediapy/mediapy/video
## (venv)  ==>  source ~/Python/python-virtual-environments/mediapy/bin/activate
################################################################################################################
################################################################################################################


import cv2

import os
from pathlib import Path
import sys
sys.path.append('..')
import tools
import image.merge as merge


class Frames:
	## https://stackoverflow.com/questions/8376758/constructor-chaining-in-python
	## Multiple initialiser
	# def __init__(self, file, dir_In=absBaseDir, dir_Out=absBaseDir):
	# 	self.dir_In  = dir_In
	# 	self.dir_Out = dir_Out
	# 	self.file    = file

	def __init__(self, pathInput, pathOutput):
		self.pathInput  = pathInput
		self.pathOutput = pathOutput
		self.parentDirInput, self.filenameImg, self.imgExtInput   = tools.osPathSplitHelper(pathInput)
		self.parentDirOutput, self.filenameVid, self.vidExtOutput = tools.osPathSplitHelper(pathOutput)


	@staticmethod
	def _get_fps(video):
		return video.get(cv2.CAP_PROP_FPS)

	def extract_Frames(self):
		vidcap        = cv2.VideoCapture(self.pathInput)
		fps           = Frames._get_fps(vidcap)
		success, image = vidcap.read()

		count = 0
		while success:
			count += 1    #1-indexed i.e. frame1.jpg, frame2.jpg, ...
			# frame = f"{self.filenameImg}{count}{self.vidExtOutput}"
			frame = f"frame{count}.png"
			pathToFrame = os.path.join(self.parentDirOutput, frame)
			cv2.imwrite(pathToFrame, image) 
			success, image = vidcap.read()

		print(f"Frames per second  :  {fps}")
		print(f"{count} frames read.")
		print(f"Frames extracted to:  {self.parentDirOutput}")

	def combine_frames_helper(self, images, fps=30):
		##DEBUGGING
		# print(f"DEBUGGING: NO. OF IMAGES:  {len(images)}")

		## %1d necessary for incrementing in ffmpeg command below
		## e.g.  frame1.jpg, frame2.jpg, frame3.jpg, ...
		# frames     = "frames%01d.png"
		# pathToImgs = os.path.join(self.parentDirInput, frames)
		## Above 2 lines raises path not found; but it's not supposed to check for that!?
		pathToImgs = r'/home/minseok/Videos/Will_Ly/Merged/frame%01d_merged.png'

		## NOTE: No FileNotFoundError shall be thrown after all
		## I assume this is due to ffmpeg msg. not quite being a Python exception
		try:
			## image2 := image file demuxer
			conversionCmd = rf'ffmpeg -f image2 -r {fps} -i {pathToImgs} -c:v mpeg4 -y {self.pathOutput}'
			os.system(conversionCmd)
		except Exception as e:
			print(e)
		finally:
			print(f"Frames per second  :  {fps}")
			print(f"Movie created at   :  {self.parentDirOutput}")


	def combine_frames(self):
		valid_images = [img for img in os.listdir(self.parentDirInput) if img.endswith(f'.{self.imgExtInput}')]
		# print(len(valid_images))
		self.combine_frames_helper(images)


	def merge_combine_frames(self, images_path_input):
		merged_dir = self.parentDirOutput
		Frames._merge_with_sniper_scope(images_path_input, merged_dir)

		images = [img for img in os.listdir(merged_dir)]
		print(f"No. of images:  {len(images)} \n")
		self.combine_frames_helper(images)

	@staticmethod
	def _merge_with_sniper_scope(images_path_input, merged_dir):
	    path_overlay = r'/home/minseok/Downloads/sniper_scope.png'

		for img in os.listdir(images_path_input):
			if img.endswith('.png'):
				path_valid_image = os.path.join(images_path_input, img)
				images = merge.MergeImage(path_valid_image, merged_dir)
				images.composite_with(path_overlay)


############################################################################################################
############################################################################################################
def terminal_usage():
	print("Calling main()")
	homeDir       = str(Path.home())
	absBaseDir    = os.path.join(homeDir, 'Videos')               #HARD-CODED BASE PATH!!

	relInputDir   = input("Input dir   (may be left blank; currently ~/Videos):  ")
	relOutputDir  = input("Output dir  (may be left blank; currently ~/Videos):  ")
	dirIn         = os.path.join(absBaseDir, relInputDir)
	dirOut        = os.path.join(absBaseDir, relOutputDir)
	tools.makeDirectory(dirOut)

	filenameImg   = input("File name  (excl. extension)                       :  ")
	imgExtInput   = input("File extension type                                :  ")
	chosenFileExt = input("Choose file extension for output                   :  ")

	pathInput = os.path.join(dirIn, filenameImg + "." + imgExtInput)

	fileInput = Frames(pathInput, pathOutput)

	mode = input("Extract [e] or Combine [c]?  (Type appropriate letter):  ")
	if mode == 'e':
		fileInput.extract_Frames()
	elif mode == 'c':
		fps = input("Frames per second:  ")
		fileInput.combine_frames()
	else:
		msg = "Mode non-existent!"
		return ppError(msg)


def three_sec_test():
	dirIn     = absBaseDir
	dirOut    = os.path.join(absBaseDir, '3_sec')
	tools.makeDirectory(dirOut)
	pathInput = os.path.join(dirIn, '3_sec_vid_og.mkv')
	pathOut = os.path.join(dirOut, 'frame.jpg')

	video1 = Frames(pathInput, pathOut)
	video1.extract_Frames()

def scope_overlay_extract():
	homeDir       = str(Path.home())
	absBaseDir    = os.path.join(homeDir)               # HARD-CODED BASE PATH!!

	dirIn     = os.path.join(absBaseDir, 'Downloads')
	dirOut    = os.path.join(absBaseDir, 'Pictures/Will_Ly')
	tools.makeDirectory(dirOut)
	pathInput = os.path.join(dirIn, 'Will_Ly.mp4')
	pathOut = os.path.join(dirOut, 'frame.jpg')

	video1 = Frames(pathInput, pathOut)
	video1.extract_Frames()	

def scope_overlay_merge():
	homeDir       = str(Path.home())
	absBaseDir    = os.path.join(homeDir)               # HARD-CODED BASE PATH!!

	dir_in     = os.path.join(absBaseDir, 'Pictures/Will_Ly')
	dir_out    = os.path.join(absBaseDir, 'Videos/Will_Ly/Merged')
	tools.makeDirectory(dir_out)

	path_input = os.path.join(dir_in)
	path_out   = os.path.join(dir_out, 'Will_Ly_merged.mp4')

	images1 = Frames(path_input, path_out)
	images1.merge_combine_frames(path_input)


if __name__ == "__main__":
	# terminal_usage()
	# three_sec_test()
	# scope_overlay_extract()
	print("")
	scope_overlay_merge()


## EXAMPLE
'''
relInputDir  ==>  3_sec
file         ==>  3_sec_video.avi
mode         ==>  'e'
'''
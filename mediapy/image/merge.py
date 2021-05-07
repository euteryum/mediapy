################################################################################################################
################################################################################################################
## REFERENCE  :  https://moonbooks.org/Articles/How-to-overlay--superimpose-two-images-using-python-and-pillow-/
## AUTHOR     :  euteryu
## Created on :  20/12/20
################################################################################################################
## (venv)  ==>  C:\Users\minse\Desktop\Python_misc\python-virtual-environments\love\Scripts\activate.bat
################################################################################################################
################################################################################################################
'''
TO-DO:
0) https://packaging.python.org/tutorials/packaging-projects/
1) OVERLOAD CONVERSION METHODS, DEPENDING ON PARAMETERS
2) CREATE PRIVATE FUNCTION  <==  DRY PRINCIPLE, ABSTRACT LOGIC
'''

from PIL import Image, ImageDraw, ImageFilter
import cv2
import numpy as np

import os
import sys
sys.path.append('..')
import tools


class WhatDoesThisFunctionDo:
    def __init__(self, path_input, dst_dir):
        self.path_input = path_input
        self.src_dir, self.file_name, self.file_ext = tools.osPathSplitHelper(self.path_input)
        self.dst_dir = dst_dir

    def convertToHeartFramed(path_input, conversionMode='L'):
        path_alpha = r'/home/minseok/Downloads/heart.png'
        im_rgb = Image.open(self.path_input)
        im_a   = Image.open(path_alpha).convert(conversionMode).resize(im_rgb.size)

        im_rgba = im_rgb.copy()
        im_rgba.putalpha(im_a)
        im_rgba.save(os.path.join(self.dst_dir, self.file_name + '_alpha' + self.file_ext))


class MergeImage:
    def __init__(self, path_input, dst_dir):
        self.path_input = path_input
        self.src_dir, self.file_name, self.file_ext = tools.osPathSplitHelper(self.path_input)
        self.dst_dir = dst_dir


    ## Paste the (ideally) transparent (if not, smaller-than-base-image) picture OVER the given base "background" image
    def composite_with(self, path_overlay):
        try:
            overlay = Image.open(path_overlay).convert("RGBA")
            bg_img = Image.open(self.path_input)

            x, y = bg_img.size
            overlay = overlay.resize((x,y), Image.ANTIALIAS)
            bg_img.paste(overlay, (0, 0, x, y), overlay)    ## [PIL/Image.py]  self.im.paste(im, box, mask.im)

            outfile = os.path.join(self.dst_dir, self.file_name + '_merged.png')
            bg_img.save(outfile, "PNG")

        except IOError:
            print(f"IOError:  Cannot create {outfile}")    ## NOTE: JPG does not support transparency, alpha


# TESTING
def main():
    path_input = r'/home/minseok/Pictures/Will_Ly_bedroom.png'
    dst_dir    = r'/home/minseok/Downloads'

    img1 = MergeImage(path_input, dst_dir)
    path_overlay = r'/home/minseok/Downloads/sniper_scope.png'
    img1.composite_with(path_overlay)


if __name__=="__main__":
    main()
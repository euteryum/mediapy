'''
SOURCE: https://note.nkmk.me/en/python-pillow-square-circle-thumbnail/
'''

import os
import glob

from PIL import Image, ImageDraw, ImageFilter


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

'''
im_thumb = crop_center(im, thumb_width, thumb_width)
im_thumb.save('data/dst/lena_thumbnail_center_square.jpg', quality=95)
'''


def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

'''
im_thumb = crop_max_square(im).resize((thumb_width, thumb_width), Image.LANCZOS)
im_thumb.save('data/dst/lena_thumbnail_max_square.jpg', quality=95)
'''


def mask_circle_transparent(pil_img, blur_radius, offset=0):
    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)  # Mode L -- (8-bit grayscale)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

    result = pil_img.copy()
    result.putalpha(mask)

    return result



### In action for SINGLE image
##
##im = Image.open(r'C:\Users\minse\Pictures\Love\pub_parents.png')  # Used as input image
##thumb_width = 900
##
##im_square = crop_max_square(im).resize((thumb_width, thumb_width), Image.LANCZOS)
##im_thumb = mask_circle_transparent(im_square, 4)
##im_thumb.save(r'C:\Users\minse\Pictures\Love\thumbnails\pub_parents_thumbnailed.png')
##


def converToThumbnail(shape, numberOfFiles=2):
    if numberofFiles == 1:
        return 
        
### FINISH CLASS

def convertToCircularThumbnail():



def convertAllImagesInDir(source, ):
    ### Apply to MULTIPLE files in a directory
    src_dir = fr'C:\Users\minse\Pictures\Love'
    dst_dir = fr'C:\Users\minse\Pictures\Love\thumbnails'  # relative folder MUST pre-exist

    ##files = glob.glob(os.path.join(src_dir, '*.jpg'))  # Specify extension type
    files = glob.glob(os.path.join(src_dir, '*'))  # Any extension type

    for f in files:
        ftitle, fext = os.path.splitext(os.path.basename(f))
        rel_path = ftitle + '_thumbnail' + fext
        
        try:
            im = Image.open(f)
            thumb_width = 650
            
            im_square = crop_max_square(im).resize((thumb_width, thumb_width), Image.LANCZOS)
            im_thumb = mask_circle_transparent(im_square, 4)
            
            im_thumb.save(os.path.join(dst_dir, rel_path))
            ##im_thumb.save(os.path.join(dst_dir, ftitle + '_thumbnail' + fext), quality=95)
            
        except OSError as e:
            print('File is unsupported due to its extension type.')
            print(f'Skipping {ftitle + fext} <-- likely not an image...')
            print('')



'''
TO-DO:
-- Avoid overwriting if same image passed, but with different values
-- Possible solutions:
--  1)  Version numbers (check full path & increment; regex??)
--  2)  Unique extension (e.g. *_RYUSTUDIO; maybe combine with #1))
--  3)* Unique identifiers (viz. based on filename and selected options; shorten str length via hashing)
'''


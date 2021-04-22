############################## SOURCE: #########################################################
## https://stackoverflow.com/questions/64519818/converting-mkv-files-to-mp4-with-ffmpeg-python
## https://stackoverflow.com/questions/42438380/ffmpeg-in-python-script
## https://askubuntu.com/questions/396883/how-to-simply-convert-video-files-i-e-mkv-to-mp4
################################################################################################

import os
import ffmpeg

start_dir = os.getcwd()

def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + ".mp4"
    ffmpeg.input(mkv_file).output(out_name).run()
    print("Finished converting {}".format(mkv_file))

def main():
    for path, folder, files in os.walk(start_dir):
        for file in files:
            if file.endswith('.mkv'):
                print("Found file: %s" % file)
                convert_to_mp4(os.path.join(start_dir, file))
            else:
                pass


if __name__=="__main__":
    main()
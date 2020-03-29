import os
import sys
from moviepy.editor import VideoFileClip


def sec_to_hours(seconds):
    hours = seconds//3600
    mins = (seconds % 3600)//60
    seconds = (seconds % 3600) % 60
    return {'hours': hours, 'mins': mins, 'seconds': seconds}


if __name__ == "__main__":
    filelist = []
    for a, b, c in os.walk(sys.argv[1]):
        for name in c:
            fname = os.path.join(a, name)
            if fname.endswith(('.mp4', '.mkv', '.avi', '.wmv', '.rmvb', '.flv')):
                filelist.append(fname)
    ftime = 0.0
    for item in filelist:
        clip = VideoFileClip(item)
        ftime += clip.duration
        clip.close()
    print("%(hours)d hours %(mins)d mins %(seconds)d seconds" %
          sec_to_hours(ftime))

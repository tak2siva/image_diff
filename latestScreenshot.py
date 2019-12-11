import glob
import os
import cv2

def getLatestScreenShot():
    files = glob.glob(os.path.expanduser('~/Desktop/Screen*.png'))
    files.sort(key=os.path.getmtime)
    files = files[-2:]
    print("\n".join(files))
    if len(files) < 2:
        raise Exception("Unable to find 2 screenshots")
    return files

def validateAndSwapByDimenion(a,b):
    f1 = cv2.imread(a)
    f2 = cv2.imread(b)
    h1, w1, channels = f1.shape
    h2, w2, channels = f2.shape

    if h1 > h2 and w1 > w2:
        return [b, a]
    elif h1 < h2 and w1 < w2:
        return [a, b]
    else:
        raise Exception("Dimensions of one image should be greater than other -- {} x {} and {} x {} ".format(w1,h1,w2,h2))
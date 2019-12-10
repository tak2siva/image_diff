import cv2
import numpy as np
from matplotlib import pyplot as plt

actual = 't_large.png'
template = 't_small.png'

actual = 'template/full_check.png'
template = 'template/check_template.png'

origImg = cv2.imread(actual)
img_rgb = cv2.imread(actual)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread(template,0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

# threshold = 0.8
# loc = np.where( res >= threshold)
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

# cv2.imshow('res2',img_rgb)
# cv2.waitKey(0)


min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = min_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
res2 = origImg[top_left[1]:top_left[1]+h,top_left[1]:bottom_right[1]+w]
cv2.imshow('res2',res2)
cv2.waitKey(0)
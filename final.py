import template_match
import image_diff
import latestScreenshot
import cv2

actual = 'template/full_check.png'
template = 'template/check_template.png'

actual, template = latestScreenshot.getLatestScreenShot()

RESIZE_RESULT = True

template, actual = latestScreenshot.validateAndSwapByDimenion(template, actual)
exepected1, actual1 = template_match.templateMatch(template, actual)

height, width, channels = exepected1.shape
print('expected dimension: ', width, height)
height, width, channels = actual1.shape
print('actual dimension: ', width, height)

# cv2.imshow('template', exepected1)
# cv2.imshow('actual', actual1)
# cv2.waitKey(0)


r1, r2 = image_diff.imageDiff(exepected1, actual1)

if RESIZE_RESULT:
    cv2.imshow('expected', cv2.resize(r1, (960, 540)))
    cv2.imshow('actual', cv2.resize(r2, (960, 540)))
else:
    cv2.imshow('expected', r1)
    cv2.imshow('actual', r1)

cv2.waitKey(0)
cv2.destroyAllWindows()
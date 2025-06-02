import cv2
import numpy as np

def apply(img, low_thresh, high_thresh):
    sharpen_kernel = np.array([[ 0, -1, 0],
                               [-1, 5, -1],
                               [ 0, -1, 0]])
    sharpened = cv2.filter2D(img, -1, sharpen_kernel)
    gray = cv2.cvtColor(sharpened, cv2.COLOR_BGR2GRAY)
    _, thresh_img = cv2.threshold(gray, low_thresh, high_thresh, cv2.THRESH_BINARY)
    return thresh_img

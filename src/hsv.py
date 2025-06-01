import cv2
import numpy as np

def apply(img, low_thresh, high_thresh):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    _, thresh_v = cv2.threshold(v, low_thresh, high_thresh, cv2.THRESH_BINARY)
    hsv_thresh = cv2.merge([h, s, thresh_v])
    return hsv_thresh
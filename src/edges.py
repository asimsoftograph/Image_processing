import cv2

def apply(img, low_thresh, high_thresh):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, low_thresh, high_thresh)
    return edges
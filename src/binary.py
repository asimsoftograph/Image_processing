import cv2

def apply(img, low_thresh, high_thresh):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, low_thresh, high_thresh, cv2.THRESH_BINARY)
    return binary
import cv2

def apply(img, low_thresh, high_thresh):
    blurred = cv2.GaussianBlur(img, (11, 11), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    _, thresh_blur = cv2.threshold(gray, low_thresh, high_thresh, cv2.THRESH_BINARY)
    return thresh_blur
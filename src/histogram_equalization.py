import cv2

def apply(img, low_thresh, high_thresh):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)
    # Apply thresholding after equalization
    _, thresh_img = cv2.threshold(equalized, low_thresh, high_thresh, cv2.THRESH_BINARY)
    return thresh_img
import cv2
import numpy as np

def apply(img, low_thresh, high_thresh):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Sobel edge detection in X and Y directions
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobelx, sobely)
    sobel = np.uint8(np.clip(sobel, 0, 255))
    # Apply thresholding to highlight strong edges
    _, thresh_img = cv2.threshold(sobel, low_thresh, high_thresh, cv2.THRESH_BINARY)
    return thresh_img
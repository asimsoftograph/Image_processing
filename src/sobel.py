import cv2
import numpy as np

def apply(img, low_thresh, high_thresh, kernel_size=3):
    kernel_size = max(3, kernel_size | 1)  # Ensure kernel size is odd and >= 3
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=kernel_size)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=kernel_size)
    sobel = cv2.magnitude(sobelx, sobely)
    sobel = np.uint8(np.clip(sobel, 0, 255))
    _, thresh_img = cv2.threshold(sobel, low_thresh, high_thresh, cv2.THRESH_BINARY)
    return thresh_img
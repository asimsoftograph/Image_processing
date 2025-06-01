#Erosion, dilation, opening, closing, etc. Useful for cleaning up binary images.
import cv2
import numpy as np

def apply(img, low_thresh, high_thresh):
    # Convert to grayscale and threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, low_thresh, high_thresh, cv2.THRESH_BINARY)
    # Create a kernel, size based on low_thresh (must be odd and >= 3)
    ksize = max(3, low_thresh | 1)
    kernel = np.ones((ksize, ksize), np.uint8)
    # Apply morphological opening then closing
    opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
    return closed
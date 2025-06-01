import cv2
import numpy as np

def apply(img, low_thresh, high_thresh):
    noise_img = img.copy()
    row, col, ch = noise_img.shape
    gauss = np.random.normal(0, 25, (row, col, ch)).astype('uint8')
    noisy = cv2.add(noise_img, gauss)
    gray = cv2.cvtColor(noisy, cv2.COLOR_BGR2GRAY)
    _, thresh_img = cv2.threshold(gray, low_thresh, high_thresh, cv2.THRESH_BINARY)
    return thresh_img
#Good for removing salt-and-pepper noise.
import cv2

def apply(img, low_thresh, high_thresh):
    # Use an odd kernel size, map low_thresh to kernel size (must be odd and >= 3)
    ksize = max(3, low_thresh | 1)  # Ensure odd and at least 3
    median = cv2.medianBlur(img, ksize)
    gray = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
    _, thresh_img = cv2.threshold(gray, low_thresh, high_thresh, cv2.THRESH_BINARY)
    return thresh_img
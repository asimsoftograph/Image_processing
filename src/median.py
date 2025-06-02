#Good for removing salt-and-pepper noise.
import cv2

def apply(img, low_thresh, high_thresh, kernel_size=3):
    kernel_size = max(3, kernel_size | 1)  # Ensure kernel size is odd and >= 3
    median = cv2.medianBlur(img, kernel_size)
    gray = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
    _, thresh_img = cv2.threshold(gray, low_thresh, high_thresh, cv2.THRESH_BINARY)
    return thresh_img
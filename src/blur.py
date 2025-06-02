import cv2

def apply(img, low_thresh, high_thresh, kernel_size=3):
    kernel_size = max(3, kernel_size | 1)  # Ensure kernel size is odd and >= 3
    blurred = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    _, thresh_img = cv2.threshold(gray, low_thresh, high_thresh, cv2.THRESH_BINARY)
    return thresh_img

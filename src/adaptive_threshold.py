import cv2

def apply(img, low_thresh, high_thresh):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Block size must be odd and >= 3
    block_size = max(3, low_thresh | 1)
    # C can be positive or negative, here mapped from high_thresh (-20 to 20)
    C = int((high_thresh / 255) * 40 - 20)
    adaptive = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, block_size, C
    )
    return adaptive
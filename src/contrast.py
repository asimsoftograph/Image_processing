import cv2

def apply(img, low_thresh, high_thresh):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Map low_thresh (0-255) to beta (-100 to 100)
    beta = int((low_thresh / 255) * 200 - 100)
    # Map high_thresh (0-255) to alpha (1.0 to 3.0)
    alpha = 1.0 + (high_thresh / 255) * 2.0
    enhanced = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)
    _, binary = cv2.threshold(enhanced, low_thresh, high_thresh, cv2.THRESH_BINARY)
    return binary


# This function applies contrast enhancement to the input image and then thresholds it.
# The low_thresh and high_thresh parameters control the contrast enhancement and thresholding.  
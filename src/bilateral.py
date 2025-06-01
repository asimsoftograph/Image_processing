import cv2

def apply(img, low_thresh, high_thresh):
    # d: Diameter of each pixel neighborhood.
    # sigmaColor: Filter sigma in the color space.
    # sigmaSpace: Filter sigma in the coordinate space.
    # We'll map the sliders to sigmaColor and sigmaSpace for user control.
    d = 9
    sigmaColor = max(1, high_thresh)
    sigmaSpace = max(1, low_thresh)
    bilateral = cv2.bilateralFilter(img, d, sigmaColor, sigmaSpace)
    gray = cv2.cvtColor(bilateral, cv2.COLOR_BGR2GRAY)
    _, thresh_img = cv2.threshold(gray, low_thresh, high_thresh, cv2.THRESH_BINARY)
    return thresh_img
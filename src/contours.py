import cv2

def apply(img, low_thresh, high_thresh):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, low_thresh, high_thresh, cv2.THRESH_BINARY)
    contours_img = img.copy()
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(contours_img, contours, -1, (0, 255, 0), 2)
    return contours_img
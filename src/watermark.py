import cv2

def apply(img, low_thresh, high_thresh):
    watermarked = img.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(watermarked, "Watermark", (10, 30), font, 1, (255, 255, 255), 2)
    gray = cv2.cvtColor(watermarked, cv2.COLOR_BGR2GRAY)
    _, thresh_img = cv2.threshold(gray, low_thresh, high_thresh, cv2.THRESH_BINARY)
    return thresh_img
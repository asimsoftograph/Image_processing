import cv2

def apply(img, low_thresh, high_thresh):
    yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    y_channel = yuv[:, :, 0]
    _, thresh_y = cv2.threshold(y_channel, low_thresh, high_thresh, cv2.THRESH_BINARY)
    return thresh_y
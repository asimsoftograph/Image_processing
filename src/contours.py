import cv2
import numpy as np
def apply(img, low_thresh, high_thresh):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, low_thresh, high_thresh, cv2.THRESH_BINARY)
    # Apply morphological operations to clean up the binary image
    kernel = np.ones((3, 3), np.uint8)
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=1)
    binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)
    contours_img = img.copy()
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(contours_img, contours, -1, (0, 255, 0), 2)
    return contours_img









# def apply(img, low_thresh, high_thresh):
    
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Apply Gaussian blur to reduce noise

#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
#     # # Use adaptive thresholding for better handling of varying lighting
#     # binary = cv2.adaptiveThreshold(
#     #     blurred, 
#     #     255, 
#     #     cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
#     #     cv2.THRESH_BINARY_INV, 
#     #     11, 
#     #     2
#     # )
#     # Apply fixed thresholding with user-defined low_thresh and high_thresh
#     _, binary = cv2.threshold(blurred, low_thresh, high_thresh, cv2.THRESH_BINARY)

#     # Apply morphological operations to clean up the binary image
#     kernel = np.ones((3, 3), np.uint8)
#     binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=1)
#     binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)
    
#     # Find contours
#     contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     # Filter contours based on area to remove small noise
#     min_area = 100  # Adjust this threshold based on your needs
#     filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]
    
#     # Draw contours on a copy of the original image
#     contours_img = img.copy()
#     cv2.drawContours(contours_img, filtered_contours, -1, (0, 255, 0), 2)
    
#     return contours_img

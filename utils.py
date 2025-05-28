import cv2
import os
import numpy as np
import random

def process_image(path,threshold_value=127):
    if not os.path.exists("processed"):
        os.makedirs("processed")

    img = cv2.imread(path)
    outputs = []

    # Original
    original_path = os.path.join("processed", "original.jpg")
    cv2.imwrite(original_path, img)
    outputs.append(original_path)

    # Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_path = os.path.join("processed", "gray.jpg")
    cv2.imwrite(gray_path, gray)
    outputs.append(gray_path)
    # Thresholding based on the provided threshold value
    _, gray = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
    # Binary
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    binary_path = os.path.join("processed", "binary.jpg")
    cv2.imwrite(binary_path, binary)
    outputs.append(binary_path)

    # HSB
    hsb = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsb_path = os.path.join("processed", "hsb.jpg")
    cv2.imwrite(hsb_path, hsb)
    outputs.append(hsb_path)

    # Luminance (Y channel of YUV)
    yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    y_channel = yuv[:, :, 0]
    luminance_path = os.path.join("processed", "luminance.jpg")
    cv2.imwrite(luminance_path, y_channel)
    outputs.append(luminance_path)

    # Blur
    blurred = cv2.GaussianBlur(img, (11, 11), 0)
    blur_path = os.path.join("processed", "blur.jpg")
    cv2.imwrite(blur_path, blurred)
    outputs.append(blur_path)

    # Edge Detection
    edges = cv2.Canny(gray, 100, 200)
    edges_path = os.path.join("processed", "edges.jpg")
    cv2.imwrite(edges_path, edges)
    outputs.append(edges_path)

    # Contours
    contours_img = img.copy()
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(contours_img, contours, -1, (0, 255, 0), 2)
    contours_path = os.path.join("processed", "contours.jpg")
    cv2.imwrite(contours_path, contours_img)
    outputs.append(contours_path)

    # Add Gaussian Noise
    noise_img = img.copy()
    row, col, ch = noise_img.shape
    gauss = np.random.normal(0, 25, (row, col, ch)).astype('uint8')
    noisy = cv2.add(noise_img, gauss)
    noise_path = os.path.join("processed", "noisy.jpg")
    cv2.imwrite(noise_path, noisy)
    outputs.append(noise_path)

    # Watermark
    watermarked = img.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(watermarked, "Watermark", (10, 30), font, 1, (255, 255, 255), 2)
    watermarked_path = os.path.join("processed", "watermarked.jpg")
    cv2.imwrite(watermarked_path, watermarked)
    outputs.append(watermarked_path)
    
    
    #Embosses the image in a 3D space
    emboss_kernel = np.array([[ -2, -1, 0],
                          [ -1, 1, 1],
                          [  0, 1, 2]])
    embossed = cv2.filter2D(img, -1, emboss_kernel)
    embossed_path = os.path.join("processed", "embossed.jpg")
    cv2.imwrite(embossed_path, embossed)
    outputs.append(embossed_path)

    #Sharpening the image
    sharpen_kernel = np.array([[ 0, -1, 0],
                                [-1, 5, -1],
                                [ 0, -1, 0]])
    sharpened = cv2.filter2D(img, -1, sharpen_kernel)
    sharpened_path = os.path.join("processed", "sharpened.jpg")
    cv2.imwrite(sharpened_path, sharpened)
    outputs.append(sharpened_path)

    # Randomly rotate the image
    angle = random.randint(-30, 30)
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h))
    rotated_path = os.path.join("processed", "rotated.jpg")
    cv2.imwrite(rotated_path, rotated)
    outputs.append(rotated_path)


    # cartoon effect
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255,
                              cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(img, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cartoon_path = os.path.join("processed", "cartoon.jpg")
    cv2.imwrite(cartoon_path, cartoon)
    outputs.append(cartoon_path)

    # Sepia effect
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepia = cv2.transform(img, sepia_filter)
    sepia = np.clip(sepia, 0, 255).astype(np.uint8)
    sepia_path = os.path.join("processed", "sepia.jpg")
    cv2.imwrite(sepia_path, sepia)
    outputs.append(sepia_path)


    return outputs

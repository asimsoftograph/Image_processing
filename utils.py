import cv2
import os
import numpy as np
import random

def process_image(path):
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

    return outputs

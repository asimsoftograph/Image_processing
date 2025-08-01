import cv2
import os
import numpy as np

from src import grayscale, hsv, edges, binary, luminance, blur, contours, watermark, noise, sharpen, original,contrast,adaptive_threshold,bilateral, median,sobel,histogram_equalization

def process_image(path, mode="gray", threshold_value=127, low_thresh=100, high_thresh=200, kernel_size=3):
    if not os.path.exists("processed"):
        os.makedirs("processed")

    img = cv2.imread(path)
    out_path = os.path.join("processed", f"{mode}.jpg")

    filter_map = {
        "gray": grayscale.apply,
        "hsv": hsv.apply,
        "edges": edges.apply,
        "binary": binary.apply,
        "luminance": luminance.apply,
        "blur": blur.apply,
        "contours": contours.apply,
        "watermark": watermark.apply,
        "noise": noise.apply,
        "sharpen": sharpen.apply,
        "original": original.apply,
        "contrast": contrast.apply,
        "adaptive_threshold": adaptive_threshold.apply,
        "bilateral": bilateral.apply,
        "median": median.apply,
        "sobel": sobel.apply,
        "histogram_equalization": histogram_equalization.apply
      
    }

    if mode in filter_map:
        # Pass kernel_size to filters that need it
        if mode in ["blur", "median", "sobel"]:
            result = filter_map[mode](img, low_thresh, high_thresh, kernel_size=kernel_size)
        else:
            result = filter_map[mode](img, low_thresh, high_thresh)
        cv2.imwrite(out_path, result)
    else:
        cv2.imwrite(out_path, img)

    return out_path
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from utils import process_image

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing Playground")
        self.low_thresh = 100
        self.high_thresh = 200
        self.threshold_val = 127
        self.current_file_path = None
        self.current_mode = "gray"

        # Upload button
        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=5)

        # Processing buttons in a horizontal frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        # Filter buttons
        filters = [
            ("Grayscale", "gray"),
            ("HSV", "hsv"),
            ("Edges", "edges"),
            ("Binary", "binary"),
            ("Luminance", "luminance"),
            ("Blur", "blur"),
            ("Contours", "contours"),
            ("Original", "original"),
            ("Watermark", "watermark"),
            ("Noise", "noise"),
            ("Sharpen", "sharpen"),
            ("Contrast", "contrast"),
            ("Adaptive Threshold", "adaptive_threshold"),
            ("Bilateral Filter", "bilateral"),
            ("Median Filter", "median"),
            ("Sobel Filter", "sobel"),
            ("Morphological Operations", "morphological"),
            ("Histogram Equalization", "histogram_equalization")
        ]
        for text, mode in filters:
            btn = tk.Button(self.button_frame, text=text, command=lambda m=mode: self.set_mode(m))
            btn.pack(side="left", padx=2)

        # Threshold sliders
        self.low_slider = tk.Scale(root, from_=0, to=255, orient="horizontal",
                                   label="Low Threshold", command=self.slider_changed)
        self.low_slider.set(self.low_thresh)
        self.low_slider.pack()
        self.high_slider = tk.Scale(root, from_=0, to=255, orient="horizontal",
                                    label="High Threshold", command=self.slider_changed)
        self.high_slider.set(self.high_thresh)
        self.high_slider.pack()

        # Image display
        self.img_label = tk.Label(root)
        self.img_label.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.current_file_path = file_path
            self.update_image()

    def set_mode(self, mode):
        self.current_mode = mode
        self.update_image()

    def slider_changed(self, _=None):
        self.low_thresh = self.low_slider.get()
        self.high_thresh = self.high_slider.get()
        self.update_image()

    def update_image(self):
        if not self.current_file_path:
            return
        out_path = process_image(
            self.current_file_path,
            mode=self.current_mode,
            threshold_value=self.threshold_val,
            low_thresh=self.low_thresh,
            high_thresh=self.high_thresh
        )
        img = Image.open(out_path)
        img = img.resize((300, 300))
        tk_img = ImageTk.PhotoImage(img)
        self.img_label.configure(image=tk_img)
        self.img_label.image = tk_img

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()

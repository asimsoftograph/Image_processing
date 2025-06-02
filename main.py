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
        self.kernel_size = 3  # Default kernel size
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

        # Kernel size slider (initially hidden)
        self.kernel_slider = tk.Scale(root, from_=3, to=31, orient="horizontal",
                                      label="Kernel Size (odd)", command=self.slider_changed)
        self.kernel_slider.set(self.kernel_size)
        self.kernel_slider.pack_forget()  # Hide by default

        # Image display frames
        self.image_frame = tk.Frame(root)
        self.image_frame.pack(pady=10)

        # Left: Original image
        self.original_label = tk.Label(self.image_frame, text="Original Image")
        self.original_label.grid(row=0, column=0, padx=10)
        self.original_img_label = tk.Label(self.image_frame)
        self.original_img_label.grid(row=1, column=0, padx=10)

        # Right: Processed image
        self.processed_label = tk.Label(self.image_frame, text="Preprocessed Image")
        self.processed_label.grid(row=0, column=1, padx=10)
        self.processed_img_label = tk.Label(self.image_frame)
        self.processed_img_label.grid(row=1, column=1, padx=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.current_file_path = file_path
            self.current_mode = "original"  
            self.show_original_image()
            self.update_image()

    def show_original_image(self):
        if not self.current_file_path:
            return
        img = Image.open(self.current_file_path)
        img = img.resize((300, 300))
        tk_img = ImageTk.PhotoImage(img)
        self.original_img_label.configure(image=tk_img)
        self.original_img_label.image = tk_img

    def set_mode(self, mode):
        self.current_mode = mode
        # Show kernel slider for filters that need it
        if mode in ["sobel", "median", "blur", "morphological"]:
            self.kernel_slider.pack()  # Show kernel slider
        else:
            self.kernel_slider.pack_forget()  # Hide kernel slider
        self.update_image()

    def slider_changed(self, _=None):
        self.low_thresh = self.low_slider.get()
        self.high_thresh = self.high_slider.get()
        self.kernel_size = self.kernel_slider.get()
        self.update_image()

    def update_image(self):
        if not self.current_file_path:
            return
        out_path = process_image(
            self.current_file_path,
            mode=self.current_mode,
            threshold_value=self.threshold_val,
            low_thresh=self.low_thresh,
            high_thresh=self.high_thresh,
            kernel_size=self.kernel_size  # Pass kernel size
        )
        img = Image.open(out_path)
        img = img.resize((300, 300))
        tk_img = ImageTk.PhotoImage(img)
        self.processed_img_label.configure(image=tk_img)
        self.processed_img_label.image = tk_img

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()
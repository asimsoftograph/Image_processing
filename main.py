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

        self.gray_btn = tk.Button(self.button_frame, text="Grayscale", command=lambda: self.set_mode("gray"))
        self.gray_btn.pack(side="left", padx=2)
        self.hsv_btn = tk.Button(self.button_frame, text="HSV", command=lambda: self.set_mode("hsv"))
        self.hsv_btn.pack(side="left", padx=2)
        self.edges_btn = tk.Button(self.button_frame, text="Edges", command=lambda: self.set_mode("edges"))
        self.edges_btn.pack(side="left", padx=2)
        self.binary_btn = tk.Button(self.button_frame, text="Binary", command=lambda: self.set_mode("binary"))
        self.binary_btn.pack(side="left", padx=2)
        self.luminance_btn = tk.Button(self.button_frame, text="Luminance", command=lambda: self.set_mode("luminance"))
        self.luminance_btn.pack(side="left", padx=2)
        self.blur_btn = tk.Button(self.button_frame, text="Blur", command=lambda: self.set_mode("blur"))
        self.blur_btn.pack(side="left", padx=2)
        self.contours_btn = tk.Button(self.button_frame, text="Contours", command=lambda: self.set_mode("contours"))
        self.contours_btn.pack(side="left", padx=2)
        self.original_btn = tk.Button(self.button_frame, text="Original", command=lambda: self.set_mode("original"))
        self.original_btn.pack(side="left", padx=2)
        self.binary_threshold_btn = tk.Button(self.button_frame, text="Binary Threshold",
                                              command=lambda: self.set_mode("binary_threshold"))
        self.binary_threshold_btn.pack(side="left", padx=2)
        self.watermark_btn = tk.Button(self.button_frame, text="Watermark", command=lambda: self.set_mode("watermark"))
        self.watermark_btn.pack(side="left", padx=2)
        self.noise_btn = tk.Button(self.button_frame, text="Noise", command=lambda: self.set_mode("noise"))
        self.noise_btn.pack(side="left", padx=2)
        self.sharpness_btn = tk.Button(self.button_frame, text="Sharpen", command=lambda: self.set_mode("sharpen"))
        self.sharpness_btn.pack(side="left", padx=2)

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

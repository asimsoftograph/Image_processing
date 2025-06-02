# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk
# from utils import process_image


# class ImageProcessingApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Image Processing Playground")
#         self.low_thresh = 100
#         self.high_thresh = 200
#         self.threshold_val = 127
#         self.current_file_path = None
#         self.current_mode = "gray"

#         # Upload button
#         self.upload_btn = tk.Button(
#             root, text="Upload Image", command=self.upload_image)
#         self.upload_btn.pack(pady=5)

#         # Processing buttons in a horizontal frame
#         self.button_frame = tk.Frame(root)
#         self.button_frame.pack(pady=5)

#         # Filter buttons
#         filters = [
#             ("Grayscale", "gray"),
#             ("HSV", "hsv"),
#             ("Edges", "edges"),
#             ("Binary", "binary"),
#             ("Luminance", "luminance"),
#             ("Blur", "blur"),
#             ("Contours", "contours"),
#             ("Original", "original"),
#             ("Watermark", "watermark"),
#             ("Noise", "noise"),
#             ("Sharpen", "sharpen"),
#             ("Contrast", "contrast"),
#             ("Adaptive Threshold", "adaptive_threshold"),
#             ("Bilateral Filter", "bilateral"),
#             ("Median Filter", "median"),
#             ("Sobel Filter", "sobel"),
#             ("Morphological Operations", "morphological"),
#             ("Histogram Equalization", "histogram_equalization")

#         ]
#         for text, mode in filters:
#             btn = tk.Button(
#                 self.button_frame,
#                 text=text,
#                 command=lambda m=mode: self.set_mode(m))
#             btn.pack(side="left", padx=2)

#         # Threshold sliders
#         self.low_slider = tk.Scale(
#             root,
#             from_=0,
#             to=255,
#             orient="horizontal",
#             label="Low Threshold",
#             command=self.slider_changed)
#         self.low_slider.set(self.low_thresh)
#         self.low_slider.pack()
#         self.high_slider = tk.Scale(
#             root,
#             from_=0,
#             to=255,
#             orient="horizontal",
#             label="High Threshold",
#             command=self.slider_changed)
#         self.high_slider.set(self.high_thresh)
#         self.high_slider.pack()

#         # Adaptive Threshold parameters
#         self.block_size = 3
#         self.block_size_slider = tk.Scale(
#             root,
#             from_=3,
#             to=255,
#             orient="horizontal",
#             label="Block Size",
#             command=self.slider_changed)
#         self.block_size_slider.set(self.block_size)
#         self.block_size_slider.pack()

#         self.C = 5
#         self.c_slider = tk.Scale(root, from_=-20, to=20, orient="horizontal",
#                                  label="C", command=self.slider_changed)
#         self.c_slider.set(self.C)
#         self.c_slider.pack()

#         # Sharpen level slider
#         self.sharpen_level = 5
#         self.sharpen_slider = tk.Scale(
#             root,
#             from_=1,
#             to=15,
#             orient="horizontal",
#             label="Sharpen Level",
#             command=self.slider_changed)
#         self.sharpen_slider.set(self.sharpen_level)
#         self.sharpen_slider.pack()

#         # Kernel size slider
#         self.kernel_size = 3
#         self.kernel_slider = tk.Scale(
#             root,
#             from_=1,
#             to=15,
#             orient="horizontal",
#             label="Kernel Size",
#             command=self.slider_changed)
#         self.kernel_slider.set(self.kernel_size)
#         self.kernel_slider.pack()

#         # Morphology operation dropdown
#         self.morph_operation = tk.StringVar(root)
#         self.morph_operation.set("erode")  # default value
#         morph_operations = ["erode", "dilate", "open", "close"]
#         self.morph_dropdown = tk.OptionMenu(
#             root, self.morph_operation, *morph_operations)
#         self.morph_dropdown.pack()

#         # Image display
#         self.img_label = tk.Label(root)
#         self.img_label.pack(pady=10)

#     def upload_image(self):
#         file_path = filedialog.askopenfilename()
#         if file_path:
#             self.current_file_path = file_path
#             self.update_image()

#     def set_mode(self, mode):
#         self.current_mode = mode
#         self.update_image()

#     def slider_changed(self, _=None):
#         self.low_thresh = self.low_slider.get()
#         self.high_thresh = self.high_slider.get()
#         self.kernel_size = self.kernel_slider.get()
#         self.block_size = self.block_size_slider.get()
#         self.C = self.c_slider.get()
#         self.sharpen_level = self.sharpen_slider.get()
#         self.update_image()

#     def update_image(self):
#         if not self.current_file_path:
#             return
#         # out_path = process_image(
#         processed_img = process_image(
#             self.current_file_path,
#             mode=self.current_mode,
#             low_thresh=self.low_thresh,
#             high_thresh=self.high_thresh,
#             block_size=self.block_size,
#             C=self.C,
#             kernel_size=self.kernel_size,
#             sharpen_level=self.sharpen_level
#         )
#         # img = Image.open(out_path)
#         img = Image.fromarray(processed_img)
#         img = img.resize((300, 300))
#         tk_img = ImageTk.PhotoImage(img)
#         self.img_label.configure(image=tk_img)
#         self.img_label.image = tk_img


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ImageProcessingApp(root)
#     root.mainloop()




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
        self.processed_img_label.configure(image=tk_img)
        self.processed_img_label.image = tk_img

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()
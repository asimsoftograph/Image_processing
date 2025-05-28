# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk
# import cv2
# import os
# from utils import process_image

# class ImageProcessingApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Image Processing Playground")

#         self.panel = tk.Label(root)
#         self.panel.pack()

#         btn = tk.Button(root, text="Upload Image", command=self.upload_image)
#         btn.pack()

#         self.processed_images = []
#         self.index = 0

#         self.next_btn = tk.Button(root, text="Next", command=self.show_next_image)
#         self.next_btn.pack()
#         self.next_btn.config(state=tk.DISABLED)

#     def upload_image(self):
#         file_path = filedialog.askopenfilename()
#         if file_path:
#             self.processed_images = process_image(file_path)
#             self.index = 0
#             self.show_image(self.processed_images[self.index])
#             self.next_btn.config(state=tk.NORMAL)

#     def show_image(self, image_path):
#         img = Image.open(image_path)
#         img = img.resize((400, 400))
#         img = ImageTk.PhotoImage(img)
#         self.panel.config(image=img)
#         self.panel.image = img

#     def show_next_image(self):
#         self.index += 1
#         if self.index < len(self.processed_images):
#             self.show_image(self.processed_images[self.index])
#         else:
#             self.index = 0
#             self.show_image(self.processed_images[self.index])

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ImageProcessingApp(root)
#     root.mainloop()



import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from utils import process_image
import os

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing Playground")
        self.threshold_val = 127

        # Upload button
        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=5)

        # Threshold slider
        self.slider = tk.Scale(root, from_=0, to=255, orient="horizontal",
                               label="Threshold Value", command=self.slider_changed)
        self.slider.set(self.threshold_val)
        self.slider.pack(pady=5)

        # Scrollable frame for showing all images
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.image_paths = []
        self.img_widgets = []
        self.current_file_path = None

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.current_file_path = file_path
            self.update_images()

    def slider_changed(self, value):
        self.threshold_val = int(value)
        if self.current_file_path:
            self.update_images()

    def update_images(self):
        # Clear previous widgets
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.image_paths = process_image(self.current_file_path, self.threshold_val)
        self.img_widgets = []

        #image captions 
        captions = [
            "Original", "Grayscale", "Binary", "HSB",
            "Luminance", "Blur", "Edges", "Contours","rotated","noise","Watermark","embossed","sharpened","cartoon"
        ]

        # for i, path in enumerate(self.image_paths):
        #     img = Image.open(path)
        #     img = img.resize((300, 300))
        #     tk_img = ImageTk.PhotoImage(img)
        #     label = tk.Label(self.scrollable_frame, image=tk_img)
        #     label.image = tk_img  # Keep reference
        #     label.grid(row=i//2, column=i % 2, padx=10, pady=10)
        for i, (path, caption) in enumerate(zip(self.image_paths, captions)):
            img = Image.open(path)
            img = img.resize((300, 300))
            tk_img = ImageTk.PhotoImage(img)

            label = tk.Label(self.scrollable_frame, image=tk_img)
            label.image = tk_img
            label.grid(row=i, column=0, padx=10, pady=10)
            caption_label = tk.Label(self.scrollable_frame, text=caption)
            caption_label.grid(row=i, column=1, padx=10, pady=10)
            self.img_widgets.append((label, caption_label))
      
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()

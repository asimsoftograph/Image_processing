import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import os
from utils import process_image

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing Playground")

        self.panel = tk.Label(root)
        self.panel.pack()

        btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        btn.pack()

        self.processed_images = []
        self.index = 0

        self.next_btn = tk.Button(root, text="Next", command=self.show_next_image)
        self.next_btn.pack()
        self.next_btn.config(state=tk.DISABLED)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.processed_images = process_image(file_path)
            self.index = 0
            self.show_image(self.processed_images[self.index])
            self.next_btn.config(state=tk.NORMAL)

    def show_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((400, 400))
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img

    def show_next_image(self):
        self.index += 1
        if self.index < len(self.processed_images):
            self.show_image(self.processed_images[self.index])
        else:
            self.index = 0
            self.show_image(self.processed_images[self.index])

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()

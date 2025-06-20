import tkinter as tk
from controller import Controller
from PIL import ImageTk

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("\ud83d\udcf8 Aplikasi Pengolahan Citra Digital")
        self.root.configure(bg="#f0f0f0")

        self.controller = Controller(self)

        title = tk.Label(root, text="Aplikasi Pengolahan Citra Digital", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        title.pack(pady=10)

        image_frame = tk.Frame(root, bg="#f0f0f0")
        image_frame.pack(pady=10)

        left_frame = tk.Frame(image_frame, bd=2, relief=tk.GROOVE)
        left_frame.grid(row=0, column=0, padx=15)
        right_frame = tk.Frame(image_frame, bd=2, relief=tk.GROOVE)
        right_frame.grid(row=0, column=1, padx=15)

        tk.Label(left_frame, text="Gambar Asli", font=("Arial", 10, "bold")).pack()
        self.image_label = tk.Label(left_frame)
        self.image_label.pack()

        tk.Label(right_frame, text="Hasil Proses", font=("Arial", 10, "bold")).pack()
        self.processed_label = tk.Label(right_frame)
        self.processed_label.pack()

        btn_frame = tk.Frame(root, bg="#e6e6e6", padx=10, pady=10, bd=1, relief=tk.RIDGE)
        btn_frame.pack(pady=10, fill="x")

        def btn(row, col, label, cmd):
            tk.Button(btn_frame, text=label, width=18, command=cmd).grid(row=row, column=col, padx=5, pady=5)

        btn(0, 0, "Input Gambar", self.controller.load_image)
        btn(0, 1, "Grayscale", self.controller.to_grayscale)
        btn(0, 2, "Biner", self.controller.to_binary)
        btn(0, 3, "Negatif", self.controller.to_negative)

        btn(1, 0, "Penjumlahan +", self.controller.arit_add)
        btn(1, 1, "OR", self.controller.logic_or)
        btn(1, 2, "Histogram Gabungan", self.controller.show_histogram_combined)
        btn(1, 3, "Konvolusi Blur", self.controller.blur)

        btn(2, 0, "Erosi (SE1)", self.controller.erosi_se1)
        btn(2, 1, "Erosi (SE2)", self.controller.erosi_se2)
        btn(2, 2, "Simpan Gambar", self.controller.save_result)

    def show_image(self, image, target):
        image = image.resize((300, 300))
        image_tk = ImageTk.PhotoImage(image)
        target.config(image=image_tk)
        target.image = image_tk
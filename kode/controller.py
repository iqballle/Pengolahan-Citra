from tkinter import filedialog, messagebox  
from PIL import Image
from image_operations import ImageOpsCustom

class Controller:
    def __init__(self, ui):
        self.ui = ui
        self.ops = ImageOpsCustom()
        self.original = None
        self.result = None

    def load_image(self):
        path = filedialog.askopenfilename()
        if path:
            self.original = Image.open(path).convert("RGB")
            self.ui.show_image(self.original, self.ui.image_label)

    def _apply(self, func):
        if self.original:
            self.result = func(self.original)
            self.ui.show_image(self.result, self.ui.processed_label)
            

    def to_grayscale(self): self._apply(self.ops.to_grayscale)
    def to_binary(self): self._apply(self.ops.to_binary)
    def arit_add(self): self._apply(self.ops.arit_add)
    def logic_or(self): self._apply(self.ops.logic_or)

    def blur(self): self._apply(self.ops.blur)
    def erosi_se1(self): self._apply(lambda img: self.ops.erosi(img, se_type="se1"))
    def erosi_se2(self): self._apply(lambda img: self.ops.erosi(img, se_type="se2"))
    def show_histogram_combined(self):
        if self.original:
            self.ops.show_histogram_combined(self.original)
            
    def save_result(self):
        if self.result:
            path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")])
            if path:
                self.result.save(path)
                messagebox.showinfo("Berhasil", "Gambar berhasil disimpan!")
        else:
            messagebox.showwarning("Peringatan", "Belum ada gambar hasil untuk disimpan.")


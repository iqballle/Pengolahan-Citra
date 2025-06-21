from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve, binary_erosion

class ImageOpsCustom:
    def to_grayscale(self, img):
        return ImageOps.grayscale(img)

    def to_binary(self, img):
        gray = ImageOps.grayscale(img)
        return gray.point(lambda x: 255 if x > 128 else 0)

    def arit_add(self, img): return self._apply_arit(img, lambda x: x + 50)

    def _apply_arit(self, img, func):
        arr = np.array(img).astype(np.float32)
        result = np.clip(func(arr), 0, 255)
        return Image.fromarray(result.astype(np.uint8))


    def logic_or(self, img): return self._logic(img, np.bitwise_or)


    def _logic(self, img, op):
        arr = np.array(img)
        masker = np.full(arr.shape, 128, dtype=np.uint8)
        return Image.fromarray(op(arr, masker))

    def blur(self, img):
        arr = np.array(img).astype(np.float32)
        kernel = np.ones((3, 3)) / 9
        for c in range(3):
            arr[:, :, c] = convolve(arr[:, :, c], kernel)
        return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

    def erosi(self, img, se_type="se1"):
        gray = ImageOps.grayscale(img)
        binary = np.array(gray.point(lambda x: 1 if x > 128 else 0, '1')).astype(bool)
        if se_type == "se1":
            se = np.ones((3,3), dtype=bool)
        else:
            se = np.array([[0,1,0],[1,1,1],[0,1,0]], dtype=bool)
        eroded = binary_erosion(binary, structure=se).astype(np.uint8) * 255
        return Image.fromarray(eroded)

    def show_histogram_combined(self, img):
        gray = img.convert('L')
        r, g, b = img.split()

        plt.figure(figsize=(10, 5))


        plt.subplot(1, 2, 1)
        plt.title("Grayscale Histogram")
        plt.plot(gray.histogram(), color='black')


        plt.subplot(1, 2, 2)
        plt.title("RGB Histogram")
        plt.plot(r.histogram(), color='red', label='Red')
        plt.plot(g.histogram(), color='green', label='Green')
        plt.plot(b.histogram(), color='blue', label='Blue')
        plt.legend()

        plt.tight_layout()
        plt.show()



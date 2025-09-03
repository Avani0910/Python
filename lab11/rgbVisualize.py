import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


image_path = r"C:\Users\Avni Kavathiya\Pictures\Avani.jpg"
image = Image.open(image_path)
image_np = np.array(image)


R = image_np[:, :, 0]
G = image_np[:, :, 1]
B = image_np[:, :, 2]


zeros = np.zeros_like(R)
red_img   = np.stack([R, zeros, zeros], axis=2)
green_img = np.stack([zeros, G, zeros], axis=2)
blue_img  = np.stack([zeros, zeros, B], axis=2)


plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(image_np)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(red_img)
plt.title("Red Channel")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(green_img)
plt.title("Green Channel")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(blue_img)
plt.title("Blue Channel")
plt.axis("off")

plt.tight_layout()
plt.show()

from PIL import Image
import numpy as np

image_path =r"C:\Users\Avni Kavathiya\Pictures\Avani.jpg"
img = Image.open(image_path)

img_array = np.array(img)

height, width = img_array.shape[:2]
print("Dimensions (Height x Width):", (height, width))

print("Shape of image:", img_array.shape)

min_blue_value = np.min(img_array[:, :, 2])
print("Minimum pixel value in Blue channel:", min_blue_value)

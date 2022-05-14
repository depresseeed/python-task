import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from tqdm import tqdm
img = Image.open('InputFile.png')
arr = np.asarray(img, dtype='uint8')

mean = arr.mean()
print("Enter factor")

k = float(input())/100 + 1 
img = np.copy(arr.reshape(-1))
img2 = np.copy(arr.reshape(-1))


for i, value in tqdm(enumerate(img)):
    delta = value - mean
    img[i] = max(0, min(255, mean + k * delta))
    img2[i] = min(255, k * value)

img = img.reshape(arr.shape)
img1 = img2.reshape(arr.shape)
im = Image.fromarray(img)
im.save("Outfile1.png")
im = Image.fromarray(img1)
im.save("Outfile2.png")

import numpy as np
from PIL import Image

##### Изменение цвета изображения #####
img = np.array(Image.open('image.jpg'))
imgR = img.copy()
imgR[:, :, (1, 2)] = 0

imgR2 = Image.fromarray(imgR)

result1 = Image.new("RGB", (img.shape[1], img.shape[0]))
result1.paste(imgR2, (0, 0))

result1.save("result1.png", format="PNG")


##### Создание фотоколлажа #####

# преобразование в черно-белое изображение
imgGray = np.mean(img, axis = 2).astype(np.uint8)

# преобразование цветных каналов
imgG = img.copy()
imgG[:, :, (0, 2)] = 0
imgB = img.copy()
imgB[:, :, (0, 1)] = 0

# объединение изображений
img1 = Image.fromarray(imgGray)
img2 = Image.fromarray(imgR)
img3 = Image.fromarray(imgG)
img4 = Image.fromarray(imgB)

result2 = Image.new("RGB", (img.shape[1] * 2, img.shape[0] * 2))
result2.paste(img1, (0, 0))
result2.paste(img2, (img.shape[1], 0))
result2.paste(img3, (0, img.shape[0]))
result2.paste(img4, (img.shape[1], img.shape[0]))

result2.save("result2.png", format="PNG")




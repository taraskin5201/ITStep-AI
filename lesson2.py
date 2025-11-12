# # # зображення у opencv
# import cv2
#
# # читання злображення
# img = cv2.imread(
#     'data/lesson1/cameraman.png',  # шлях до файлу
#     cv2.IMREAD_GRAYSCALE # формат зображення
# )
#
#
# print(type(img))
# print(img)
# print(img.shape)
# print(img.dtype)
#
# # показати зображення
# cv2.imshow(
#     'image',   # назву
#     img
# )
#
# cv2.waitKey(0)


# Завдання 2
# Відкрийте зображення data/Lenna.png. Виведіть на екран
# такі зображень:
#  Верхній лівий кут розміром 100х50
#  Центральний квадрат розміром 100х100
#  Верхню половину
#  Нижню половину
#  Ліву половину
#  Праву половину


import cv2
import numpy as np
# Практичне завдання 1
# Відкрийте зображення data/Lenna.png. Виведіть на екран розмір зображення, тип даних,
# максимальну та мінімальну інтенсивність пікселів,
# саме зображення з підписом.
img = cv2.imread(
     'data/lesson1/Lenna.png',
     cv2.IMREAD_GRAYSCALE
)


new_img = cv2.resize(img, (500, 500))

print(type(new_img))
print(new_img)
print(new_img.shape)
print(new_img.dtype)

num_max = np.max(new_img)
num_min = np.min(new_img)

print(num_min)
print(num_max)

# Відкрийте зображення data/Lenna.png. Виведіть на екран такі зображень:
# Верхній лівий кут розміром 300х150

cut_img = new_img[0:300, 0:150]
# cv2.imshow('left apper', cut_img)
#
# # Центральний квадрат розміром 200х200
# center = new_img[150:350, 150:350]
# cv2.imshow('center', center)
#
# # Верхню половину
# half_up = new_img[0:250, :]
# cv2.imshow('half up', half_up)
#
#
# cv2.imshow('new', new_img)

# # Нижню половину
# half_down = new_img[250:, :]
# cv2.imshow('half down', half_down)
#
# # Ліву половину
# half_left = new_img[:, 0:250]
# cv2.imshow('half left', half_left)


# # Праву половину
# half_right = new_img[:, 250:]
# cv2.imshow('half right', half_right)



# Завдання 3
# Відкрийте зображення data/Lenna.png. Створіть наступні
# зображення

# super_new_img = new_img.copy()
# super_new_img[:30, :] = 0
# super_new_img[-30:, :] = 255

# super_new_img = new_img.copy()
# super_new_img[:, :50] = 0
# super_new_img[:, -50:] = 0
#
# cv2.imshow('new', new_img)
# print(super_new_img)
# cv2.imshow('super new', super_new_img)



# Завдання 4
# Відкрийте зображення data/Lenna.png. Створіть маску для
# пік селів з інтенсивністю більше 128 та виведіть її. Також
# виведіть заперечення цієї маски.
# На оригінальному зображенні, усі пікселі які не
# відповідають масці замініть на 0 та виведіть результат

mask = new_img > 128
print(mask)
print(mask.shape)
print(mask.dtype)

cv2.imshow('img', new_img)

new_img[~mask] = 0
cv2.imshow('new', new_img)

new_img[mask] = 255
cv2.imshow('new', new_img)



cv2.waitKey(0)
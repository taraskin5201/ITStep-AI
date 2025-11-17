# # дз
# result1 = img.copy()
# result1[:] = 0
#
# # те саме(створити масив 0 такого ж розміру як img)
# result1 = np.zero_like(img)
#
# # проблема зі знаками \
# r"C:\ITSTEP\ITStep-AI\data\lesson1\baboo.jpg"


# # колір
# import cv2
#
# # читати як чорно біле
# img = cv2.imread('data/lesson2/lego.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.resize(img, (500, 500))
#
# print(img.shape)
# print(img.dtype)
#
# cv2.imshow('gray', img)
#
# # читати як кольорове
# img = cv2.imread('data/lesson2/lego.jpg', cv2.IMREAD_COLOR)
# img = cv2.resize(img, (500, 500))
#
# print(img.shape)
# print(img.dtype)
#
# # піксель формат bgr
# print(img[220, 220]) # [60 75 230]
#
# cv2.imshow('color', img)
#
# # дістати черіоний колір з зображення
# # img.shape = (рядки, стовпчики, колір)
# red_part = img[:, :, 2]
# green_part = img[:, :, 1]
# blue_part = img[:, :, 0]
#
# print(red_part.shape)
# print(red_part.dtype)
#
# # якщо в shape 2 числа -- показує як чорнобіле зображення
# cv2.imshow('wrong red', red_part)
#
# # правильно
# red_part = img.copy()
# # первести синій та зелений в 0
# red_part[:, :, 0] = 0  # blue
# red_part[:, :, 1] = 0  # blue
#
# cv2.imshow('red', red_part)
# cv2.waitKey(0)
#
#
# # # rgb(bgr)
# # import utils
# #
# # utils.lesson2_bgr_range()

# кольоровий простір hsv
# h -- колір  (hue)  -- кут / 2
# s -- насиченість  (saturation)
# v -- яскравість   (value)

# import utils
#
# utils.lesson2_hsv_range()

# import cv2
#
#
# img = cv2.imread('data/lesson2/lego.jpg', cv2.IMREAD_COLOR)
# img = cv2.resize(img, (500, 500))
#
# # img -- bgr
# cv2.imshow('bgr', img)
#
# # перевести в hsv
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
# print(hsv.shape)
# print(hsv.dtype)
#
# # # думає що hsv -- bgr
# # cv2.imshow('hsv', hsv)
#
# # h -- 100-130
# # s -- 150-255
# # v -- 140-255
# mask_blue = cv2.inRange(
#     hsv,
#     (100, 150, 140), # нижні межі
#     (130, 255, 255)  # верхні межі
# )
#
# print(mask_blue.shape)
# print(mask_blue.dtype)
#
# cv2.imshow('mask_blue', mask_blue)
#
# cv2.waitKey(0)



# Відкрийте зображення data/lesson2/cell.png. Покращте
# зображення за допомогою вирівнювання гістограми. Оскільки
# зображення кольорове, вам доведеться зробити наступні
# кроки:
#  перевести зображення в LAB
#  розбити зображення на канали l, a та b
#  вирівняти гістограму для l
#  зібрати канали назад в зображення
#  перевести результат назад в BGR
# Порівняйте результати для 2 алгоритмів.


import cv2

# img = cv2.imread('data/lesson2/cell.png', cv2.IMREAD_COLOR)
# img = cv2.resize(img, (500, 500))
#
# lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#
# l = lab[:, :, 0]
# a = lab[:, :, 1]
# b = lab[:, :, 2]
#
#
# new_l = cv2.equalizeHist(l)
#
# lab[:, :, 0] = new_l
#
# cv2.imshow('new_l', new_l)
#
# new_img = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
#
# cv2.imshow('new_img', new_img)
#
# cv2.imshow('original', img)
#
# cv2.waitKey(0)
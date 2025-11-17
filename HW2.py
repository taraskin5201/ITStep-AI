# Завдання 1

import cv2
import numpy as np

# # Відкрийте зображення data/Lenna.png
# img = cv2.imread('data/lesson1/Lenna.png')
#
# cv2.imshow('img', img)
# cv2.waitKey(0)
#
# # Прочитайте маски
# # data/lesson1/mask1.png та data/lesson1/mask2.png
# mask1 = cv2.imread('data/lesson1/mask1.png', cv2.IMREAD_GRAYSCALE)
# mask2 = cv2.imread('data/lesson1/mask2.png', cv2.IMREAD_GRAYSCALE)
#
# # Об’єднайте дві маски в одну, скористайтесь cv2.bitwise_or()
# # та виведіть результат
# result = cv2.bitwise_or(mask1, mask2)
#
# # Виведіть ту частину зображення, яка відповідає:
# #  mask1
# #  mask2
# #  mask1 і mask2
# cv2.imshow('mask1', mask1)
# cv2.imshow('mask2', mask2)
# cv2.imshow('result', result)
# cv2.waitKey(0)


# Усі пікселі які не відповідають маскам замінити на 0, перед
# застосуванням змініть тип даних у масці на bool
# mask_bool = result.astype(bool)
#
# image = mask1.copy()
# image_masked = np.zeros_like(image)
# image_masked[mask_bool] = image[mask_bool]
#
# cv2.imshow("mask1", mask1)
# cv2.imshow("mask2", mask2)
# cv2.imshow("mask1+mask2", result)
# cv2.imshow("masked_result", image_masked)
#
# cv2.waitKey(0)


# Завдання 2

# Виведіть зображення. Підберіть самостійно межі

# img = cv2.imread('data/lesson1/baboo.jpg', cv2.IMREAD_GRAYSCALE)
#
# cv2.imshow('original', img)
#
# image = img.copy()
# sigment = image[15:50, 50:200]
#
# cv2.imshow('sigment', sigment)
#
# cv2.waitKey(0)


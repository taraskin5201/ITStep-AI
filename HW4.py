#  Завдання 1
# Відкрийте зображення data/lesson3/sonet.png. Проведіть
# бінарізацію.
# Обов’язково використайте:
#  розмиття або наведення різкості
#  адаптивну  бінарізацію
#  очищеня шумів

import cv2

img = cv2.imread('data/lesson3/sonet.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


res = cv2.GaussianBlur(
    gray,
    (1, 1),
    1
)

binary = cv2.adaptiveThreshold(
    res,
    255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    5,
    3
)


cv2.imshow("Original", img)
cv2.imshow("Binary", binary)

cv2.waitKey(0)


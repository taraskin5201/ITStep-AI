#  Завдання 1
# Відкрийте зображення data\lesson2\darken.png. Проведіть з
# ним наступні операції, переведіть його в HSV формат та
# обробіть канал Value наступними способами:
#  застосуйте вирівнювання гістограм
#  збільшіть значення десь на 20-50%, оскільки тут
# результат буде типу float32 та явно вийде за межі [0-255]
# застосуйте np.clip(value, 0, 255) та value.astype(np.uint8)
#  Виведіть результати обох обробок на екран

import cv2
import numpy as np


img = cv2.imread('data/lesson2/darken.png')

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)

# Вирівнювання гістограми
v_eq = cv2.equalizeHist(v)

# Підвищення яскравості (на 40%)
v_float = v.astype(np.float32)
v_brighter = v_float * 1.4
v_brighter = np.clip(v_brighter, 0, 255).astype(np.uint8)

hsv_eq = cv2.merge([h, s, v_eq])
hsv_br = cv2.merge([h, s, v_brighter])

res_eq = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)
res_br = cv2.cvtColor(hsv_br, cv2.COLOR_HSV2BGR)

cv2.imshow("Original", img)
cv2.imshow("Histogram Equalized", res_eq)
cv2.imshow("Brighter +40%", res_br)

cv2.waitKey(0)

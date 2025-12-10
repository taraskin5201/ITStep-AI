# Завдання 1
# Відкрийте зображення data/lesson_seg/tumor1.jpg
# Проведіть сегментацію зображення використовуючи
# модель data/lesson_seg/brain-tumor-seg.jpg
# Визначте площу пухлини в пікселях.
# Визначте площу в
# (1 піксель – 0,0025
# )
# В залежності від площі присвойте пухлині певний тип
#  <10     – small
#  10-25     – middle
#  >25    – large
# Покажіть пухлину – за допомогою маски усі лишні
# пікселі зробіть 0, а як назву зображення використайте її тип


import ultralytics
import cv2
import numpy as np

model = ultralytics.YOLO('data/lesson_seg/brain-tumor-seg.pt')

img = cv2.imread('data/lesson_seg/tumor1.jpg')

results = model.predict(img)
result = results[0]

masks = result.masks.data
cls = result.boxes.cls
names = result.names

mask = masks[0]
mask = mask.cpu().numpy().astype(np.uint8)

tumor_area_px = np.sum(mask)
print(f"Tumor area in pixels: {tumor_area_px}")

tumor_area = tumor_area_px * 0.0025
print(f"Tumor area: {tumor_area:.4f}")

if tumor_area < 10:
    tumor_type = "small"
elif tumor_area <= 25:
    tumor_type = "middle"
else:
    tumor_type = "large"

print(f"Tumor type: {tumor_type}")

tumor_img = np.zeros_like(img)
for c in range(3):
    tumor_img[:, :, c] = img[:, :, c] * mask

cv2.imshow(tumor_type, tumor_img)
cv2.waitKey(0)


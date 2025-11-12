# # зображення у opencv
import cv2

# читання злображення
img = cv2.imread(
    'data/lesson1/cameraman.png',  # шлях до файлу
    cv2.IMREAD_GRAYSCALE # формат зображення
)


print(type(img))
print(img)
print(img.shape)
print(img.dtype)

# показати зображення
cv2.imshow(
    'image',   # назву
    img
)

cv2.waitKey(0)
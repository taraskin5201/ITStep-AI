# # відео
# # import cv2
# #
# # img1 = cv2. imread('data/lesson3/sonet.png')
# # img2 = cv2. imread('data/lesson3/sudoku.jpg')
# #
# #
# # cv2.imshow('orig', img1)
# #
# # cv2.imshow('orig', img2)   # зітре img1 та покаже лише img2
# #
# # cv2.waitKey(0)
#
#
# import cv2
#
# # відкрити відео
# cap = cv2.VideoCapture(
#     0   # шлях до файлу аба 0 для камери в комп'ютері
# )
#
# # інформація про відео
# # розмір кадрів
# print(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))  # ширина
# print(int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  # висота
#
# # FPS -- кількість кадрів у секунду
# print(int(cap.get(cv2.CAP_PROP_FPS)))
#
# # збереження відео
# # кодек(розширення файлу(mp4, avi, xvd))
# fourcc = cv2.VideoWriter_fourcc(*"mp4v")
#
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = int(cap.get(cv2.CAP_PROP_FPS))
#
# writer = cv2.VideoWriter(
#     'result.mp4',  # шлях до файлу
#     fourcc,        # кодек
#     fps,
#     (width, height),
#     isColor=False   # чи кадри кольорові
# )
#
#
# # показ відео
# while True:
#     # дістати наступний кадр
#     success, img = cap.read()
#
#     # success -- True/False чи вдалось отримати кадр
#     if not success:
#         break  # щось сталось, зупиняємо показ кадрів
#
#     # обробка кадру
#
#     # перевести зображення в чорно біле
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # розмиття
#     gauss = cv2.GaussianBlur(
#         gray,
#         ksize=(9, 9),
#         sigmaX=1
#     )
#
#     # бінарізація
#     adapt = cv2.adaptiveThreshold(
#         gauss,
#         255,
#         cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#         cv2.THRESH_BINARY,
#         11,
#         2
#     )
#
#
#     cv2.imshow('original', img)
#     cv2.imshow('gray', gray)
#     cv2.imshow('gauss', gauss)
#     cv2.imshow('adapt', adapt)
#     # зберегти кадр до файлу
#     writer.write(adapt)
#
#     # чекаємо поки натиснеться кнопка на клавіатурі
#     # але максимум 1 мілі секунду
#
#     # якщо натиснута кнопка q то зупинити відео
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
#
# # оримати перший кадр
# _, img = cap.read()
# cv2.imshow('first frame', img)
# cv2.waitKey(0)
#
# # в кінці все закрити
# cap.release()
# writer.release()


# очистка шуму методом не локальних середніх
import cv2

img = cv2.imread('data/lesson3/sonet_noised.png', cv2.IMREAD_GRAYSCALE)
res = cv2.fastNlMeansDenoising(
    img,
    h=8,                  # параметр схожості
    templateWindowSize=7, # рамка для порівняння схожості
    searchWindowSize=11   # рамка для пошуку сусідів
)

cv2.imshow('orig', img)
cv2.imshow('res', res)
cv2.waitKey(0)
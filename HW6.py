# Завдання 1
# Відкрийте відео з файлу data\lesson8\meetings.mp4
# Застосуйте детекцію та виведіть результат, підберіть
# параметри
# Можете змінити розмір кадру для кращої візуалізації
# cv2.resize()


# import ultralytics
# import cv2
#
# model = ultralytics.YOLO('yolov8s.pt')
#
# cap = cv2.VideoCapture('data/lesson8/meetings.mp4')
#
# while True:
#     success, frame = cap.read()
#     if not success:
#         break
#
#     frame = cv2.resize(frame, None, fx=0.2, fy=0.2)
#
#
#     results = model.predict(
#         frame,
#         device='cpu',
#         conf=0.35,
#         iou=0.6
#     )
#
#     result = results[0]
#
#     res_frame = result.plot()
#
#     cv2.imshow('Meetings detection', res_frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# Завдання 2
# Відкрийте відео з файлу data\lesson8\meetings.mp4
# Застосуйте детекцію та почніть показувати відео з
# моменту, коли людей стало 5


# import ultralytics
# import cv2
#
# model = ultralytics.YOLO('yolov8s.pt')
#
# cap = cv2.VideoCapture('data/lesson8/meetings.mp4')
#
# start_show = False
#
# while True:
#     success, frame = cap.read()
#     if not success:
#         break
#
#     frame = cv2.resize(frame, None, fx=0.2, fy=0.2)
#
#     results = model.predict(
#         frame,
#         device='cpu',
#         conf=0.35,
#         iou=0.6
#     )
#
#     result = results[0]
#
#     person_count = 0
#     for c in result.boxes.cls:
#         if result.names[int(c)] == 'person':
#             person_count += 1
#
#     if person_count >= 5:
#         start_show = True
#
#     if start_show:
#         res_frame = result.plot()
#         cv2.imshow('Meetings (from 5 persons)', res_frame)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break



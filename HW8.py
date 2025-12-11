# Завдання 1
# Відкрийте відео data/lesson_pose/squat.mp4
# Ваша задача рахувати кількість присідань.
# Отримайте перший кадр та виділіть основні точки.
# Отримайте координати 3-ох точок ноги
# Визначте кут між цими трьома точками. Скористайтесь
# функцією utils.get_angle(x1, y1, x2, y2, x3, y3) де x2, y2 –
# координати коліна(центральна точка)
# Запустіть відео та добавте на сам кадр кут згинання ніг.
# Визначіть нижню межу кута(якщо людина опустилась
# нижче  вважаємо що вона достатньо опустилась) та верхню
# межу кута(якщо людина піднялась вище вважаємо що вона
# достатньо піднялась)
# Добавте кількість присідань та
# кут на кожен кадр.



import cv2
import ultralytics
import numpy as np
from utils import get_angle


model = ultralytics.YOLO("yolo11s-pose.pt")


video = cv2.VideoCapture("data/lesson_pose/squat.mp4")


counter = 0
move_down = True

LOWER_ANGLE = 60
UPPER_ANGLE = 170


while True:
    success, frame = video.read()
    frame = cv2.resize(frame, None, fx=0.4, fy=0.4)
    if not success:
        break

    results = model.predict(frame)
    result = results[0]
    keypoints = result.keypoints

    xy = keypoints.xy[0].cpu().numpy()

    hip_x, hip_y = xy[12]
    knee_x, knee_y = xy[14]
    ankle_x, ankle_y = xy[16]

    angle = get_angle(hip_x, hip_y, knee_x, knee_y, ankle_x, ankle_y)

    cv2.circle(frame, (int(hip_x), int(hip_y)), 6, (0, 255, 255), -1)
    cv2.circle(frame, (int(knee_x), int(knee_y)), 6, (0, 0, 255), -1)
    cv2.circle(frame, (int(ankle_x), int(ankle_y)), 6, (255, 0, 0), -1)

    cv2.putText(frame, f"Angle: {int(angle)} deg",
                (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 3)

    if angle < LOWER_ANGLE and move_down:
        counter += 0.5
        move_down = False

    if angle > UPPER_ANGLE and not move_down:
        counter += 0.5
        move_down = True

    cv2.putText(frame, f"Squats: {int(counter)}",
                (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()




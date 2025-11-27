# Завдання 1
# Відкрийте відео з файлу data\lesson7\meter.mp4.
# Проведіть бінарізацію кадрів та збережіть в новий файл.
# Можливо очистіть від шуму або наведіть різкість через
# bilateralFilter


import cv2

cap = cv2.VideoCapture('data/lesson7/meter.mp4')

if not cap.isOpened():
    print("Error: відео не знайдено!")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(
    'meter_binary.mp4',
    fourcc,
    fps,
    (width, height),
    isColor=False
)

while True:
    success, frame = cap.read()
    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    smooth = cv2.bilateralFilter(gray, 9, 75, 75)

    # binary = cv2.adaptiveThreshold(
    #     smooth,
    #     255,
    #     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #     cv2.THRESH_BINARY,
    #     15,
    #     2
    # )

    binary = cv2.adaptiveThreshold(
        smooth,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        45,
        3
    )

    preview = cv2.resize(binary, None, fx=0.5, fy=0.5)

    cv2.imshow("Binary video", preview)

    writer.write(binary)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
writer.release()


import cv2

def get_points(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"Point selected: ({x}, {y})")

points = []

cap = cv2.VideoCapture("../input/Задание.mp4")
ret, frame = cap.read()

if not ret:
    print("Error reading video file")
else:
    cv2.namedWindow("Frame")
    cv2.setMouseCallback("Frame", get_points)

    while True:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q") or len(points) == 2:  # Press 'q' to quit or select 4 points
            break

    cv2.destroyAllWindows()

print("Selected points:", points)
cap.release()

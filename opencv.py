import cv2

cap = cv2.VideoCapture(0)  # Try 1 or -1 if 0 doesn't work

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera is working.")

cap.release()
cv2.destroyAllWindows()

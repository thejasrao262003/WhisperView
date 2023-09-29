import cv2
import pytesseract
import cv2
from PIL import Image
from gtts import gTTS
import os

def say(text):
    os.system(f"say {text}")
# Read from USB camera
def fun4():
    cap = cv2.VideoCapture("http:10.16.160.118:4747/video")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # cv2.imshow('frame', frame)

        # Resize the frame to a smaller size
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to make text stand out from the background
        _, binary_frame = cv2.threshold(gray_frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        binary_frame = cv2.resize(binary_frame, None, fx=0.5, fy=0.5)

        # binary_frame = cv2.GaussianBlur(binary_frame, (3, 3), 0)

        # Uncomment this section to display the processed frame and recognized text using matplotlib
        # Optionally, you can apply noise reduction (e.g., Gaussian blur)
        # binary_frame = cv2.GaussianBlur(binary_frame, (3, 3), 0)

        cv2.imshow('processed frame', gray_frame)

        text = pytesseract.image_to_string(binary_frame, lang='eng', config='--psm 6')
        say(text)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

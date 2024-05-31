import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

bigote = cv2.imread('bigotes_images/bigote1.png', cv2.IMREAD_UNCHANGED) #Se puedee cambiar

def superponer_bigote(frame, x, y, w, h, y_offset):
    bigote_resized = cv2.resize(bigote, (w, int(h/2)))  
    alpha_s = bigote_resized[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    # Posicionamiento del bigote debajo de la nariz y sobre la parte superior del labio
    y += int(h/2) + y_offset

    for c in range(0, 3):
        frame[y:y+int(h/2), x:x+w, c] = (alpha_s * bigote_resized[:, :, c] +
                                          alpha_l * frame[y:y+int(h/2), x:x+w, c])

def mainBigote():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            superponer_bigote(frame, x, y, w, h, y_offset=0)

        cv2.imshow('Bigote', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or cv2.getWindowProperty('Bigote', cv2.WND_PROP_VISIBLE) < 1:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    mainBigote()

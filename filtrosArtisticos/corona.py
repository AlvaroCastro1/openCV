import cv2
import numpy as np

def superponer_corona(frame, x, y, w, h, y_offset, corona):
    corona_resized = cv2.resize(corona, (w, int(h/3))) 
    alpha_s = corona_resized[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    # Posicionamiento de la corona sobre la parte superior de la cabeza
    y -= int(h/3) + y_offset

    for c in range(0, 3):
        frame[y:y+int(h/3), x:x+w, c] = (alpha_s * corona_resized[:, :, c] +
                                          alpha_l * frame[y:y+int(h/3), x:x+w, c])

def mainCorona():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    lista_coronas = ['coronas_images/corona1.png', 'coronas_images/corona2.png', 'coronas_images/corona3.png']
    corona_index = 0
    corona = cv2.imread(lista_coronas[corona_index], -1)

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if not ret:
            break

        # Convertir a escala de grises para la detección facial
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar rostros
        faces = face_cascade.detectMultiScale(gray, 1.3, 8)

        # Superponer la corona con un desplazamiento en la altura
        for (x, y, w, h) in faces:
            superponer_corona(frame, x, y, w, h, y_offset=8, corona=corona)  

        # Mostrar el resultado
        cv2.imshow('Frame', frame)

        # Capturar entrada del teclado
        key = cv2.waitKey(1) & 0xFF

        # Cambiar la imagen de la corona con la tecla "k"
        if key == ord('k'):
            corona_index = (corona_index + 1) % len(lista_coronas)
            corona = cv2.imread(lista_coronas[corona_index], -1)

        # Salir con la tecla 'q' o haciendo clic en la 'X' de la ventana
        if key == ord('q') or cv2.getWindowProperty('Frame', cv2.WND_PROP_VISIBLE) < 1:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    mainCorona()

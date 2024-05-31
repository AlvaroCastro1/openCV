import cv2
import numpy as np

def superponer_lentes(frame, lentes, x, y, w, h, y_offset):
    lentes_resized = cv2.resize(lentes, (w, h))
    alpha_s = lentes_resized[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s
    y += y_offset
    for c in range(0, 3):
        frame[y:y+h, x:x+w, c] = (alpha_s * lentes_resized[:, :, c] +
                                  alpha_l * frame[y:y+h, x:x+w, c])

def mainLentes():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Lista de imágenes de lentes
    imagenes_lentes = ['lentes_images/lente7.png', 'lentes_images/lente3.png', 'lentes_images/lente4.png', 'lentes_images/lente5.png', 'lentes_images/lente6.png', 'lentes_images/lentes1.png']
    lentes_index = 0
    lentes = cv2.imread(imagenes_lentes[lentes_index], -1)
    if lentes is None:
        print(f"Error: No existen elementos en la lista de imagenes  {imagenes_lentes[lentes_index]}")
        return

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            superponer_lentes(frame, lentes, x, y, w, h, y_offset=-25)

        cv2.imshow('Filtro', frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('k'):
            lentes_index = (lentes_index + 1) % len(imagenes_lentes)
            lentes = cv2.imread(imagenes_lentes[lentes_index], -1)
            if lentes is None:
                print(f"Error:No se puede leer la imagen en el frame{imagenes_lentes[lentes_index]}")
                continue

        if key == ord('q') or cv2.getWindowProperty('Filtro', cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    mainLentes()

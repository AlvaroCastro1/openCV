import cv2
import numpy as np
import tkinter as tk
from tkinter import Scale, filedialog
from PIL import Image, ImageTk

#Clase de rotacion ara una imagen 
class Rotacion_imagenes:
    def __init__(self):
        self.rotacion_imagen = None
        self.original_image = None
        self.angulo_scale = None
        self.rotacion_resultado = None  # Definir el atributo rotacion_resultado

    def rotacion_image(self, angulo):
        angulo = float(angulo)
        self.rotacion_imagen = self.rotacion(self.original_image, angulo)
        self.update_image(self.rotacion_imagen)

    def rotacion(self, image, angulo):
        image_center = tuple(np.array(image.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, angulo, 1.0)
        result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
        return result

    def update_image(self, cv2_image):
        pil_image = Image.fromarray(cv2_image)
        photo = ImageTk.PhotoImage(image=pil_image)
        self.rotacion_resultado.config(image=photo)
        self.rotacion_resultado.image = photo

    def guardar_imagen(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
        if filepath:
            cv2.imwrite(filepath, cv2.cvtColor(self.rotacion_imagen, cv2.COLOR_RGB2BGR))
            print(f"Imagen guardada como {filepath}")

    def actualizar_rotacion(self, event):
        angulo = self.angulo_scale.get()
        self.rotacion_image(angulo)

if __name__ == "__main__":
    rotacion_instancia = Rotacion_imagenes()

    rotacion_instancia.original_image = cv2.imread("lorito.png")
    rotacion_instancia.original_image = cv2.cvtColor(rotacion_instancia.original_image, cv2.COLOR_BGR2RGB)

    root = tk.Tk()
    root.title("Rotación de Imagen")

    # Barra de desplazamiento para seleccionar el ángulo de rotación
    rotacion_instancia.angulo_scale = Scale(root, from_=0, to=360, orient="horizontal", label="Ángulo de Rotación", length=300)
    rotacion_instancia.angulo_scale.pack()

    # Asociar la barra de desplazamiento a la función de actualización
    rotacion_instancia.angulo_scale.bind("<ButtonRelease-1>", rotacion_instancia.actualizar_rotacion)

    rotacion_instancia.rotacion_resultado = tk.Label(root)
    rotacion_instancia.rotacion_resultado.pack()
    guardar_button = tk.Button(root, text="Guardar Imagen", command=rotacion_instancia.guardar_imagen)
    guardar_button.pack()

    original_photo = ImageTk.PhotoImage(Image.fromarray(rotacion_instancia.original_image))
    original_label = tk.Label(root, image=original_photo)
    original_label.pack()

    root.mainloop()

from tkinter import filedialog
from tkinter import messagebox
import cv2

def guardar_imagen_ruta(imagen):
        # Obtener la ruta de guardado de la imagen
        ruta_guardado = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
        if ruta_guardado:
            cv2.imwrite(ruta_guardado, imagen)
            messagebox.showinfo("Guardado", "Imagen guardada exitosamente en: {}".format(ruta_guardado))
    

import cv2
import numpy as np

def top_hat(image, kernel_size=(5,5)):
    # Aplicar una operación de apertura a la imagen
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size))
    # Calcular la diferencia entre la imagen original y la imagen abierta
    top_hat_image = cv2.subtract(image, opening)
    return top_hat_image

def black_hat(image, kernel_size=(5,5)):
    # Aplicar una operación de cierre a la imagen
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size))
    # Calcular la diferencia entre la imagen cerrada y la imagen original
    black_hat_image = cv2.subtract(closing, image)
    return black_hat_image

def skeletonize(image):
    # Crear un kernel estructurante
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    done = False
    # Aplicar iterativamente la transformación hasta que no haya cambios en la imagen
    while not done:
        eroded = cv2.erode(image, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(image, temp)
        skeleton = cv2.bitwise_or(cv2.bitwise_and(image, temp), eroded)
        done = cv2.countNonZero(image) == cv2.countNonZero(skeleton)
        image = skeleton
    return skeleton

def fill_edges(image):
    # Duplicar la imagen
    filled_image = image.copy()
    # Encontrar los contornos de la imagen
    contours, _ = cv2.findContours(filled_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Rellenar los contornos
    cv2.drawContours(filled_image, contours, -1, (255, 255, 255), thickness=cv2.FILLED)
    return filled_image

if __name__ == "__main__":
    # Cargar una imagen de ejemplo
    image = cv2.imread("example.jpg", cv2.IMREAD_GRAYSCALE)

    # Realizar las operaciones morfológicas
    top_hat_result = top_hat(image)
    black_hat_result = black_hat(image)
    skeleton_result = skeletonize(image)
    fill_edges_result = fill_edges(image)

    # Mostrar los resultados
    cv2.imshow("Original", image)
    cv2.imshow("Top Hat", top_hat_result)
    cv2.imshow("Black Hat", black_hat_result)
    cv2.imshow("Skeleton", skeleton_result)
    cv2.imshow("Fill Edges", fill_edges_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

import cv2
import numpy as np

def gradiente(image):

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    dilatacion = cv2.dilate(image, kernel)

    erocion = cv2.erode(image, kernel)

    gradiente = cv2.subtract(dilatacion, erocion)
    return gradiente

if __name__ == "__main__":
    image = cv2.imread("images/coins.png", 0)
    cv2.imshow('Original', image)
    gradiente=gradiente(image)
    cv2.imshow('gradientee Morfológico', gradiente)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
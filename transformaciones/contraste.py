import cv2
import numpy as np

#-------------------------------------------Contraste a Color--------------------------------------------------------
def contraste_operacion(img1, factor_contraste):

    factor_contraste = (factor_contraste + 100) / 100
    img1_float = img1.astype(np.float32) / 255.0

    img1_contrast = np.zeros_like(img1_float)
    for i in range(img1.shape[2]):  
        img1_contrast[:, :, i] = np.clip((img1_float[:, :, i] - 0.5) * factor_contraste + 0.5, 0, 1)
    return (img1_contrast * 255).astype(np.uint8)

#---------------------------------------------Contraste a escala de Grises--------------------------------------------
def ope_contraste_bw(img1, factor_contraste):

    factor_contraste = (factor_contraste + 100) / 100
    img1_float = img1.astype(np.float32) / 255.0

    img1_contrast = np.clip((img1_float - 0.5) * factor_contraste + 0.5, 0, 1)
    return (img1_contrast * 255).astype(np.uint8)


if __name__ == "__main__":
    img1 = cv2.imread("flor.png")
    factor_contraste = float(input("Ingresa el valor del factor de contraste entre -100 y 100: "))
    img1n_con_contraste = aplicar_contraste(img1.copy(), factor_contraste)
    cv2.imshow("Imagen original", img1)
    cv2.imshow("Imagen con contraste aplicado", img1n_con_contraste)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

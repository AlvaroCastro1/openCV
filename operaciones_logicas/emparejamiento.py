import cv2

def emparejar_canales(image1, image2):
    # print(f"{image1.shape} {image2.shape}")
    
    if len(image1.shape) == 3 and len(image2.shape) == 3:
        # ambas img son a color
        pass

    elif len(image1.shape) == 2 and len(image2.shape) == 2:
        # ambas img son a escala de grises
        pass
    
    else:  # una de las img es a color y la otra en escala de grises
        if len(image1.shape) == 2:  # Si la imagen 1 está en escala de grises, convierte la imagen 2
            image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        elif len(image2.shape) == 2:  # Si la imagen 2 está en escala de grises, convierte la imagen 1
            image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    # print(f"{image1.shape} {image2.shape}")

    return image1, image2

if __name__ == "__main__":
    img1 = "C:/Users/Hp245-User/Desktop/openCV/images/lc3.tiff"
    img2 = "C:/Users/Hp245-User/Desktop/openCV/images/lenacolor.png"

    imagen1 = cv2.imread(img1)
    imagen1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)
    imagen2 = cv2.imread(img2)

    imagen1, imagen2 = emparejar_canales(imagen1, imagen2)

    cv2.imshow("Img1", imagen1)
    cv2.imshow("Img2", imagen2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
import numpy as np
import cv2

def rgb2cmyk(imagen_rgb):
    alto, ancho, _ = imagen_rgb.shape
    
    if imagen_rgb.shape[2] != 3:
        raise ValueError("La imagen debe ser RGB")
    
    imagen_cmyk = np.zeros((alto, ancho, 4), dtype=np.float32)

    # cada pixel RGB a CMYK
    for i in range(alto):
        for j in range(ancho):
            # Convertir el valor RGB a CMY
            r = imagen_rgb[i, j, 2] / 255.0  # Rojo
            g = imagen_rgb[i, j, 1] / 255.0  # Verde
            b = imagen_rgb[i, j, 0] / 255.0  # Azul
            
            # Calcular CMY
            c = 1 - r
            m = 1 - g
            y = 1 - b
            
            # Calcular K
            k = min(c, m, y)
            
            # Ajustar CMY por K
            c = (c - k) / (1 - k) if (1 - k) != 0 else 0
            m = (m - k) / (1 - k) if (1 - k) != 0 else 0
            y = (y - k) / (1 - k) if (1 - k) != 0 else 0
            
            # Almacenar valores CMYK en la imagen
            imagen_cmyk[i, j] = [c, m, y, k]
    
    return imagen_cmyk


def rgb2hsv(imagen_rgb):
    alto, ancho, _ = imagen_rgb.shape
    imagen_hsv = np.zeros((alto, ancho, 3), dtype=np.float32)

    if imagen_rgb.shape[2] != 3:
        raise ValueError("La imagen debe ser RGB")
    
    for i in range(alto):
        for j in range(ancho):
            # normalizar de 0-1
            r = imagen_rgb[i, j, 0] / 255.0
            g = imagen_rgb[i, j, 1] / 255.0
            b = imagen_rgb[i, j, 2] / 255.0

            max_val = max(r, g, b)
            min_val = min(r, g, b)
            delta = max_val - min_val

            if delta == 0:
                hue = 0
            elif max_val == r:
                hue = (60 * ((g - b) / delta) + 360) % 360
            elif max_val == g:
                hue = (60 * ((b - r) / delta) + 120) % 360
            elif max_val == b:
                hue = (60 * ((r - g) / delta) + 240) % 360

            # Convertir a rango 0-180
            hue = hue / 2

            saturacion = 0 if max_val == 0 else delta / max_val

            brillo = max_val

            saturacion = int(saturacion * 255)
            brillo = int(brillo * 255)

            imagen_hsv[i, j] = [hue, saturacion, brillo]

    return imagen_hsv.astype(np.uint8)

def rgb2bgr(imagen_rgb):
    if imagen_rgb.shape[2] != 3:
        raise ValueError("La imagen debe ser RGB")
    
    return imagen_rgb[:, :, ::-1]  # inviertir el orden

def rgb2hls(imagen_rgb):
    alto, ancho, _ = imagen_rgb.shape
    imagen_hls = np.zeros((alto, ancho, 3), dtype=np.float32)

    if imagen_rgb.shape[2] != 3:
        raise ValueError("La imagen debe ser RGB")
    
    for i in range(alto):
        for j in range(ancho):
            # Normalizar a 0-1
            r = imagen_rgb[i, j, 0] / 255.0
            g = imagen_rgb[i, j, 1] / 255.0
            b = imagen_rgb[i, j, 2] / 255.0

            max_val = max(r, g, b)
            min_val = min(r, g, b)
            delta = max_val - min_val

            claridad = (max_val + min_val) / 2

            # calcular Hue
            if delta == 0:
                hue = 0
            elif max_val == r:
                hue = (60 * ((g - b) / delta) + 360) % 360
            elif max_val == g:
                hue = (60 * ((b - r) / delta) + 120) % 360
            elif max_val == b:
                hue = (60 * ((r - g) / delta) + 240) % 360

            hue = hue / 2  # rango 0-180

            if delta == 0:
                saturacion = 0
            elif claridad < 0.5:
                saturacion = delta / (max_val + min_val)
            else:
                saturacion = delta / (2 - (max_val + min_val))

            saturacion = int(saturacion * 255)

            claridad = int(claridad * 255)

            imagen_hls[i, j] = [hue, claridad, saturacion]

    return imagen_hls.astype(np.uint8)


if __name__ == "__main__":
    imagen_rgb = cv2.imread("/home/alvaro/Público/openCV/images/flowers.jpg")
    cv2.imshow("original", imagen_rgb)

    imagen_cmyk = rgb2cmyk(imagen_rgb)
    cv2.namedWindow("cmyk", cv2.WINDOW_NORMAL)
    cv2.imshow("cmyk", imagen_cmyk)

    imagen_hsv = rgb2hsv(imagen_rgb)
    cv2.namedWindow("hsv", cv2.WINDOW_NORMAL)
    cv2.imshow("hsv", imagen_hsv)

    imagen_hls = rgb2hls(imagen_rgb)
    cv2.namedWindow("hls", cv2.WINDOW_NORMAL)
    cv2.imshow("hls", imagen_hls)

    cv2.waitKey()
    cv2.destroyAllWindows()
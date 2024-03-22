import numpy as np
import cv2

def shear_horizontal(image, shear_factor):
    height, width = image.shape[:2]
    
    # Definir la matriz de transformación de shear horizontal
    shear_matrix = np.array([
        [1, 0, 0],
        [shear_factor, 1, 0],
        [0, 0, 1]
    ])
    
    # Crear una lista de coordenadas de píxeles en la imagen original
    coords = np.indices((height, width), dtype=np.float32)
    coords = np.vstack((coords.reshape(2, -1), np.ones((1, height*width))))
    
    # Aplicar la transformación de shear a las coordenadas
    sheared_coords = np.dot(shear_matrix, coords).astype(np.int32)
    
    # Redondear los valores de coordenadas
    sheared_coords[0] = np.clip(sheared_coords[0], 0, height - 1)
    sheared_coords[1] = np.clip(sheared_coords[1], 0, width - 1)
    
    # Mapear los valores de píxeles de la imagen original a la imagen transformada
    sheared_image = np.zeros_like(image)
    sheared_image[sheared_coords[0], sheared_coords[1]] = image[sheared_coords[0], sheared_coords[1]]
    
    return sheared_image

# Cargar la imagen
image_path = 'c:/Users/Hp245-User/Desktop/openCV/images/amarilla.png'
# image = cv2.imread(image_path, 0)
image = cv2.imread(image_path)

# Factor de shear horizontal
shear_factor = 0.5


# Aplicar la transformación de shear horizontal a la imagen
sheared_image = shear_horizontal(image, shear_factor)

# Mostrar la imagen original y la imagen transformada
cv2.imshow('Imagen original', image)
cv2.imshow('Imagen con shear horizontal', sheared_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

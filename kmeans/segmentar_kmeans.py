import cv2
import numpy as np

def inicializar_centroides(datos, k):
    centroides = []
    # seleccionar un pixel random y hacerlo centroide 
    centroides.append(datos[np.random.randint(datos.shape[0])])

    
    for _ in range(1, k):
        # calcula la distancia mínima de cada pixel a los centroides
        distancias = np.array([min([np.linalg.norm(x-c) for c in centroides]) for x in datos])
        # validar que tan cerca esta cada punto de datos de los centroides 
        probabilidades = distancias / distancias.sum()
        probabilidades_acumuladas = probabilidades.cumsum()
        # seleccionar un pixel random segun las probabilidades 
        aleatorio = np.random.rand()
        # el primer pixel que tenga una prob acum mayor se elige como nuevo centroide
        indice = np.where(probabilidades_acumuladas >= aleatorio)[0][0]
        centroides.append(datos[indice])
        
    return np.array(centroides)

def kmeans(imagen, k=2, max_iter=100):
    # adaptar imagen a una matriz (n*m, #canal)
    if len(imagen.shape) == 3:
        datos = imagen.reshape((-1, 3)).astype(np.float32)
    else:
        datos = imagen.reshape((-1, 1)).astype(np.float32)

    centroides = inicializar_centroides(datos, k)

    for _ in range(max_iter):
        """calcular distancia euclidiana (punto y centroide)
        pixel -> (n, 1, d) y centroides -> (k, d)
        realizar la resta
        """
        distancias = np.linalg.norm(datos[:, np.newaxis] - centroides, axis=2)

        # asignacion de cluster
        """
        cada indice conteiene la distancia que existe entre el cluster y el pixel
        np.argmin -> devuelve el indice con la menor distancia
        """
        
        etiquetas = np.argmin(distancias, axis=1)

        # actualizar centroides
        nuevos_centroides = np.array([datos[etiquetas == i].mean(axis=0) for i in range(k)])

        # si estan cerca debe terminar la asignacion
        if np.allclose(centroides, nuevos_centroides):
            break

        centroides = nuevos_centroides

    imagen_segmentada = centroides[etiquetas].reshape(imagen.shape)

    return imagen_segmentada

if __name__ == "__main__":
    image = cv2.imread("c:/Users/Hp245-User/Desktop/openCV/images/perro.jpg",0)

    segmented_image = kmeans(image)

    cv2.namedWindow("imagen original", cv2.WINDOW_NORMAL)
    cv2.imshow("imagen original", image)

    cv2.namedWindow("imagen segmentada", cv2.WINDOW_NORMAL)
    cv2.imshow("imagen segmentada", segmented_image.astype(np.uint8))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
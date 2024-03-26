# https://youtu.be/X-Y91ddBqaQ

import cv2
from sklearn.cluster import KMeans

def segmentar_con_kmeans(imagen, n_clusters=2):
    if len(imagen.shape) == 3:  # Verificar si la imagen es a color
        X = imagen.reshape(-1, 3)
    elif len(imagen.shape) == 2:  # Si la imagen es en escala de grises
        X = imagen.reshape(-1, 1)
    else:
        raise ValueError("Formato de imagen no compatible.")

    kmeans = KMeans(n_clusters=n_clusters, n_init=10)
    kmeans.fit(X)
    imagen_seg = kmeans.cluster_centers_[kmeans.labels_]
    imagen_seg = imagen_seg.reshape(imagen.shape)

    return imagen_seg/255

if __name__ == "__main__":
    imagen = cv2.imread("c:/Users/Hp245-User/Desktop/openCV/images/perro.jpg")
    cv2.namedWindow("imagen original", cv2.WINDOW_NORMAL)
    cv2.imshow("imagen original", imagen)

    imagen_seg = segmentar_con_kmeans(imagen, n_clusters=3)
    cv2.namedWindow("imagen segmentada", cv2.WINDOW_NORMAL)
    cv2.imshow("imagen segmentada", imagen_seg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
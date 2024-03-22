# https://youtu.be/X-Y91ddBqaQ

import cv2
from sklearn.cluster import KMeans


image=cv2.imread("c:/Users/Hp245-User/Desktop/openCV/images/perro.jpg")
cv2.namedWindow("imagen original", cv2.WINDOW_NORMAL)
cv2.imshow("imagen original", image)

X = image.reshape(-1,3)
kmeans = KMeans(n_clusters=5, n_init=10)
kmeans.fit(X)
imagen_seg = kmeans.cluster_centers_[kmeans.labels_]
imagen_seg = imagen_seg.reshape(image.shape)

cv2.namedWindow("imagen segmentada", cv2.WINDOW_NORMAL)
cv2.imshow("imagen segmentada", imagen_seg/255)

cv2.waitKey(0)
cv2.destroyAllWindows()
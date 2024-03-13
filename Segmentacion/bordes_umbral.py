import cv2

def umbral(valor):
    _, th = cv2.threshold(img, valor, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow("Binarizando", th)

cv2.namedWindow("Binarizando")
img = cv2.imread("C:/Users/Hp245-User/Desktop/openCV/images/coins.png",0)

cv2.createTrackbar("Umbral", "Binarizando", 0, 255, umbral)

cv2.waitKey()
cv2.destroyAllWindows()

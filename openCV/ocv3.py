import cv2
import numpy as np
import matplotlib.pyplot as plt

bgr = cv2.imread("C:/Users/Hp245-User/Desktop/openCV/images/peppers.tiff")
cv2.imshow("Color BGR", bgr )
cv2.waitKey()

rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

plt.figure(1)
plt.subplot(311)  # 3f 1c 1 
plt.title("Peppers 256")
plt.hist(rgb.ravel(), bins=256 )   
plt.subplot(313)   #3 1 3
plt.imshow(rgb)
plt.subplot(312)  # 3f 1c pos2
plt.title("Peppers 64")
plt.hist(rgb.ravel(), bins=64 )
plt.show()


print( "RGB: ", rgb.shape, "\t (200,60): ", rgb[200,60] )
print( "BGR: ", bgr.shape, "\t (200,60): ", bgr[200,60] )

px = rgb[200,60]
print("Pixel: ", px)

pxr, pxg, pxb = rgb[200,60]
print("Rojo: ", pxr)
print("Verde: ", pxg)
print("Azul: ", pxb)

cv2.destroyAllWindows()

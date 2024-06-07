## Operaciones

- *kernel*
- *imagen*

```python
import cv2
import numpy as np

# Cargar la imagen en escala de grises
imagen = cv2.imread('imagen.png', 0)

# Crear un kernel
kernel = np.ones((5, 5), np.uint8)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow('Original', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### 1. Dilatación
**Descripción**: La dilatación expande las regiones blancas de una imagen binaria.

**Código**:
```python
# Aplicar dilatación
imagen_dilatada = cv2.dilate(imagen, kernel, iterations=1)
```

### 2. Erosión
**Descripción**: La erosión reduce las regiones blancas de una imagen binaria.

**Código**:
```python
# Aplicar erosión
imagen_erosionada = cv2.erode(imagen, kernel, iterations=1)
```

### 3. Apertura
**Descripción**: La apertura elimina pequeños objetos del primer plano (blanco) de una imagen binaria.

**Código**:
```python
# Aplicar apertura
imagen_apertura = cv2.morphologyEx(imagen, cv2.MORPH_OPEN, kernel)
```

### 4. Clausura
**Descripción**: La clausura cierra pequeños huecos en el fondo (negro) de una imagen binaria.

**Código**:
```python
# Aplicar clausura
imagen_clausura = cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, kernel)
```

### 5. Top Hat
**Descripción**: La transformación Top Hat resalta los objetos más pequeños de una imagen.

**Código**:
```python
# Aplicar top hat
imagen_top_hat = cv2.morphologyEx(imagen, cv2.MORPH_TOPHAT, kernel)
```

### 6. Black Hat
**Descripción**: La transformación Black Hat resalta los pequeños huecos en una imagen.

**Código**:
```python
# Aplicar black hat
imagen_black_hat = cv2.morphologyEx(imagen, cv2.MORPH_BLACKHAT, kernel)
```

### 7. Esqueletización
**Descripción**: La esqueletización reduce las estructuras a sus esqueleto, preservando su conectividad.

**Código**:
```python
from skimage.morphology import skeletonize


# Binarizar la imagen
_, imagen_binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

# Esqueletización
esqueleto = skeletonize(imagen_binaria // 255) * 255

cv2.imshow('Esqueletización', esqueleto.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 8. Rellenar Borde
**Descripción**: Rellena los huecos en el borde de una imagen binaria.

**Código**:
```python
# Binarizar la imagen
_, imagen_binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY_INV)

# Rellenar borde
imagen_rellenada = flood_fill(imagen_binaria, (0, 0), 255)
```

### 9. Gradiente Morfológico
**Descripción**: El gradiente morfológico resalta los bordes de los objetos en una imagen.

**Código**:
```python
# Aplicar gradiente morfológico
gradiente = cv2.morphologyEx(imagen, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('Gradiente Morfológico', gradiente)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 10. Transformada de Hough
**Descripción**: Detecta líneas en una imagen usando la transformada de Hough.

**Código**:
```python
# Aplicar transformada de Hough
imagen = cv2.imread('imagen.png')
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
bordes = cv2.Canny(imagen_gris, 50, 150, apertureSize=3)
lineas = cv2.HoughLines(bordes, 1, np.pi / 180, 200)

for linea in lineas:
    rho, theta = linea[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(imagen, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('Transformada de Hough', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 11. Momentos de Hu
**Descripción**: Los momentos de Hu son un conjunto de valores que son invariables a transformaciones como la traslación, la escala y la rotación, y son útiles para la clasificación de formas.

**Código**:
```python
# Calcular los momentos de Hu
momentos = cv2.moments(imagen)
hu_momentos = cv2.HuMoments(momentos).flatten()

print("Momentos de Hu:")
for i, momento in enumerate(hu_momentos):
    print(f"Hu[{i}] = {momento}")
```

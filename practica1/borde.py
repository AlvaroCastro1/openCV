from PIL import Image

imagen = Image.open('C:/Users/Hp245-User/Desktop/openCV/images/cameraman.png')

borde_size = 10
borde_color = (255, 255, 255)  # Color blanco

ancho, alto = imagen.size

imagen_con_borde = Image.new('RGB', (ancho + 2 * borde_size, alto + 2 * borde_size), borde_color)

imagen_con_borde.paste(imagen, (borde_size, borde_size))

imagen_con_borde.save("borde.png")

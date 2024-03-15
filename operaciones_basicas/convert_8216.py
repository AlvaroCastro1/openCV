import numpy as np
def transformar(g):
    valor_min = np.min(g)
    gm = g - valor_min

    valor_max = np.max(gm)
    gs = (gm / valor_max) * 255

    gs = gs.astype(np.uint8)

    return gs
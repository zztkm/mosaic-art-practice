import matplotlib.pyplot as plt
import skimage.transform
import skimage.io
import skimage.color
import numpy as np


def trisize(Hm, Wm, Ib):
    Hb = Ib.shape[0]
    Wb = Ib.shape[1]
    ratio_m = Wm / Hm
    ratio_b = Wb / Hb
    if ratio_b == ratio_m:
        T = skimage.transform.resize(Ib, (Hm, Wm, 3), anti_aliasing=True)
    elif ratio_b > ratio_m:
        T = skimage.transform.resize(
            Ib, (Hm, np.floor(ratio_b * Hm), 3), anti_aliasing=True
        )
        T = T[:, :Wm]
    else:
        T = skimage.transform.resize(
            Ib, (np.floor(Wm * Hb / Wb), Wm, 3), anti_aliasing=True
        )
        T = T[:Hm, :]
    return T


def small_lab(I):
    return skimage.color.rgb2lab(
        skimage.transform.resize(I, (8, 8, 3), anti_aliasing=True)
    )

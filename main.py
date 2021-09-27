import sys

import matplotlib.pyplot as plt
import skimage.transform
import skimage.io
import skimage.color
import skimage.util
import numpy as np

from trisize import trisize, small_lab


def main():

    with open("./img_urls.txt", "r", encoding="utf-8") as f:
        image_urls = f.read().splitlines()

    img_src = sys.argv[1]

    I = skimage.io.imread(img_src)
    I = skimage.transform.resize(
        I, (I.shape[0] * 2, I.shape[1] * 2, 3), anti_aliasing=True
    )

    row_split = 50
    col_split = 28

    print("ブロックの高さ:{}".format(I.shape[0] / row_split))
    print("ブロックの幅:{}".format(I.shape[1] / col_split))
    print("ブロックの高さの余り:{}".format(I.shape[0] % row_split))
    print("ブロックの幅の余り:{}".format(I.shape[1] % col_split))

    row1_size = I.shape[0] // row_split
    col1_size = I.shape[1] // col_split
    I_tri = I[: (row1_size * row_split), : (col1_size * col_split), :]
    Ims = skimage.util.view_as_blocks(I_tri, (row1_size, col1_size, 3))

    n = 0
    url_nums = []
    Ibs = np.zeros((row1_size, col1_size, 3, 500))
    for i, U in enumerate(image_urls):
        try:
            Iu = skimage.io.imread(U)
        except:
            continue
        if len(Iu.shape) == 2:
            continue
        url_nums.append(i)
        Ibs[:, :, :, n] = trisize(row1_size, col1_size, Iu)
        n += 1
    Ibs = Ibs[:, :, :, :n]

    slabs = np.zeros((8, 8, 3, n))
    for i in range(n):
        slabs[:, :, :, i] = small_lab(Ibs[:, :, :, i])

    IM = np.zeros((row_split * row1_size, col_split * col1_size, 3))
    for row in range(row_split):
        for col in range(col_split):
            Im = small_lab(Ims[row, col, 0, :, :, :])
            min_diff = np.sum(skimage.color.deltaE_cie76(Im, slabs[:, :, :, 0]))
            min_idx = 0
            for i in range(1, n):
                diff = np.sum(skimage.color.deltaE_cie76(Im, slabs[:, :, :, i]))
                if diff < min_diff:
                    min_diff = diff
                    min_idx = i
            IM[
                (row * row1_size) : ((row + 1) * row1_size),
                (col * col1_size) : ((col + 1) * col1_size),
                :,
            ] = Ibs[:, :, :, min_idx]
    plt.subplot(1, 2, 1)
    plt.imshow(I)
    plt.axis("off")
    plt.subplot(1, 2, 2)
    plt.imshow(IM)
    plt.axis("off")
    plt.gcf().set_size_inches(15, 15)
    plt.show()


if __name__ == "__main__":
    main()

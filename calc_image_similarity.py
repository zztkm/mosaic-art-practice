import matplotlib.pyplot as plt
import skimage.io
import numpy as np

I = skimage.io.imread("./img/hyou-1-bg-waterblue.jpg")
I_G80 = I.copy()
I_G80[:, :, 1] = I_G80[:, :, 1] * 0.8
I_B80 = I.copy()
I_B80[:, :, 2] = I_B80[:, :, 2] * 0.8
plt.subplot(1, 3, 1)
plt.imshow(I)
plt.subplot(1, 3, 2)
plt.imshow(I_G80)
plt.subplot(1, 3, 3)
plt.imshow(I_B80)
plt.gcf().set_size_inches(15, 15)
plt.show()

I_Lab = skimage.color.rgb2lab(I)
I_G80Lab = skimage.color.rgb2lab(I_G80)
I_B80Lab = skimage.color.rgb2lab(I_B80)
print("I_Lab, I_Lab", np.sum(skimage.color.deltaE_cie76(I_Lab, I_Lab)))
print("I_Lab, I_G80Lab", np.sum(skimage.color.deltaE_cie76(I_Lab, I_G80Lab)))
print("I_Lab, I_B80Lab", np.sum(skimage.color.deltaE_cie76(I_Lab, I_B80Lab)))

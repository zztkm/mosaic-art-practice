import matplotlib.pyplot as plt
import skimage.io

url = "https://images.metmuseum.org/CRDImages/es/web-large/DT7115.jpg"

plt.imshow(skimage.io.imread(url))
plt.show()

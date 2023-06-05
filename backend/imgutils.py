import cv2
import numpy as np

def crop_squared_and_reshape(img, shape):
    a = img.shape[0]//2
    b = img.shape[1]//2

    if img.shape[0] > img.shape[1]:
        img = np.copy(img[a-b:a+b, :])
    elif img.shape[0] < img.shape[1]:
        img = np.copy(img[:, b-a:b+a])

    return cv2.resize(img, shape)

def calc_dist(img):
    print(img.shape)
    distas = (0, 0)
    larriba = []
    labajo = []

    for i in range(16):
        # para arriba:
        larriba.append(abs(img[16 - i, 16, 0] - img[17 - i, 16, 0]))
        # para abajo: 
        labajo.append(abs(img[15 + i, 16, 0] - img[16 + i, 16, 0]))

    return np.argmax(larriba) + np.argmax(labajo)
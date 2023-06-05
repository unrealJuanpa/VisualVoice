import cv2
import numpy as np

alturas = { # en metros
    'avión': 15,
    'automóvil': 1.3,
    'pájaro': 0.16,
    'ciervo': 1.3,
    'gato': 0.25,
    'perro': 0.60,
    'rana': 0.08,
    'caballo': 1.6,
    'barco': 60,
    'camión': 4.3
}

def crop_squared_and_reshape(img, shape):
    a = img.shape[0]//2
    b = img.shape[1]//2

    if img.shape[0] > img.shape[1]:
        img = np.copy(img[a-b:a+b, :])
    elif img.shape[0] < img.shape[1]:
        img = np.copy(img[:, b-a:b+a])

    return cv2.resize(img, shape)

def calc_dist(img, clase):
    print(img.shape)
    distas = (0, 0)
    larriba = []
    labajo = []

    for i in range(16):
        # para arriba:
        larriba.append(abs(img[16 - i, 16, 0] - img[17 - i, 16, 0]))
        # para abajo: 
        labajo.append(abs(img[15 + i, 16, 0] - img[16 + i, 16, 0]))

    altura = (14.4*alturas[clase])/(np.argmax(larriba) + np.argmax(labajo))
    return altura
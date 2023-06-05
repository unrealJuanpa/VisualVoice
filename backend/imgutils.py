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

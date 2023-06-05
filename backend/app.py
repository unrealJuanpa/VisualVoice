from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
from PIL import Image
import io
import socket
import imgutils
from model import Classifier
# inbound rule to port 9000 on TCP

mcf = Classifier()
mcf.load_weights('modelcifar10-loss00007.h5')
print('modelo cargado!')
classnames = [
    'avión',
    'automóvil',
    'pájaro',
    'ciervo',
    'gato',
    'perro',
    'rana',
    'caballo',
    'barco',
    'camión'
] 

def obtener_direccion_ip():
    hostname = socket.gethostname()
    direccion_ip = socket.gethostbyname(hostname)
    print(direccion_ip)
    return direccion_ip

app = Flask(__name__)
CORS(app)

def base64_to_image(base64_string):
    image_data = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(image_data))
    # image = np.array(image)
    # image.save('output.jpg', 'JPEG')
    return np.array(image)

@app.route('/', methods=['POST'])
def process_image():
    data = request.get_json()
    # image = data['image'].split(',')[1]
    image = data['image']
    image = base64_to_image(image)
    image = imgutils.crop_squared_and_reshape(image, (32, 32))
    image = image.astype(np.float32)[np.newaxis, ...]
    print(image.shape)
    res = mcf(image).numpy()[0].argmax()
    print(res)
    return jsonify({'message': classnames[res]}) 

@app.route('/', methods=['GET'])
def test_get():
    return jsonify({'message': 'si hizo pa!'}) 

if __name__ == '__main__':
    app.run(host=obtener_direccion_ip(), debug=True, port=9000)
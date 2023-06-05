from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
from PIL import Image
import io
import socket
# inbound rule to port 9000 on TCP


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
    image.save('output.jpg', 'JPEG')
    return np.array(image)

@app.route('/', methods=['POST'])
def process_image():
    data = request.get_json()
    # image = data['image'].split(',')[1]
    image = data['image']
    image = base64_to_image(image)

    print(image.shape)

    return jsonify({'message': 'aqui se muestra el resultado de reconocimiento'}) 

@app.route('/', methods=['GET'])
def test_get():
    return jsonify({'message': 'si hizo pa!'}) 

if __name__ == '__main__':
    app.run(host=obtener_direccion_ip(), debug=True, port=9000)
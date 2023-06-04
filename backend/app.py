from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
from PIL import Image
import io

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

    return jsonify({'objects_detected': 'si'}) 

if __name__ == '__main__':
    app.run(debug=True, port=9000)
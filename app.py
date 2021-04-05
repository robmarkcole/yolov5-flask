import argparse
import io
import os
import json
from PIL import Image

import torch
from flask import Flask, jsonify, url_for, render_template, request, redirect

app = Flask(__name__)

RESULT_FOLDER = os.path.join('static')
app.config['RESULT_FOLDER'] = RESULT_FOLDER

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, force_reload=True).autoshape()  # for PIL/cv2/np inputs and NMS
model.eval()

def get_prediction(img_bytes):
    img = Image.open(io.BytesIO(img_bytes))
    results = model(img, size=640)  # includes NMS
    return results

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if not file:
            return

        img_bytes = file.read()
        results = get_prediction(img_bytes)
        results.print()
        results.save()  # save as results1.jpg, results2.jpg... etc.
        os.rename("results0.jpg", "static/results0.jpg")

        full_filename = os.path.join(app.config['RESULT_FOLDER'], 'results0.jpg')
        return redirect('static/results0.jpg')
    return render_template('index.html')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()
    app.run(host="0.0.0.0", debug=True, port=args.port)
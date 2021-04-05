import argparse
import io
import os
import json
from PIL import Image

import torch
from flask import Flask, jsonify, url_for, render_template, request, redirect

app = Flask(__name__)

model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True).autoshape()
model.eval()


@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return

        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        img.save("/tmp/tmp.jpg")

        # Reopen
        img = Image.open("/tmp/tmp.jpg")
        results = model(img, size=640)

        results.display(save=True, save_dir="static")
        return redirect("static/tmp.jpg")

    return render_template("index.html")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()
    app.run(host="0.0.0.0", debug=True, port=args.port)

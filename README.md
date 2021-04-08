# deploy a yolov5 model using pytorch + flask
This repo contains example apps for exposing [yolo5](https://github.com/ultralytics/yolov5) models via a [flask](https://flask.palletsprojects.com/en/1.1.x/) api/app.

## Web app
Simple app consisting of a form where you can upload an image, and see the inference result of the model in the browser. Run:

`$ python3 app.py --port 5000`

then visit http://localhost:5000/ in your browser

<p align="center">
<img src="https://github.com/robmarkcole/yolov5-flask/blob/master/docs/app_form.jpg" width="350">
</p>

<p align="center">
<img src="https://github.com/robmarkcole/yolov5-flask/blob/master/docs/app_result.jpg" width="350">
</p>

## Run & Develop locally
Run locally and dev:
* `python3 -m venv venv`
* `source venv/bin/activate`
* `(venv) $ pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt`
* `(venv) $ pip install -r requirements.txt`
* `(venv) $ python3 app.py --port 5000`

## docker - WIP
work in progress
```
# Build
docker build -t yolov5-flask .
# Run
docker run -p 5000:5000 yolov5-flask:latest
```

## reference
- https://github.com/ultralytics/yolov5
- [Load YOLOv5 from PyTorch Hub ](https://github.com/ultralytics/yolov5/issues/36)
- https://github.com/avinassh/pytorch-flask-api-heroku

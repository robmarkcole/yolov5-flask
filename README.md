# Yolov5 object detection model deployment using flask
This repo contains example apps for exposing the [yolo5](https://github.com/ultralytics/yolov5) object detection model from [pytorch hub](https://pytorch.org/hub/ultralytics_yolov5/) via a [flask](https://flask.palletsprojects.com/en/1.1.x/) api/app.

## Web app
Simple app consisting of a form where you can upload an image, and see the inference result of the model in the browser. Run:

`$ python3 webapp.py --port 5000`

then visit http://localhost:5000/ in your browser:

<p align="center">
<img src="https://github.com/robmarkcole/yolov5-flask/blob/master/docs/app_form.jpg" width="450">
</p>

<p align="center">
<img src="https://github.com/robmarkcole/yolov5-flask/blob/master/docs/app_result.jpg" width="450">
</p>

## Rest API
Simple rest API exposing the model for consumption by another service. Run:

`$ python3 restapi.py --port 5000`

Then use [curl](https://curl.se/) to perform a request:

`$ curl -X POST -F image=@tests/zidane.jpg 'http://localhost:5000/v1/object-detection/yolov5s'`

The model inference results are returned:

```
[{'class': 0,
  'confidence': 0.8197850585,
  'name': 'person',
  'xmax': 1159.1403808594,
  'xmin': 750.912902832,
  'ymax': 711.2583007812,
  'ymin': 44.0350036621},
 {'class': 0,
  'confidence': 0.5667674541,
  'name': 'person',
  'xmax': 1065.5523681641,
  'xmin': 116.0448303223,
  'ymax': 713.8904418945,
  'ymin': 198.4603881836},
 {'class': 27,
  'confidence': 0.5661227107,
  'name': 'tie',
  'xmax': 516.7975463867,
  'xmin': 416.6880187988,
  'ymax': 717.0524902344,
  'ymin': 429.2020568848}]
```

An example python script to perform inference using [requests](https://docs.python-requests.org/en/master/) is given in `tests/test_request.py`

## Run & Develop locally
Run locally and dev:
* `python3 -m venv venv`
* `source venv/bin/activate`
* `(venv) $ pip install -r requirements.txt`
* `(venv) $ python3 webapp.py --port 5000`

## Docker
The example dockerfile shows how to expose the rest API:
```
# Build
docker build -t yolov5-flask .
# Run
docker run -p 5000:5000 yolov5-flask:latest
```

## reference
- https://github.com/ultralytics/yolov5
- https://github.com/jzhang533/yolov5-flask (this repo was forked from here)
- https://github.com/avinassh/pytorch-flask-api-heroku

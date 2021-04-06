# deploy a yolov5 model using pytorch + flask
Run locally and dev:
* `python3 -m venv venv`
* `source venv/bin/activate`
* `(venv) $ pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt`
* `(venv) $ pip install -r requirements.txt`
* `(venv) $ python3 app.py --port 5000`

then, visit http://localhost:5000/ in your browser

## docker
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

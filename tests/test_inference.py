import cv2
import torch
from PIL import Image

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Images
for f in ['zidane.jpg']:  # download 2 images, 'bus.jpg'
    print(f'Downloading {f}...')
    torch.hub.download_url_to_file('https://github.com/ultralytics/yolov5/releases/download/v1.0/' + f, f)

img1 = Image.open('zidane.jpg')  # PIL image

results = model(img1, size=640)  # includes NMS

# Results
results.print()  
# print(results.tolist())

# Data
# print(results.xyxy[0])  # print img1 predictions (pixels)
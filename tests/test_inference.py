import io
import torch
from PIL import Image

# Model
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, force_reload=True)

# img = Image.open("zidane.jpg")  # PIL image, succeeds

# Reading bytes fails
with open("zidane.jpg", "rb") as file:
    img_bytes = file.read()
img = Image.open(io.BytesIO(img_bytes))

print(img.size) # validate image
results = model(img, size=640)  # includes NMS
results.print()

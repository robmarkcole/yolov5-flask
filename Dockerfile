FROM python:3.8-slim-buster

WORKDIR /app

COPY src/requirements.txt requirements.txt

COPY src/ .

COPY weights/ ./weights

EXPOSE 5000
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
CMD ["python", "restapi.py", "--port=8000"]
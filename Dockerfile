FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir flask pillow torch torchvision

COPY app.py .
COPY resnet18_cifar10.pth .

EXPOSE 5000

CMD ["python", "app.py"]
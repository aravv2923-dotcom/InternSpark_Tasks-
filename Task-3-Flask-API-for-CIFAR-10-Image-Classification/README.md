# Task 3: Flask API for CIFAR-10 Image Classification

## Overview

This project wraps a trained ResNet18 model for CIFAR-10 image classification using a Flask API. The API accepts an image and returns the predicted CIFAR-10 class.

The project also includes a Dockerfile for containerizing the Flask application.

## Project Structure

```text
Task-3-Flask-API/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── resnet18_cifar10.pth
```

## Technologies Used

* Python
* Flask
* PyTorch
* Torchvision
* Docker
* ResNet18
* CIFAR-10

## Installation

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

## Running the Flask API

Start the Flask application with:

```bash
python app.py
```

The API will run locally on:

```text
http://127.0.0.1:5000
```

## API Endpoint

### POST `/predict`

The `/predict` endpoint accepts an image file and returns the predicted CIFAR-10 class.

### Example Request

Send a `POST` request to:

```text
http://127.0.0.1:5000/predict
```

Attach an image using the form-data field:

```text
image
```

### Example Response

```json
{
    "class": "cat",
    "class_id": 3
}
```

The exact response should match the output produced by the current `app.py`.

## CIFAR-10 Classes

The model predicts one of the following classes:

```text
airplane
automobile
bird
cat
deer
dog
frog
horse
ship
truck
```

## Docker

Build the Docker image using:

```bash
docker build -t cifar10-flask-api .
```

Run the container using:

```bash
docker run -p 5000:5000 cifar10-flask-api
```

The API can then be accessed at:

```text
http://127.0.0.1:5000
```

## Model

The application uses the trained:

```text
resnet18_cifar10.pth
```

model for CIFAR-10 image classification.

## Task Requirements Completed

* Trained CIFAR-10 image classification model
* Flask API for model inference
* `/predict` endpoint
* Dockerfile for containerization
* Requirements file
* Example API request and response
* Project Documentation

from flask import Flask, request, jsonify
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

app = Flask(__name__)

# CIFAR-10 class names
classes = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]

# Create the same ResNet18 architecture used in Task 2
model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, 10)

# Load trained model
model.load_state_dict(
    torch.load("resnet18_cifar10.pth", map_location=torch.device("cpu"))
)

model.eval()

# Image preprocessing used for inference
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.4914, 0.4822, 0.4465],
        std=[0.2470, 0.2435, 0.2616]
    )
])


@app.route("/")
def home():
    return jsonify({
        "message": "CIFAR-10 Image Classification API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({
            "error": "No image file provided"
        }), 400

    image_file = request.files["image"]

    try:
        image = Image.open(image_file).convert("RGB")
        image = transform(image)
        image = image.unsqueeze(0)

        with torch.no_grad():
            output = model(image)
            probabilities = torch.softmax(output, dim=1)

        confidence, predicted_class = torch.max(probabilities, 1)

        prediction = classes[predicted_class.item()]
        confidence_value = confidence.item()

        return jsonify({
            "prediction": prediction,
            "confidence": round(confidence_value, 4)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

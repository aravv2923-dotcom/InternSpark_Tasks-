# Task 2 - Deep Learning Image Classification

## Overview

This project implements an image classification model using PyTorch and a pretrained ResNet18 model.

The CIFAR-10 dataset is used for classification, with data augmentation and transfer learning.

## Technologies Used

- Python
- PyTorch
- Torchvision
- Scikit-learn
- Matplotlib

## Model

- Pretrained ResNet18
- Transfer learning
- 10 CIFAR-10 classes
- 2 training epochs

## Dataset

A subset of the CIFAR-10 dataset was used:

- Training images: 5,000
- Testing images: 1,000

Data augmentation:
- Random horizontal flip
- Random rotation

## Results

- Test Accuracy: 73.30%
- Precision: 0.74
- Recall: 0.73
- F1-score: 0.73

## Deliverables

- Training notebook: `Task2_Deep_Learning.ipynb`
- Saved model: `resnet18_cifar10.pth`
- Training and test curves
- Confusion matrix
- Evaluation metrics
- Inference code

## Inference

The saved model can be used with the `predict_image()` function in the notebook.

Example:

```python
predict_image("path/to/your/image.jpg")
```


## Trained Model

Download the trained weights here: [resnet18_cifar10.pth](https://drive.google.com/file/d/1ChgtKDI24C9TJ1Kzq99j1beeAUvaPij5/view?usp=sharing)

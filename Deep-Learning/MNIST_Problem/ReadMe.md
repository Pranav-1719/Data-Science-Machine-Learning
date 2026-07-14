# MNIST Handwritten Digit Classification

## Project Overview

This project develops a Deep Learning model for handwritten digit recognition using the MNIST dataset. The objective is to classify grayscale images of handwritten digits (0–9) with high accuracy using a Neural Network built with TensorFlow and Keras.

The project demonstrates the complete deep learning workflow, including data preprocessing, dataset splitting, model development, training, validation, and evaluation.

---

## Project Structure

```text
MNIST_Handwritten_Digit_Classification/
│
├── MNIST_Classification.ipynb
├── ReadMe.md
│
└── Model Assets (Generated During Training)
```

---

## Dataset

The project uses the MNIST dataset provided through TensorFlow Datasets.

### Dataset Characteristics

* 70,000 handwritten digit images
* 28 × 28 grayscale images
* 10 classes (Digits 0–9)
* 60,000 training samples
* 10,000 testing samples

Each image contains a handwritten digit that must be classified into its corresponding numerical category.

---

## Data Preprocessing

### Data Loading

The dataset is loaded directly using TensorFlow Datasets:

```python
mnist_dataset, mnist_info = tfds.load(
    name='MNIST',
    with_info=True,
    as_supervised=True
)
```

### Normalization

Pixel values are scaled from:

```text
0 - 255
```

to

```text
0 - 1
```

using:

```python
image = tf.cast(image, tf.float32)
image /= 255.
```

### Dataset Split

| Dataset    | Percentage    |
| ---------- | ------------- |
| Training   | 90%           |
| Validation | 10%           |
| Test       | 10,000 Images |

### Batch Processing

```text
Batch Size = 100
Buffer Size = 10,000
```

Data is shuffled before training to improve model generalization.

---

## Model Architecture

The Neural Network consists of:

| Layer          | Configuration         |
| -------------- | --------------------- |
| Input Layer    | Flatten (28 × 28 × 1) |
| Hidden Layer 1 | 50 Neurons, ReLU      |
| Hidden Layer 2 | 50 Neurons, ReLU      |
| Hidden Layer 3 | 50 Neurons, ReLU      |
| Output Layer   | 10 Neurons, Softmax   |

### Model Definition

```python
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28,1)),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
```

---

## Training Configuration

| Parameter      | Value                           |
| -------------- | ------------------------------- |
| Optimizer      | Adam                            |
| Loss Function  | Sparse Categorical Crossentropy |
| Metric         | Accuracy                        |
| Epochs         | 15                              |
| Early Stopping | Patience = 3                    |
| Batch Size     | 100                             |

### Training Features

* Mini-batch Gradient Descent
* Early Stopping to prevent overfitting
* Validation Monitoring
* Automatic Optimization using Adam

---

## Technologies Used

* Python
* NumPy
* TensorFlow
* Keras
* TensorFlow Datasets (TFDS)
* Jupyter Notebook

---

## Deep Learning Workflow

1. Load MNIST Dataset
2. Normalize Pixel Values
3. Split Training and Validation Data
4. Shuffle Dataset
5. Create Mini-batches
6. Build Neural Network
7. Train Model
8. Validate Performance
9. Evaluate on Test Dataset
10. Generate Predictions

---

## Business & Practical Applications

Handwritten digit recognition is widely used in:

* Postal Code Recognition
* Bank Check Processing
* Document Digitization
* Form Automation
* OCR (Optical Character Recognition)
* Automated Data Entry Systems

---

## Results

The Neural Network successfully learns handwritten digit patterns and classifies images into one of ten digit classes.

The model demonstrates:

* High classification accuracy
* Effective feature extraction through dense neural layers
* Strong generalization on unseen test data

---

## Skills Demonstrated

* Deep Learning
* Neural Networks
* Image Classification
* TensorFlow/Keras
* Data Preprocessing
* Computer Vision Fundamentals
* Model Evaluation
* Early Stopping
* Batch Processing
* Predictive Modeling

---

## Author

Pranav Sankpal

Computer Science Student | Data Science | Machine Learning | Deep Learning

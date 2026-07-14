# Audiobooks Business Case

## Project Overview

This project uses Deep Learning to predict whether an audiobook customer is likely to make a repeat purchase. By analyzing customer purchase history and engagement metrics, the model helps businesses identify valuable customers and improve retention strategies.

A fully connected Neural Network was built using TensorFlow/Keras, with data preprocessing, feature scaling, dataset balancing, and model evaluation performed to maximize predictive performance.

---

## Project Structure

```text
Audiobooks_Business_Case/
│
├── Audiobooks_Preprocessing.ipynb
├── Audiobooks_Machine_Learning.ipynb
│
├── Audiobooks_data.csv
├── Audiobooks_data_train.npz
├── Audiobooks_data_validation.npz
├── Audiobooks_data_test.npz
│
└── ReadMe.md
```

---

## Files Description

### `Audiobooks_Preprocessing.ipynb`

* Cleans and preprocesses the raw audiobook dataset
* Balances target classes
* Standardizes input features
* Splits data into Training, Validation, and Test sets
* Saves processed datasets as `.npz` files

### `Audiobooks_Machine_Learning.ipynb`

* Loads preprocessed datasets
* Builds and trains a Neural Network using TensorFlow/Keras
* Applies Early Stopping to prevent overfitting
* Evaluates model performance on unseen test data

### `Audiobooks_data.csv`

Raw audiobook customer dataset.

### `Audiobooks_data_train.npz`

Training dataset used for model learning.

### `Audiobooks_data_validation.npz`

Validation dataset used during training and hyperparameter tuning.

### `Audiobooks_data_test.npz`

Test dataset used to evaluate final model performance.

---

## Model Architecture

The Neural Network consists of:

* Input Layer (10 Features)
* Hidden Layer 1 – 100 Neurons (ReLU)
* Hidden Layer 2 – 100 Neurons (ReLU)
* Output Layer – 2 Neurons (Softmax)

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])
```

### Training Configuration

| Parameter      | Value                           |
| -------------- | ------------------------------- |
| Optimizer      | Adam                            |
| Learning Rate  | 0.001                           |
| Loss Function  | Sparse Categorical Crossentropy |
| Batch Size     | 100                             |
| Epochs         | 100                             |
| Early Stopping | Patience = 3                    |

---

## Technologies Used

* Python
* NumPy
* TensorFlow
* Keras
* Scikit-learn
* Jupyter Notebook

---

## Deep Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Scaling
4. Dataset Balancing
5. Train-Validation-Test Split
6. Neural Network Development
7. Model Training
8. Validation & Early Stopping
9. Model Evaluation
10. Customer Purchase Prediction

---

## Business Objective

The objective is to predict whether a customer will purchase audiobooks again, allowing businesses to:

* Improve customer retention
* Optimize marketing campaigns
* Identify high-value customers
* Increase customer lifetime value
* Support data-driven decision making

---

## How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install numpy tensorflow scikit-learn jupyter
```

3. Run the notebooks in order

```text
1. Audiobooks_Preprocessing.ipynb
2. Audiobooks_Machine_Learning.ipynb
```

4. The preprocessing notebook generates:

```text
Audiobooks_data_train.npz
Audiobooks_data_validation.npz
Audiobooks_data_test.npz
```

5. Train and evaluate the model using the generated datasets.

---

## Results

The Neural Network successfully classifies customers into repeat-purchase and non-repeat-purchase categories. The model leverages customer behavioral data to generate actionable insights that can improve marketing effectiveness and customer retention.

---

## Skills Demonstrated

* Data Preprocessing
* Feature Scaling
* Dataset Balancing
* Deep Learning
* Neural Networks
* TensorFlow/Keras
* Model Evaluation
* Classification
* Predictive Analytics

---

## Author

Pranav Sankpal

Computer Science Student | Data Science | Machine Learning | Deep Learning

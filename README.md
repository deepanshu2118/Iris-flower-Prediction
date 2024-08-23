# Iris-flower-Prediction

This repository contains the implementation of a machine learning model to classify iris flowers into three species: *Iris-setosa*, *Iris-versicolor*, and *Iris-virginica*. The classification is performed using the famous Iris dataset.

## Dataset

The Iris dataset consists of 150 samples with the following features:

- **Sepal Length**
- **Sepal Width**
- **Petal Length**
- **Petal Width**

Each sample belongs to one of the following three classes:

1. *Iris-setosa*
2. *Iris-versicolor*
3. *Iris-virginica*

## Project Structure

- `iris_data.csv`: The dataset file.
- `iris_model.ipynb`: Jupyter notebook containing the code for data exploration, model training, and evaluation.
- `requirements.txt`: A file listing all the Python libraries required to run the project.
- `model.pkl`: Serialized model for future predictions.
- `README.md`: Project documentation (this file).

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/iris-classification.git
   cd iris-classification

2. Create and activate a virtual environment
   python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required packages
   pip install -r requirements.txt


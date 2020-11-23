import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf

print("Loading dataset")
dataset = pd.read_csv("data/houses.csv")
train_dataset = dataset
# Move labels to seperate vector
X = train_dataset.copy()
y = X.pop("price")
# Normalize data
X_change = [X.mean(), X.std()]
y_change = [y.mean(), y.std()]
X = (X-X.mean())/X.std()
y = (y-y.mean())/y.std()

sizes = []
import csv
with open("data/houses.csv", "r") as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if row[0] == "beds":
            continue
        sizes.append(int(row[3]))

print("Loading model")
model = tf.keras.models.load_model("model.h5")

with open("normal_vals", "r") as file:
    data = file.read()
    y_normal_vals = [float(i) for i in data.split("\n")[:2]]
    X_normal_vals = [x.split(" ") for x in data.split("\n")[2:]]
    X_normal_vals.pop()
    for i, _ in enumerate(X_normal_vals):
        X_normal_vals[i].pop()
        X_normal_vals[i] = [float(ele) for ele in X_normal_vals[i]]

prediction = model(np.array(X)).numpy() * y_normal_vals[1] + y_normal_vals[0]
plt.scatter(sizes, prediction.flatten(), c="b", marker="o", label="Predicted")
plt.scatter(sizes, y * y_normal_vals[1] + y_normal_vals[0], c='r', marker='s', label='Actual')
plt.legend(loc='lower right')
plt.title('Housing Prices')
plt.xlabel("Size (sqft)")
plt.ylabel("Price ($)")
plt.show()

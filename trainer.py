import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf
from tensorflow import keras


def train(data_location, max_iter):
    print("Loading dataset to train")
    dataset = pd.read_csv(data_location)

    # Create training and testing datasets
    train_dataset = dataset.sample(frac=0.8, random_state=0)
    test_dataset = dataset.drop(train_dataset.index)

    # Move labels to seperate vector
    X = train_dataset.copy()
    y = X.pop("price")
    X_val = test_dataset.copy()
    y_val = X_val.pop("price")

    # Normalize data
    X_change = [X.mean(), X.std()]
    y_change = [y.mean(), y.std()]
    X = (X-X.mean())/X.std()
    y = (y-y.mean())/y.std()
    X_val = (X_val-X.mean())/X.std()
    y_val = (y_val-y.mean())/y.std()

    
    if (os.path.isfile(os.getcwd() + "/model.h5")):
        print("Loading model")
        model = keras.models.load_model("model.h5")
    else:
        print("Creating new model")
        model = keras.models.Sequential([
            keras.layers.Dense(32, input_shape=(4,), activation="relu"),
            keras.layers.Dense(32, activation="relu"),
            keras.layers.Dense(1)
        ])

        model.compile(optimizer='RMSprop',
                    loss="mse",
                    metrics=["mse", "mae"])

    print("Training model")
    # TODO graph training and cross-val error
    model.fit(X, y, epochs=max_iter)

    model.save("model.h5")
    # Write the normalization vals to file so that another file can predict using them
    with open("normal_vals", "w") as file:
        file.write(str(y_change[0]) + "\n" + str(y_change[1]) + "\n")
        for i in np.array(X_change):
            for j in i:
                file.write(str(j) + " ")
            file.write("\n")
    print("Model saved to disk")

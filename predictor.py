import os
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf

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

cont = True
while (cont):
    beds = (int(input("Number of beds: ")) -
            X_normal_vals[0][0]) / X_normal_vals[1][0]
    baths_full = (int(input("Number of full-baths: ")) -
                  X_normal_vals[0][1]) / X_normal_vals[1][1]
    baths_half = (int(input("Number of half-baths: ")) -
                  X_normal_vals[0][2]) / X_normal_vals[1][2]
    building_size = (int(input("Building size (sqft): ")) -
                     X_normal_vals[0][3]) / X_normal_vals[1][3]
    user_input = np.array([[beds, baths_full, baths_half, building_size]])

    prediction = model(user_input).numpy() * y_normal_vals[1] + y_normal_vals[0]
    print(prediction.flatten())

    cont = input("Predict again? (y/N): ").lower() in ["y", "yes"]

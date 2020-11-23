import matplotlib.pyplot as plt
import csv


def plot_price_vs_size(file_name):
    x = []
    y = []

    print("Reading input file")
    with open(file_name, "r") as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            if row[0] == "beds":
                continue
            x.append(int(row[3]))
            y.append(int(row[4]))

    print("Plotting")
    plt.scatter(x, y, marker='o')

    plt.title('Housing Prices')

    plt.xlabel("Size (sqft)")
    plt.ylabel("Price ($)")

    plt.show()

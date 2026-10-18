
import numpy as np

def plot_data(X, y, ax):
    y = np.asarray(y).reshape(-1)

    ax.scatter(
        X[y == 0, 0],
        X[y == 0, 1],
        marker="x",
        color="red",
        label="y=0"
    )

    ax.scatter(
        X[y == 1, 0],
        X[y == 1, 1],
        marker="o",
        color="blue",
        label="y=1"
    )

    ax.legend()

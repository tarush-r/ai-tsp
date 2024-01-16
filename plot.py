import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("times.csv")
    df["branchAndBound"] /= 10**3
    df["sls"] /= 10**3

    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "sans-serif"
    })

    fig, ax = plt.subplots(1, 1)

    mask = df["bruteForce"] != 0
    ax.plot(df.loc[mask, "n"], df.loc[mask, "bruteForce"], c="b", marker=".", alpha=0.75, label="Brute force")
    ax.plot(df["n"], df["branchAndBound"], c="r", marker=".", alpha=0.75, label="B\&B")
    ax.plot(df["n"], df["sls"], c="g", marker=".", alpha=0.75, label="SLS")

    ax.set_xlabel("n")
    ax.set_ylabel("Time (s)")
    ax.set_yscale("log")

    fig.legend()

    plt.show()

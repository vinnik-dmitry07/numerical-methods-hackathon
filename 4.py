import matplotlib.pyplot as plt
import numpy as np


def main():
    h = 0.001
    tpoints = np.arange(0, 30, h)
    xpoints, ypoints = [], []
    r = np.array([0.1, 0.1], float)
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        r += rk4(r, t, h)
    plt.plot(tpoints, xpoints)
    plt.plot(tpoints, ypoints)
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.show()


def rk4(r, t, h):
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    return (k1 + 2 * k2 + 2 * k3 + k4) / 6


def f(r, t):
    #         alpha = 4.0
    #         beta = 2.5
    #         gamma = 2.0
    #         sigma = 1.0
    alpha = 2.0
    beta = 0.5
    gamma = 0.5
    sigma = 1.0
    x, y = r[0], r[1]
    dxdt = x * (alpha - beta * y)
    dydt = -y * (gamma - sigma * x)
    return np.array([dxdt, dydt], float)


if __name__ == "__main__":
    main()

import numpy as np
import matplotlib.pyplot as plt
from random import randint


def func(x, y):
    return (10 * x * y) / np.exp(x**2 + 0.5 * x + y**2)


def gradient(x, y):
    return (-20 * x**2 - 5 * x + 10) * y / (
        np.exp(x**2 + 0.5 * x + y**2)
    ), -10 * x * (2 * y**2 - 1) / (np.exp(+(x**2) + 0.5 * x + y**2))


LEARNING_RATE = 0.1
x_pos = 10
y_pos = 10
start_point = (x_pos, y_pos, func(x_pos, y_pos))
current_pos = start_point
y_delta = 1
x_delta = 1
i = 0

while (y_delta > 0.00001 or x_delta > 0.00001) and i < 1000000:
    x_derivative, y_derivative = gradient(current_pos[0], current_pos[1])
    x_new = current_pos[0] + LEARNING_RATE * x_derivative
    y_new = current_pos[1] + LEARNING_RATE * y_derivative
    y_delta = abs(current_pos[1] - y_new)
    x_delta = abs(current_pos[0] - x_new)
    current_pos = (x_new, y_new, func(x_new, y_new))
    i += 1
    
print(current_pos)
# plots
x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)
X, Y = np.meshgrid(x, y)
Z = func(X, Y)
ax = plt.subplot(projection="3d", computed_zorder=False)
ax.plot_surface(X, Y, Z, cmap="viridis", zorder=0)
ax.scatter(current_pos[0], current_pos[1], current_pos[2], color="red", zorder=1)
ax.scatter(start_point[0], start_point[1], start_point[2], color="black", zorder=1)
plt.show()

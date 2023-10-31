import random
import numpy as np
import matplotlib.pyplot as plt
import math


def func(x, y):
    return (10 * x * y) / np.exp(x**2 + 0.5 * x + y**2)


def initializePopulation(n):
    return np.array(
        [
            [random.randint(-200, 200) / 100, random.randint(-200, 200) / 100]
            for i in range(n)
        ]
    )


def mutate(population):
    mutation = 0.13 * np.random.normal(0, 1, (len(population), 2))
    prob = np.tile(np.random.uniform(0, 1, (len(population), 1)), (1, 2))
    population = population + mutation * (prob > 0.9)
    return population


def value_list(population):
    vectorized_func = np.vectorize(func)
    v_list = vectorized_func(population[:, 0], population[:, 1])
    return v_list


def select_max(population, n):
    v_list = value_list(population)
    min_value = min(v_list)
    v_list = v_list - min_value
    v_sum = sum(v_list)
    weights = v_list / v_sum
    population = np.array(random.choices(population, weights, k=n))
    return population


def select_min(population, n):
    v_list = value_list(population)
    max_value = max(v_list)
    v_list = -(v_list - max_value)
    v_sum = sum(v_list)
    weights = v_list / v_sum
    population = np.array(random.choices(population, weights, k=n))
    return population


def calc_weights_max(population):
    v_list = value_list(population)
    min_value = min(v_list)
    v_list = v_list - min_value
    v_sum = sum(v_list)
    weights = v_list / v_sum
    return weights


def calc_weights_min(population):
    v_list = value_list(population)
    max_value = max(v_list)
    v_list = -(v_list - max_value)
    v_sum = sum(v_list)
    weights = v_list / v_sum
    return weights


def crossover(parents):
    children = []
    for num in range(len(parents)):
        if num % 2 == 1:
            a = random.random()
            if a == 0 or a == 1:
                a = 0.1
            children.append(parents[num - 1] * a + parents[num] * (1 - a))
    return np.array(children)


population = initializePopulation(40)
x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)
X, Y = np.meshgrid(x, y)
Z = func(X, Y)
ax = plt.subplot(projection="3d", computed_zorder=False)
ax.plot_surface(X, Y, Z, cmap="viridis", zorder=0)

for obj in population:
    ax.scatter(obj[0], obj[1], func(obj[0], obj[1]), color="black", zorder=1)


def has_duplicates(arr):
    unique_arrays = set()
    for sub_array in arr:
        if tuple(sub_array) in unique_arrays:
            print(tuple(sub_array))
            return True
        unique_arrays.add(tuple(sub_array))
    return False


average_old = 10000
average_delta = 1
i = 0
while average_delta > 0.00001 and i < 1:
    average_new = np.mean(value_list(population))
    average_delta = abs(average_new - average_old)
    average_old = average_new
    i += 1
    parents = select_max(population, 80)
    children = crossover(parents)
    children = mutate(children)

    population = np.concatenate((population, children), axis=0)
    print("=========================================================")
    if has_duplicates(population):

    population = select_max(population, 40)
    if has_duplicates(population):



print(i)
for obj in population:
    ax.scatter(obj[0], obj[1], func(obj[0], obj[1]), color="red", zorder=1)

plt.show()

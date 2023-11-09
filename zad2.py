import random
import numpy as np
import matplotlib.pyplot as plt


def func(x, y):
    return (10 * x * y) / np.exp(x**2 + 0.5 * x + y**2)


def initialize_population(n):
    return np.array([[0, 0] for i in range(n)])


def mutate(population):
    mutation = 0.23 * np.random.normal(0, 1, (len(population), 2))
    prob = np.tile(np.random.uniform(0, 1, (len(population), 1)), (1, 2))
    population = population + mutation * (prob > 0.8)
    return population


def value_list(population):
    vectorized_func = np.vectorize(func)
    v_list = vectorized_func(population[:, 0], population[:, 1])
    return v_list


def calc_weights_max(population):
    v_list = value_list(population)
    min_value = min(v_list)
    v_list = v_list - min_value + 0.000001
    v_sum = sum(v_list)
    weights = v_list / v_sum
    return weights


def calc_weights_min(population):
    v_list = value_list(population)
    max_value = max(v_list)
    v_list = -(v_list - max_value - 0.000001)
    v_sum = sum(v_list)
    weights = v_list / v_sum
    return weights


def crossover(parents):
    children = []
    for num in range(len(parents)):
        if num % 2 == 1:
            a = random.random()
            children.append(parents[num - 1] * a + parents[num] * (1 - a))
    return np.array(children)


def main(mu, lamb, mode, max_index):
    population = initialize_population(mu)

    x = np.arange(-5, 5, 0.01)
    y = np.arange(-5, 5, 0.01)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)
    ax = plt.subplot(projection="3d", computed_zorder=False)
    ax.plot_surface(X, Y, Z, cmap="viridis", zorder=0)
    for obj in population:
        ax.scatter(obj[0], obj[1], func(obj[0], obj[1]), color="black", zorder=1)

    i = 0
    while i < max_index:
        i += 1
        if mode:
            weights = calc_weights_max(population)
        else:
            weights = calc_weights_min(population)

        parents = np.array(random.choices(population, weights, k=int(lamb * 2)))
        children = crossover(parents)
        children = mutate(children)
        population = np.concatenate((population, children), axis=0)
        v_list = value_list(population)
        sorted_indices = np.argsort(v_list)
        if mode:
            sorted_population = population[sorted_indices[::-1]]
        else:
            sorted_population = population[sorted_indices]

        population = sorted_population[:mu]

    point = population[0]
    point = (round(point[0], 3), round(point[1], 3), round(func(point[0], point[1]), 5))

    print(point)

    for obj in population:
        ax.scatter(obj[0], obj[1], func(obj[0], obj[1]), color="red", zorder=1)
    ax.scatter(point[0], point[1], func(point[0], point[1]), color="yellow", zorder=1)

    plt.show()


if __name__ == "__main__":
    # arg1 - parent population
    # arg2 - children population
    # arg3 - mode: 1=maximum, 0=minimum
    # arg4 - number of iterations
    main(128, 512, 0, 100)

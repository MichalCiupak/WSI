import pickle
from pprint import pprint
import numpy as np

"""Implement your model, training code and other utilities here. Please note, you can generate multiple 
pickled data files and merge them into a single data list."""


def load_data(file_name):
    with open(file_name, "rb") as f:
        loaded_data = pickle.load(f)
    return loaded_data


def is_food_this_direction(food, head):
    d1 = 1 if food[1] < head[1] else 0
    d2 = 1 if food[0] > head[0] else 0
    d3 = 1 if food[1] > head[1] else 0
    d4 = 1 if food[0] < head[0] else 0
    return np.array([d1, d2, d3, d4])


def is_obstacle_this_direction(body, b_s, bounds):
    head = body[-1]
    obstacles = np.array([0, 0, 0, 0])
    print(obstacles)
    for segment in body:
        if head[1] - b_s == segment[1] or head[1] == 0:
            obstacles[0] = 1
        if head[0] + b_s == segment[0] or head[0] + b_s == bounds[0]:
            obstacles[1] = 1
        if head[1] + b_s == segment[1] or head[1] + b_s == bounds[1]:
            obstacles[2] = 1
        if head[0] - b_s == segment[0] or head[0] == 0:
            obstacles[3] = 1
    return obstacles


def data_converter():
    loaded_data = load_data("snakerun1.pickle")
    bounds = loaded_data["bounds"]
    block_size = loaded_data["block_size"]
    data = loaded_data["data"]
    input_features = []
    for data_set in data:
        print(data_set)
        input_features = np.array([])
        food = data_set[0]["food"]
        body = data_set[0]["snake_body"]
        head = body[-1]
        input_features = np.concatenate(
            (input_features, is_food_this_direction(food, head))
        )
        print(food)
        print(head)
        print(input_features)
        input_features = np.concatenate(
            (input_features, is_obstacle_this_direction(body, block_size, bounds))
        )
        print(input_features)
        break


if __name__ == "__main__":
    data_converter()
    """Example of how to read a pickled file, feel free to remove this"""
    # with open(f"data/2022-11-14_12:52:37.pickle", "rb") as f:
    #     data_file = pickle.load(f)
    # print(data_file["block_size"])
    # print(data_file["bounds"])
    # print(data_file["data"])


# pprint(load_data("snakerun1.pickle"))

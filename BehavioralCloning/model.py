import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from snake import Direction
from pprint import pprint

"""Implement your model, training code and other utilities here. Please note, you can generate multiple 
pickled data files and merge them into a single data list."""

direction_to_label = {
    Direction.UP: 0,
    Direction.RIGHT: 1,
    Direction.DOWN: 2,
    Direction.LEFT: 3,
}


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


def is_obstacle_this_direction(body, direction, b_s, bounds):
    head = body[-1]
    body = body[:-1]
    obstacles = np.array([0, 0, 0, 0, direction])
    for segment in body:
        if head[1] - b_s == segment[1] and head[0] == segment[0] or head[1] == 0:
            obstacles[0] = 1
        if (
            head[0] + b_s == segment[0]
            and head[1] == segment[1]
            or head[0] + b_s == bounds[0]
        ):
            obstacles[1] = 1
        if (
            head[1] + b_s == segment[1]
            and head[0] == segment[0]
            or head[1] + b_s == bounds[1]
        ):
            obstacles[2] = 1
        if head[0] - b_s == segment[0] and head[1] == segment[1] or head[0] == 0:
            obstacles[3] = 1
    return np.array(obstacles)


def game_state_to_data_sample(game_state, bounds, block_size):
    input_features = np.array([])
    food = game_state["food"]
    body = game_state["snake_body"]
    direction = direction_to_label[game_state["snake_direction"]]
    head = body[-1]
    input_features = np.concatenate(
        (input_features, is_food_this_direction(food, head))
    )

    input_features = np.concatenate(
        (
            input_features,
            is_obstacle_this_direction(body, direction, block_size, bounds),
        )
    )
    return input_features


def clear_data(data):
    leng = 0
    prevlen = 0
    indexr = []
    for num, elem in enumerate(data):
        leng = len(elem[0]["snake_body"])
        if leng < prevlen:
            indexr.append(num - 1)
        prevlen = leng
    data = [value for index, value in enumerate(data) if index not in indexr]
    return data


def data_converter():
    loaded_data1 = load_data("snakerun5.pickle")
    bounds = loaded_data1["bounds"]
    block_size = loaded_data1["block_size"]
    loaded_data2 = load_data("snakerun4.pickle")
    data = loaded_data1["data"]
    data2 = loaded_data2["data"]
    data = data + data2
    print(len(data))
    data = clear_data(data)
    print(len(data))
    X_train = []
    Y_train = []
    for data_set in data:
        input_features = game_state_to_data_sample(data_set[0], bounds, block_size)
        output = data_set[1]
        X_train.append(input_features)
        Y_train.append(direction_to_label[output])
    return np.array(X_train), np.array(Y_train)


def compare_vectors(a, b):
    cons = 0
    not_cons = 0
    for a_elem, b_elem in zip(a, b):
        if a_elem == b_elem:
            cons += 1
        else:
            not_cons += 1
    return cons / (cons + not_cons)


class LogisticRegressionMulticlass:
    def __init__(self, learning_rate=0.01, num_iterations=10000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations

    def softmax(self, z):
        exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def fit(self, X, Y, num_classes):
        num_samples, num_features = X.shape
        # self.num_classes = num_classes

        self.weights = np.ones((num_features, num_classes))
        self.bias = np.ones((1, num_classes))

        Y_encoded = np.eye(num_classes)[Y]

        for _ in range(self.num_iterations):
            linear_model = np.dot(X, self.weights) + self.bias

            probabilities = self.softmax(linear_model)
            dw = (1 / num_samples) * np.dot(X.T, (probabilities - Y_encoded))
            db = (1 / num_samples) * np.sum(
                probabilities - Y_encoded, axis=0, keepdims=True
            )
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict_classes(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        probabilities = self.softmax(linear_model)

        # print(probabilities)
        return probabilities


if __name__ == "__main__":
    X_train, Y_train = data_converter()
    print(len(X_train[0]))

    X_train, X_test, Y_train, Y_test = train_test_split(
        X_train, Y_train, test_size=0.2, random_state=42
    )

    num_classes = 4
    model = LogisticRegressionMulticlass()
    model.fit(X_train, Y_train, num_classes)

    predicted_classes1 = model.predict_classes(X_train)
    predicted_classes2 = model.predict_classes(X_test)
    # print(compare_vectors(predicted_classes1, Y_train))
    # print(compare_vectors(predicted_classes2, Y_test))
    with open("snake_model.pickle", "wb") as f:
        pickle.dump(model, f)

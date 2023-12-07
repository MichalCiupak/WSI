import pickle
from pprint import pprint
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from snake import Direction

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


def is_obstacle_this_direction(body, b_s, bounds):
    head = body[-1]
    body = body[:-1]
    obstacles = np.array([0, 0, 0, 0])
    print(obstacles)
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


def data_converter():
    loaded_data = load_data("snakerun4.pickle")
    # pprint(loaded_data)
    bounds = loaded_data["bounds"]
    block_size = loaded_data["block_size"]
    data = loaded_data["data"]
    input_features = []
    X_train = []
    Y_train = []
    for data_set in data:
        # print(data_set)
        input_features = np.array([])
        food = data_set[0]["food"]
        body = data_set[0]["snake_body"]
        head = body[-1]
        output = data_set[1]
        input_features = np.concatenate(
            (input_features, is_food_this_direction(food, head))
        )
        # print(food)
        # print(head)
        # print(input_features)
        input_features = np.concatenate(
            (input_features, is_obstacle_this_direction(body, block_size, bounds))
        )
        X_train.append(input_features)
        Y_train.append(direction_to_label[output])
        print("oto")
        print(input_features)
        # print(Y_train)
    return X_train, Y_train


def game_state_to_data_sample(game_state, bounds, block_size):

    input_features = np.array([])
    food = game_state["food"]
    body = game_state["snake_body"]
    head = body[-1]
    input_features = np.concatenate(
        (input_features, is_food_this_direction(food, head))
    )

    input_features = np.concatenate(
        (input_features, is_obstacle_this_direction(body, block_size, bounds))
    )
    return input_features


if __name__ == "__main__":
    X_train, Y_train = data_converter()
    Y_train_one_hot = np.array(Y_train)

    # Podział danych na zbiór treningowy i testowy
    X_train, X_test, Y_train, Y_test = train_test_split(
        X_train, Y_train_one_hot, test_size=0.2, random_state=42
    )

    # Standaryzacja danych (opcjonalne, ale może poprawić wyniki)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Tworzymy model regresji logistycznej
    model = LogisticRegression(max_iter=1000, random_state=42)

    # Trenujemy model
    model.fit(X_train, Y_train)

    # Testujemy model na zbiorze testowym
    Y_pred = model.predict(X_test)

    # Oceniamy dokładność modelu
    accuracy = accuracy_score(Y_test, Y_pred)
    with open("snake_model.pickle", "wb") as f:
        pickle.dump(model, f)
    print(f"Accuracy: {accuracy}")
    """Example of how to read a pickled file, feel free to remove this"""
    # with open(f"data/2022-11-14_12:52:37.pickle", "rb") as f:
    #     data_file = pickle.load(f)
    # print(data_file["block_size"])
    # print(data_file["bounds"])
    # print(data_file["data"])


# pprint(load_data("snakerun1.pickle"))

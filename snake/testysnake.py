import pickle
from pprint import pprint

for i in range(3):
    print(i)


def loadpickle():
    with open("snakerun1.pickle", "rb") as f:
        loaded_data = pickle.load(f)
    return loaded_data


data = loadpickle()
pprint(data)

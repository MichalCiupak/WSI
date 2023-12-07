import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

# Przygotowanie danych treningowych
constant_data = [
    {
        'food': (150, 150),
        'snake_body': [(120, 150), (90, 150), (60, 150)],
        'snake_direction': Direction.RIGHT.value,
    },
    {
        'food': (200, 200),
        'snake_body': [(180, 200), (150, 200), (120, 200)],
        'snake_direction': Direction.UP.value,
    },
    # Dodaj więcej stałych danych treningowych
]

# Przygotowujemy dane wejściowe i wyjściowe
X_train = []
y_train = []

for data_point in constant_data:
    food_position = data_point['food']
    snake_body = data_point['snake_body']
    snake_direction = data_point['snake_direction']

    input_features = [food_position[0], food_position[1]]
    for body_part in snake_body:
        input_features.extend([body_part[0], body_part[1]])
    X_train.append(input_features)

    y_train.append(snake_direction)

# Tworzymy model
model = models.Sequential([
    layers.Dense(1, activation='linear', input_shape=(len(input_features),))
])

# Kompilujemy model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Trenujemy model
model.fit(np.array(X_train), np.array(y_train), epochs=10, batch_size=32)

# Testujemy model na nowych danych
new_data_point = {
    'food': (100, 100),
    'snake_body': [(80, 100), (60, 100), (40, 100)],
}

input_features = [new_data_point['food'][0], new_data_point['food'][1]]
for body_part in new_data_point['snake_body']:
    input_features.extend([body_part[0], body_part[1]])

predicted_direction = model.predict(np.array([input_features]))[0]
print(f'Predicted Direction: {predicted_direction}')

import copy
import os
import pickle
import pygame
import time
import numpy as np
from food import Food
from model import game_state_to_data_sample
from snake import Snake, Direction
from model import LogisticRegressionMulticlass


def main():
    pygame.init()
    bounds = (300, 300)
    window = pygame.display.set_mode(bounds)
    pygame.display.set_caption("Snake")

    block_size = 30
    snake = Snake(block_size, bounds)
    food = Food(block_size, bounds, lifetime=100)

    # agent = HumanAgent(
    #     block_size, bounds
    # )  # Once your agent is good to go, change this line
    agent = BehavioralCloningAgent(
        block_size, bounds
    )  # Once your agent is good to go, change this line
    scores = []
    run = True
    pygame.time.delay(100)
    game_count = 0
    while run and game_count < 100:
        pygame.time.delay(
            50
        )  # Adjust game speed, decrease to test your agent and model quickly

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        game_state = {
            "food": (food.x, food.y),
            "snake_body": snake.body,  # The last element is snake's head
            "snake_direction": snake.direction,
        }

        direction = agent.act(game_state)
        snake.turn(direction)

        snake.move()
        snake.check_for_food(food)
        food.update()

        if snake.is_wall_collision() or snake.is_tail_collision():
            game_count += 1
            pygame.display.update()
            pygame.time.delay(300)
            scores.append(snake.length - 3)
            snake.respawn()
            food.respawn()

        window.fill((0, 0, 0))
        snake.draw(pygame, window)
        food.draw(pygame, window)
        pygame.display.update()

    print(f"Scores: {scores}")
    print(f"Mean: {np.mean(scores)}")
    # agent.dump_data()
    pygame.quit()


class HumanAgent:
    """In every timestep every agent should perform an action (return direction) based on the game state. Please note, that
    human agent should be the only one using the keyboard and dumping data."""

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.data = []

    def act(self, game_state) -> Direction:
        keys = pygame.key.get_pressed()
        action = game_state["snake_direction"]
        if keys[pygame.K_LEFT]:
            action = Direction.LEFT
        elif keys[pygame.K_RIGHT]:
            action = Direction.RIGHT
        elif keys[pygame.K_UP]:
            action = Direction.UP
        elif keys[pygame.K_DOWN]:
            action = Direction.DOWN

        self.data.append((copy.deepcopy(game_state), action))
        return action

    def dump_data(self):
        os.makedirs("data", exist_ok=True)
        current_time = time.strftime("%Y-%m-%d_%H:%M:%S")
        with open(f"data/{current_time}.pickle", "wb") as f:
            pickle.dump(
                {
                    "block_size": self.block_size,
                    "bounds": self.bounds,
                    "data": self.data[:-10],
                },
                f,
            )  # Last 10 frames are when you press exit, so they are bad, skip them


class BehavioralCloningAgent:
    def __init__(self, block_size, bounds):
        self.model = self.load_model()
        self.block_size = block_size
        self.bounds = bounds

    def load_model(self):
        with open("snake_model.pickle", "rb") as f:
            loaded_model = pickle.load(f)
        return loaded_model

    def act(self, game_state) -> Direction:
        data_sample = game_state_to_data_sample(
            game_state, self.bounds, self.block_size
        )
        predicted_classes = self.model.predict_classes(np.array([data_sample]))
        action = game_state["snake_direction"]
        if predicted_classes == 0:
            action = Direction.UP
        elif predicted_classes == 1:
            action = Direction.RIGHT
        elif predicted_classes == 2:
            action = Direction.DOWN
        elif predicted_classes == 3:
            action = Direction.LEFT
        return action

    def dump_data(self):
        pass


if __name__ == "__main__":
    main()

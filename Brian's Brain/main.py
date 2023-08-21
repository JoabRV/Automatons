import time
import random
import numpy as np


def brians_brain(generations, width, height):
    states = [0, 1, 2]
    grid = np.random.choice(states, size=(height, width), p=[0.5, 0.25, 0.25])

    for _ in range(generations):
        new_grid = np.copy(grid)
        for y in range(height):
            for x in range(width):
                neighbors = grid[max(0, y - 1):min(height, y + 2), max(0, x - 1):min(width, x + 2)]
                live_neighbors = np.count_nonzero(neighbors == 1)
                if grid[y, x] == 0:
                    new_grid[y, x] = 1 if live_neighbors == 2 else 0
                elif grid[y, x] == 1:
                    new_grid[y, x] = 2
                elif grid[y, x] == 2:
                    new_grid[y, x] = 0
        grid = new_grid
        for row in grid:
            print(''.join(['#' if cell == 1 else ' ' if cell == 0 else '*' for cell in row]))
        time.sleep(0.1)


# Ejemplo de uso
brians_brain(generations=50, width=40, height=20)

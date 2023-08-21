import random


def forest_fire(steps, size):
    grid = [['empty'] * size for _ in range(size)]

    for _ in range(size * size // 3):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        grid[y][x] = 'tree'

    for _ in range(steps):
        new_grid = [['empty'] * size for _ in range(size)]
        for y in range(size):
            for x in range(size):
                if grid[y][x] == 'tree':
                    new_grid[y][x] = 'tree'
                    if random.random() < 0.01:
                        new_grid[y][x] = 'fire'
                elif grid[y][x] == 'fire':
                    new_grid[y][x] = 'empty'
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if 0 <= x + dx < size and 0 <= y + dy < size:
                                if random.random() < 0.1 and grid[y + dy][x + dx] == 'tree':
                                    new_grid[y + dy][x + dx] = 'fire'
        grid = new_grid
        for row in grid:
            print(''.join(['#' if cell == 'tree' else ' ' if cell == 'empty' else '*' for cell in row]))


# Ejemplo de uso
forest_fire(steps=50, size=40)

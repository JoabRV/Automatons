def langtons_ant(steps):
    grid = [[0] * 101 for _ in range(101)]
    x, y = 50, 50
    dx, dy = 0, -1

    for _ in range(steps):
        if grid[y][x] == 0:
            grid[y][x] = 1
            dx, dy = -dy, dx
        else:
            grid[y][x] = 0
            dx, dy = dy, -dx
        x += dx
        y += dy

    for row in grid:
        print(''.join(['#' if cell else ' ' for cell in row]))


# Ejemplo de uso
langtons_ant(steps=11000)

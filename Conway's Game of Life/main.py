import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Tamaño de la cuadrícula
rows, cols = 30, 30

# Crear una cuadrícula aleatoria inicial
grid = np.random.choice([0, 1], size=(rows, cols), p=[0.8, 0.2])


# Función para actualizar la cuadrícula en cada paso
def update(frameNum, img, grid, rows, cols):
    new_grid = grid.copy()
    for i in range(rows):
        for j in range(cols):
            # Calcular el número de vecinos vivos
            neighbors = grid[max(0, i - 1):min(rows, i + 2), max(0, j - 1):min(cols, j + 2)]
            live_neighbors = np.sum(neighbors) - grid[i, j]

            # Aplicar reglas del Juego de la Vida
            if grid[i, j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and live_neighbors == 3:
                new_grid[i, j] = 1

    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img


# Configuración de la visualización
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='binary')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, rows, cols), frames=50, interval=200)

plt.show()

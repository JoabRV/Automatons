def elementary_cellular_automaton(rule, generations, width):
    current_generation = [0] * width
    current_generation[width // 2] = 1

    for _ in range(generations):
        print(''.join(['X' if cell else ' ' for cell in current_generation]))
        next_generation = []
        for i in range(width):
            pattern = current_generation[i - 1] * 4 + current_generation[i] * 2 + current_generation[(i + 1) % width]
            next_generation.append((rule >> pattern) & 1)
        current_generation = next_generation


# Ejemplo de uso
elementary_cellular_automaton(rule=110, generations=10, width=21)

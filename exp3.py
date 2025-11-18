import random 
def fitness(x): 
    return -x**2 + 10*x 
def hill_climbing(): 
    current_x = random.uniform(0, 10) 
    step_size = 0.1 
    max_iterations = 100 
    for i in range(max_iterations): 
        next_x1 = current_x + step_size 
        next_x2 = current_x - step_size 
        next_fitness1 = fitness(next_x1) 
        next_fitness2 = fitness(next_x2) 
        current_fitness = fitness(current_x) 
        if next_fitness1 > current_fitness: 
            current_x = next_x1 
        elif next_fitness2 > current_fitness: 
            current_x = next_x2 
        else: 
        # No better neighbor found 
            break 
    return current_x, fitness(current_x) 
# Run the algorithm 
best_x, best_fitness = hill_climbing() 
print(f"Best solution x = {best_x:.4f}, f(x) = {best_fitness:.4f}")
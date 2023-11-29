import random
import math
import numpy as np

def calculate_fitness(solution):
    x, y = solution
    fitness = -(abs(math.sin(x) * math.cos(y) * math.exp(abs(1 - (math.sqrt(x**2 + y**2) / math.pi)))))
    return fitness

def initialize_population(population_size, solution_size, search_space):
    population = []
    for _ in range(population_size):
        solution = np.random.uniform(search_space[0], search_space[1], size=solution_size)
        population.append(solution)
    return population

def update_velocity(current_velocity, current_position, best_position, alpha, gamma):
    updated_velocity = current_velocity + alpha * (best_position - current_position) + gamma * (random.random() - 0.5)
    return updated_velocity

def update_position(current_position, velocity, search_space):
    updated_position = np.clip(current_position + velocity, search_space[0], search_space[1])
    return updated_position

def bat_algorithm(population_size, solution_size, search_space, num_iterations, alpha, gamma):
    population = initialize_population(population_size, solution_size, search_space)
    velocities = np.zeros((population_size, solution_size))

    for _ in range(num_iterations):
        fitness_values = [calculate_fitness(solution) for solution in population]
        best_index = np.argmax(fitness_values)
        best_solution = population[best_index]

        for i in range(population_size):
            current_solution = population[i]
            current_fitness = fitness_values[i]

            velocities[i] = update_velocity(velocities[i], current_solution, best_solution, alpha, gamma)
            new_solution = update_position(current_solution, velocities[i], search_space)
            new_fitness = calculate_fitness(new_solution)

            if new_fitness >= current_fitness and random.random() < 0.5:
                population[i] = new_solution

    fitness_values = [calculate_fitness(solution) for solution in population]
    best_index = np.argmax(fitness_values)
    best_solution = population[best_index]

    return best_solution

population_size = 50
solution_size = 2
search_space = [-10, 10]
num_iterations = 100
alpha = 0.5
gamma = 0.5

best_solution = bat_algorithm(population_size, solution_size, search_space, num_iterations, alpha, gamma)

print("Bat Algorithm:")
print("Best Solution:", best_solution)
print("Best Fitness:", calculate_fitness(best_solution))

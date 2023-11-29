import random
import math

def calculate_fitness(solution):
    # Fungsi ini menghitung fitness dari solusi yang diberikan.
    # Anda dapat mengganti fungsi ini sesuai dengan permasalahan yang ingin diselesaikan.
    # Semakin tinggi nilai fitness, semakin baik solusi tersebut.
    x = solution[0]
    y = solution[1]
    fitness = -(abs(math.sin(x) * math.cos(y) * math.exp(abs(1 - (math.sqrt(x**2 + y**2) / math.pi)))))
    return fitness

def initialize_population(population_size, solution_size, search_space):
    # Fungsi ini menginisialisasi populasi awal dengan solusi-solusi acak dalam rentang search space.
    population = []
    for _ in range(population_size):
        solution = [random.uniform(search_space[0], search_space[1]) for _ in range(solution_size)]
        population.append(solution)
    return population

def quantum_rotation_gate(solution, rotation_angle):
    # Fungsi ini menerapkan operasi Quantum Rotation Gate pada solusi.
    rotated_solution = []
    for i in range(len(solution)):
        theta = rotation_angle * (random.random() * 2 - 1)
        rotated_solution.append(solution[i] * math.cos(theta) + solution[i] * math.sin(theta))
    return rotated_solution

def quantum_inspired_evolutionary_algorithm(population_size, solution_size, search_space, num_iterations, rotation_angle):
    # Inisialisasi populasi awal
    population = initialize_population(population_size, solution_size, search_space)

    # Iterasi algoritma
    for _ in range(num_iterations):
        # Evaluasi fitness untuk setiap solusi dalam populasi
        fitness_values = [calculate_fitness(solution) for solution in population]

        # Mencari solusi terbaik dalam populasi
        best_index = fitness_values.index(max(fitness_values))
        best_solution = population[best_index]

        # Operasi Quantum Rotation Gate pada setiap solusi
        rotated_population = []
        for solution in population:
            rotated_solution = quantum_rotation_gate(solution, rotation_angle)
            rotated_population.append(rotated_solution)

        # Evaluasi fitness untuk setiap solusi yang sudah dirotasi
        rotated_fitness_values = [calculate_fitness(solution) for solution in rotated_population]

        # Memperbarui populasi dengan solusi-solusi yang memiliki fitness lebih baik
        new_population = []
        for i in range(population_size):
            if rotated_fitness_values[i] >= fitness_values[i]:
                new_population.append(rotated_population[i])
            else:
                new_population.append(population[i])

        population = new_population

    # Evaluasi fitness untuk populasi terakhir
    fitness_values = [calculate_fitness(solution) for solution in population]

    # Mencari solusi terbaik dalam populasi terakhir
    best_index = fitness_values.index(max(fitness_values))
    best_solution = population[best_index]

    return best_solution

# Parameter algoritma
population_size = 50
solution_size = 2
search_space = [-10, 10]
num_iterations = 100
rotation_angle = math.pi / 4

# Menjalankan algoritma Quantum-Inspired Evolutionary
best_solution = quantum_inspired_evolutionary_algorithm(population_size, solution_size, search_space, num_iterations, rotation_angle)

print("Quantum-Inspired Evolutionary Algorithm:")
print("Best Solution:", best_solution)
print("Best Fitness:", calculate_fitness(best_solution))
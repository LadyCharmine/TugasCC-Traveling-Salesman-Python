import random
import math

def calculate_fitness(solution):
    # Fungsi ini menghitung fitness dari solusi yang diberikan.
    # Anda dapat mengganti fungsi ini sesuai dengan permasalahan yang ingin diselesaikan.
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

def clone_solution(solution, clone_rate):
    # Fungsi ini mengklon solusi dengan mempertahankan beberapa proporsi gen yang sama.
    clone_solution = []
    for i in range(len(solution)):
        if random.random() < clone_rate:
            clone_solution.append(solution[i])
    return clone_solution

def mutate_solution(solution, mutation_rate, search_space):
    # Fungsi ini melakukan mutasi pada solusi dengan mengganti beberapa gen dengan nilai acak dalam rentang search space.
    mutated_solution = []
    for i in range(len(solution)):
        if random.random() < mutation_rate:
            mutated_solution.append(random.uniform(search_space[0], search_space[1]))
        else:
            mutated_solution.append(solution[i])
    return mutated_solution

def immune_system_algorithm(population_size, solution_size, search_space, num_iterations, clone_rate, mutation_rate):
    # Inisialisasi populasi awal
    population = initialize_population(population_size, solution_size, search_space)

    # Evaluasi fitness untuk setiap solusi dalam populasi
    fitness_values = [calculate_fitness(solution) for solution in population]

    # Mencari solusi terbaik dalam populasi
    best_index = fitness_values.index(max(fitness_values))
    best_solution = population[best_index]
    best_fitness = fitness_values[best_index]

    # Iterasi algoritma
    for _ in range(num_iterations):
        # Seleksi klonal
        clones = []
        for i in range(population_size):
            clone = clone_solution(population[i], clone_rate)
            clones.append(clone)

        # Mutasi
        mutants = []
        for i in range(population_size):
            mutant = mutate_solution(clones[i], mutation_rate, search_space)
            mutants.append(mutant)

        # Evaluasi fitness untuk setiap solusi baru
        fitness_values = [calculate_fitness(solution) for solution in mutants]

        # Mencari solusi terbaik dalam populasi baru
        new_best_index = fitness_values.index(max(fitness_values))
        new_best_solution = mutants[new_best_index]
        new_best_fitness = fitness_values[new_best_index]

        # Memperbarui solusi terbaik jika ditemukan solusi yang lebih baik
        if new_best_fitness > best_fitness:
            best_solution = new_best_solution
            best_fitness = new_best_fitness

        # Mengganti populasi dengan populasi baru
        population = mutants

    return best_solution

# Parameter algoritma
population_size = 50
solution_size = 2
search_space = [-10, 10]
num_iterations = 100
clone_rate = 0.1
mutation_rate = 0.1

# Menjalankan algoritma Immune System
best_solution = immune_system_algorithm(population_size, solution_size, search_space, num_iterations, clone_rate, mutation_rate)

print("Immune System Algorithm:")
print("Best Solution:", best_solution)
print("Best Fitness:", calculate_fitness(best_solution))

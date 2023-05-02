import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel("Student-choices.xls", header=None)
students = students.drop(students.columns[0], axis=1)
students = students.values.tolist()
capacity = pd.read_excel("Supervisors.xlsx", header=None)
capacity = capacity.drop(capacity.columns[0], axis=1)
capacity = capacity.values.tolist()
supervisors = list(range(1, len(capacity) + 1))

crossover_rate = 0.8
mutation_rate = 0.1
population_size = 100
max_generations = 20

num_supervisors = len(supervisors)
num_students = len(students)

capacity_map = {}
preference_map = {}
for i in range(1, num_supervisors + 1):
    capacity_map[i] = capacity[i - 1][0]
for i in range(num_students):
    preference_map[i] = students[i]
x_points = []
y_points = []


def create_population():
    population = []
    for _ in range(population_size):
        solution = []
        available_supervisors = supervisors.copy()
        for student in range(num_students):
            supervisor = random.choice(available_supervisors)
            solution.append((student, supervisor))
            capacity_map[supervisor] -= 1
            if capacity_map[supervisor] <= 0:
                available_supervisors.remove(supervisor)
        population.append(solution)
    return population


def select_parent(population):
    population = sorted(population, key=lambda x: fitness(x), reverse=True)
    num_parents = len(population) // 2
    parents = random.sample(population[:num_parents], 2)
    return parents


def mutate(solution):
    i, j = random.sample(range(len(solution)), 2)
    solution[i], solution[j] = solution[j], solution[i]
    return solution


def crossover(parent1, parent2):
    crossover_point = random.randint(0, num_students - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def fitness(solution):
    fitness = 0
    for student, supervisor in solution:
        preference_list = preference_map[student]
        for index, preference in enumerate(preference_list):
            if preference == supervisor:
                fitness += (index + 1)
                break
    return fitness


def graph(x, y):
    plt.plot(x, y)
    plt.xlabel('Generations')
    plt.ylabel('Average fitness')
    plt.title('Average fitness')
    plt.show()


def genetic_algorithm():
    population = create_population()
    generation = 0

    while generation < max_generations:
        new_population = []

        for _ in range(population_size // 2):
            parent1, parent2 = select_parent(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1) if random.random() < mutation_rate else child1
            child2 = mutate(child2) if random.random() < mutation_rate else child2
            new_population.append(child1)
            new_population.append(child2)

        population = new_population
        avg_fitness = sum([fitness(x) for x in population]) / population_size
        x_points.append(generation)
        y_points.append(avg_fitness)
        print(f"Generation {generation}: Average fitness = {avg_fitness:.2f}")
        generation += 1

    graph(x_points, y_points)


genetic_algorithm()
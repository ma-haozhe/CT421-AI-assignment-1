# CT421 AI Assignment 1 part a problem iii deceptive landscape
# Haozhe Ma
# id: 19280083

import csv
import part_a_i
import part_a_ii
import random
import matplotlib.pyplot as plt

num_tests = 5
test_data =[]
x_plt = []
y_plt = []
# expand this to decimal numbers, string length still = 30
target_dec = '012345678909876543211234567890'

#modified version of mutation function
def mutation_1(offspring_pair):
    # we set the mutation rate as 10%.
    # so we can use random number [0,1] generated less than 0.1 to simulate 10%.
    # on average about 3 digits in the string will be flipped by use 1 to minus that digit.
    offspring_pair[0] = list(offspring_pair[0])
    offspring_pair[1] = list(offspring_pair[1])
    for i in range(len(offspring_pair[0])):
        if random.random() < 0.1:
            offspring_pair[0][i] = str(random.randint(0,9))
            #print('str1 changed')

    for i in range(len(offspring_pair[1])):
        if random.random() < 0.1:
            offspring_pair[1][i] = str(random.randint(0,9))
            #print('str2 changed')

    offspring_pair[0] = ''.join(offspring_pair[0])
    offspring_pair[1] = ''.join(offspring_pair[1])
    #print('offspring pair', offspring_pair)
    return offspring_pair


def count_fitness_3(binary_strings):
    output = []
    for binary_string in binary_strings:
        count = 0
        for i in range(len(binary_string)):
            if binary_string[i] == target_dec[i]:
                count += 1
        output.append(count)
    return output

def count_fitness_4(binary_string):
    count = 0
    for i in range(len(binary_string)):
        if binary_string[i] == target_dec[i]:
            count += 1
    return count

#we also need to modify the string generation func
def generate_strings(len):
    output = []
    for i in range(50):
        binary_string = ""
        for j in range(len):
            binary_string += str(random.randint(0, 9))
        output.append(binary_string)
    return output

def replace_individual_2(binary_strings, offspring_pair):
    # the function should take the original 5 string population and two mutated offspring
    # then replace the least fitted individuals with the offsprings
    # this is the end of a generation, the generation counter should + 1
    fitness_list = count_fitness_3(binary_strings)
    min1 = min(fitness_list)
    min1_index = fitness_list.index(min1)
    fitness_list.remove(min1)
    min2 = min(fitness_list)
    min2_index = fitness_list.index(min2)
    min_list = [binary_strings[min1_index], binary_strings[min2_index]]
    # find the two largest fitness from min1, min2 and the two offspring
    # this tuned out to be especially tricky(pain in the fucking ass actually
    # , I spent like at least half a whole day to solve this stupid problme) for me.
    combine = min_list+offspring_pair
    # calculate the fitness score for each binary string and store them in a dictionary
    fitness_scores = {}
    for binary_string in combine:
        fitness_scores[binary_string] = count_fitness_4(binary_string)
    # sort the binary strings based on their fitness scores (in descending order)
    sorted_binary_strings = sorted(
        combine, key=lambda x: fitness_scores[x], reverse=True)
    # select the two binary strings with the highest scores
    best_binary_strings = sorted_binary_strings[:2]
    # print the result
    #print(best_binary_strings)
    # now we have the least fitted index from the population list
    binary_strings[min1_index] = best_binary_strings[0]
    binary_strings[min2_index] = best_binary_strings[1]
    # return the new generation population.
    return binary_strings

def one_max_3():
    csv_writer = csv.writer(open('output.csv', 'w'))
    csv_writer.writerow(['Generation', 'Average fitness'])
    # step1 init population of 50.
    data = []
    populaton = generate_strings(30)
    #generation counter
    generation = 0
    # print('original population:', populaton)
    for i in range(30000):
        # step2 calculate the fitness of this generation (mean?)
        # write this to csv later
        #for this problem, the fitness counting function is from problem ii. 
        fitness = count_fitness_3(populaton)
        avg_fitness = sum(fitness) / len(fitness)
        # step3 perform crossover
        offspring = part_a_i.shuffle_and_crossover(populaton)
        # step4 pass the two offspring to mutate, 10% mutation probability.
        offspring = mutation_1(offspring)
        # step5 calculate the fitness after mutation
        # offspring_fitness = count_fitness(offspring)
        # step6 replace low fitness individuals with offspring
        replace_individual_2(populaton, offspring)
        generation += 1
        csv_writer.writerow([generation, avg_fitness])
        data.append([generation, avg_fitness])
        if avg_fitness == 30:
            print('current gen fitness: ', avg_fitness)
            print('generation:', generation)
            return data
        
def plot():
    for i in range(num_tests):
        test_results = one_max_3()
        test_data.append(test_results)

    #print(test_data)
    colours = ['r', 'g', 'b', 'c', 'm']
    labels = [0, 1, 2, 3, 4]
    for i in range(num_tests):
        for j in range(len(test_data[i])):
            plt.plot(test_data[i][j][0], test_data[i]
                     [j][1], '.', color=colours[i])

   # clset = set(zip(colours, labels))

    # add a legend and axis labels

    plt.xlabel('generation')
    plt.ylabel('fitness')

    # show the plot
    plt.show()

#one_max_3()
plot()


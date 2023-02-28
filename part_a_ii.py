# CT421 AI Assignment 1 part a problem ii
# Haozhe Ma
# id: 19280083


import csv
import part_a_i

# we are setting a different binary string this time and changing 
# the fitness function to check how many it matching bits it have.

# 1. creating a custom binary string
# also length = 30
target = '111000111000111000111000111000'

#for counting multiple strings
def count_fitness_1(binary_strings):
    output = []
    for binary_string in binary_strings:
        count = 0
        for i in range(len(binary_string)):
            if binary_string[i] == target[i]:
                count+=1
        output.append(count)
    return output

# for counting a single string
def count_fitness_2(binary_string):
    count = 0
    for i in range(len(binary_string)):
            if binary_string[i] == target[i]:
                count+=1
    return count

def replace_individual_1(binary_strings, offspring_pair):
    # the function should take the original 5 string population and two mutated offspring
    # then replace the least fitted individuals with the offsprings
    # this is the end of a generation, the generation counter should + 1
    fitness_list = count_fitness_1(binary_strings)
    min1 = min(fitness_list)
    min1_index = fitness_list.index(min1)
    fitness_list.remove(min1)
    min2 = min(fitness_list)
    min2_index = fitness_list.index(min2)
    min_list = [binary_strings[min1_index], binary_strings[min2_index]]
    # find the two largest fitness from min1, min2 and the two offspring
    # this tuned out to be especially tricky(pain in the fucking ass actually
    # , I spent like at least half a whole day to solve this stupid problme) for me.
    combine  = min_list+offspring_pair
    # calculate the fitness score for each binary string and store them in a dictionary
    fitness_scores = {}
    for binary_string in combine:
        fitness_scores[binary_string] = count_fitness_2(binary_string)
    # sort the binary strings based on their fitness scores (in descending order)
    sorted_binary_strings = sorted(combine, key=lambda x: fitness_scores[x], reverse=True)
    # select the two binary strings with the highest scores
    best_binary_strings = sorted_binary_strings[:2]
    # print the result
    print(best_binary_strings)  
    # now we have the least fitted index from the population list
    binary_strings[min1_index] = best_binary_strings[0]
    binary_strings[min2_index] = best_binary_strings[1]
    # return the new generation population.
    return binary_strings

def one_max_1():
    csv_writer = csv.writer(open('output.csv', 'w'))
    csv_writer.writerow(['Generation', 'Average fitness'])
    # step1 init population of 50.
    populaton = part_a_i.binary_strings(30)
    #generation counter
    generation = 0
    # print('original population:', populaton)
    for i in range(10000):
        # step2 calculate the fitness of this generation (mean?)
        # write this to csv later
        fitness = count_fitness_1(populaton)
        avg_fitness = sum(fitness) / len(fitness)
        print('current gen fitness: ', avg_fitness)
        # step3 perform crossover
        offspring = part_a_i.shuffle_and_crossover(populaton)
        # step4 pass the two offspring to mutate, 10% mutation probability.
        offspring = part_a_i.mutation(offspring)
        # step5 calculate the fitness after mutation
        # offspring_fitness = count_fitness(offspring)
        # step6 replace low fitness individuals with offspring
        replace_individual_1(populaton, offspring)
        generation += 1
        print('generation:', generation)
        csv_writer.writerow([generation, avg_fitness])
        #print(populaton)
        if avg_fitness == 30:
            break
    #print(populaton)

one_max_1()
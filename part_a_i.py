# CT421 AI Assignment 1 part 1
# Haozhe Ma
# id: 19280083
# 1. one-max problem


import random
import csv

# step 1: we first generate a population of string (length = 30)


def binary_strings(len):
    output = []
    for i in range(50):
        binary_string = ""
        for j in range(len):
            binary_string += str(random.randint(0, 1))
        output.append(binary_string)
    return output

# print(binary_strings(30)) to generate 50 random binary strings, length of 30.


# step 2 calculate the fitness by counting number of 1s in each string.

def count_fitness(binary_strings):
    output = []
    for binary_string in binary_strings:
        count = 0
        for char in binary_string:
            if char == '1':
                count += 1
        output.append(count)
    return output

# print(count_fitness(binary_strings(30)))
# this could ouput how many 1s in each population
# e.g. [16, 15, 13, 13, 24]

# step 3: one-point crossover. Let's say we select two from the population
# and form a pairs randomly each time. Then do the crossover and calculate
# offsprings' fitness.


def one_point_crossover(str1, str2):
    cut_point = random.randint(1, len(str1) - 1)
    output1 = str1[:cut_point] + str2[cut_point:]
    output2 = str2[:cut_point] + str1[cut_point:]
    return output1, output2


def shuffle_and_crossover(binary_sstrings):
    random.shuffle(binary_sstrings)
    crossover1, crossover2 = one_point_crossover(
        binary_sstrings[0], binary_sstrings[1])
    # crossover1, 2 are the new offsprings
    offspring = [crossover1, crossover2]

    return offspring


# step 4 mutate the offspring
def mutation(offspring_pair):
    # we set the mutation rate as 10%.
    # so we can use random number [0,1] generated less than 0.1 to simulate 10%.
    # on average about 3 digits in the string will be flipped by use 1 to minus that digit.
    offspring_pair[0] = list(offspring_pair[0])
    offspring_pair[1] = list(offspring_pair[1])
    for i in range(len(offspring_pair[0])):
        if random.random() < 0.1:
            offspring_pair[0][i] = 1-int(offspring_pair[0][i], 2)
            offspring_pair[0][i] = str(offspring_pair[0][i])
            # print('str1 changed')

    for i in range(len(offspring_pair[1])):
        if random.random() < 0.1:
            offspring_pair[1][i] = 1-int(offspring_pair[1][i], 2)
            offspring_pair[1][i] = str(offspring_pair[1][i])
            # print('str2 changed')

    offspring_pair[0] = ''.join(offspring_pair[0])
    offspring_pair[1] = ''.join(offspring_pair[1])
    # print(offspring_pair)
    return offspring_pair

# mutation(['000111101100010000111011111000','010100000110100010111110100110'])

# step 5 calculate the fitness of our mutated offsprings,
# we can use the count_fitness() func for this.

# step 6 replace the least fit individuals in our population with the new offspring
# do the offspring need to have higher fitness??
# after testing: yes, otherwise the average fitness will max out at around 25 out of 30.


def replace_individual(binary_strings, offspring_pair):
    # the function should take the original 5 string population and two mutated offspring
    # then replace the least fitted individuals with the offsprings
    # this is the end of a generation, the generation counter should + 1
    fitness_list = count_fitness(binary_strings)
    min1 = min(fitness_list)
    min1_index = fitness_list.index(min1)
    fitness_list.remove(min1)
    min2 = min(fitness_list)
    min2_index = fitness_list.index(min2)
    min_list = [binary_strings[min1_index], binary_strings[min2_index]]
    # find the two largest fitness from min1, min2 and the two offspring
    largest = []
    for s1, s2 in zip(min_list, offspring_pair):
        if max(count_fitness(s1), count_fitness(s2)) == count_fitness(s1):
            largest.append(s1)
        else:
            largest.append(s2)
    # print(largest)
    # now we have the least fitted index from the population list
    binary_strings[min1_index] = largest[0]
    binary_strings[min2_index] = largest[1]
    # return the new generation population.
    return binary_strings

# Now we build a function to do all these iteratively and write the data to a csv so we can plot it.


def one_max():
    csv_writer = csv.writer(open('output.csv', 'w'))
    csv_writer.writerow(['Generation', 'Average fitness'])
    # step1 init population of 50.
    populaton = binary_strings(30)
    #generation counter
    generation = 0
    # print('original population:', populaton)
    for i in range(7000):
        # step2 calculate the fitness of this generation (mean?)
        # write this to csv later
        fitness = count_fitness(populaton)
        avg_fitness = sum(fitness) / len(fitness)
        print('current gen fitness: ', avg_fitness)
        # step3 perform crossover
        offspring = shuffle_and_crossover(populaton)
        # step4 pass the two offspring to mutate, 10% mutation probability.
        offspring = mutation(offspring)
        # step5 calculate the fitness after mutation
        # offspring_fitness = count_fitness(offspring)
        # step6 replace low fitness individuals with offspring
        replace_individual(populaton, offspring)
        generation += 1
        print('generation:', generation)
        csv_writer.writerow([generation, avg_fitness])
        if avg_fitness == 30:
            #csv_writer.close()
            break


#one_max()

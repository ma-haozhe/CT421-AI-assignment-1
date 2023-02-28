# CT421 AI Assignment 1 part a problem iii deceptive landscape
# Haozhe Ma
# id: 19280083


# we have a fixed length of solution (30) for this problem. 
# does it means that when the whole string is '0', then the fitness
# is going to be 2*30 = 60??
# well that is truely quite deceptive.

import part_a_i

# change the fitness counting function
def count_fitness_3(binary_strings):
    #this new one should first check if there's no '1' present in the whole string.
    #if so the fitness score should be 60(explained in the top comment).

    output = []
    for binary_string in binary_strings:
        count = 0
        for char in binary_string:
            if char == '1':
                count += 1
        if count == 0:
            output.append(2*len(binary_string))
        else:
            output.append(count)
    return output

# we are going to modify this 'main' function from q1 i too. 

def one_max_2():
    csv_writer = part_a_i.csv.writer(open('output.csv', 'w'))
    csv_writer.writerow(['Generation', 'Average fitness'])
    # step1 init population of 50.
    populaton = part_a_i.binary_strings(30)
    #generation counter
    generation = 0
    # print('original population:', populaton)
    for i in range(20000):
        # step2 calculate the fitness of this generation (mean?)
        # write this to csv later
        fitness = count_fitness_3(populaton)
        avg_fitness = sum(fitness) / len(fitness)
        print('current gen fitness: ', avg_fitness)
        # step3 perform crossover
        offspring = part_a_i.shuffle_and_crossover(populaton)
        # step4 pass the two offspring to mutate, 10% mutation probability.
        offspring = part_a_i.mutation(offspring)
        # step5 calculate the fitness after mutation
        # offspring_fitness = count_fitness(offspring)
        # step6 replace low fitness individuals with offspring
        part_a_i.replace_individual(populaton, offspring)
        generation += 1
        print('generation:', generation)
        csv_writer.writerow([generation, avg_fitness])
        #if avg_fitness == 30:
            #csv_writer.close()
        #    break

#one_max_2()
# CT421 AI Assignment 1 part a problem iii deceptive landscape
# Haozhe Ma
# id: 19280083

import part_a_i
import part_a_iii
import random

# expand this to decimal numbers, string length still = 30
target = '012345678909876543211234567890'

#modified version of mutation function
def mutation_1(offspring_pair):
    # we set the mutation rate as 10%.
    # so we can use random number [0,1] generated less than 0.1 to simulate 10%.
    # on average about 3 digits in the string will be flipped by use 1 to minus that digit.
    offspring_pair[0] = list(offspring_pair[0])
    offspring_pair[1] = list(offspring_pair[1])
    for i in range(len(offspring_pair[0])):
        if random.random() < 0.1:
            offspring_pair[0][i] = str((int(offspring_pair[0][i]) + 1) % 10)
            # print('str1 changed')

    for i in range(len(offspring_pair[1])):
        if random.random() < 0.1:
            offspring_pair[1][i] = str((int(offspring_pair[1][i]) + 1) % 10)
            # print('str2 changed')

    offspring_pair[0] = ''.join(offspring_pair[0])
    offspring_pair[1] = ''.join(offspring_pair[1])
    # print(offspring_pair)
    return offspring_pair

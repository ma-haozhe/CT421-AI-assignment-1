#CT421 AI Assignment 1 part B
# Haozhe Ma
# 19280083

# We have a list of Students (S) and a list of Lecturers (L). 
# Each student has a complete list of the preference of lectures for their project. 
# and lecutrers have capacities of students they can take. 
# the fitness is basically the sum of students one lecture finally take.
# we want the sum to be as small as possible, 
# this sounds like a knapsack problem to me when first reading it. 

# The student preference and lecturers are stored in two xlsx files. 
# We first read the supervisor file, store them in lists? we need to get the number of 
# lecturers first. 

# use pandas lib to read xls tables. 
import pandas as pd
#'header=None' to also read the first row.
dataframe = pd.read_excel('./Supervisors.xlsx', header=None)
#convert pandas dataframe to list. 
supervisors = dataframe.values.tolist()

print(supervisors)
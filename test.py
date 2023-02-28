target='111000'

min_list  = ['111111', '000000']

offspring_pair = ['111100', '011000']

best_string1, best_string2 = None, None
best_score = 0
for string1 in min_list:
     for string2 in offspring_pair:
        score = 0
        for i in range(len(target)):
            if target[i] == string1[i] or target[i] == string2[i]:
                score += 1

            if score > best_score:
                best_score = score
                best_string1 = string1
                best_string2 = string2

print(best_string1,', ', best_string2)




    best_strings = []
    for string1 in combine:
        fit = count_fitness_2(string1)
        print(fit)
        print(type(fit))
        if len(best_strings) < 2:
            best_strings.append(string1)
        elif max(best_strings, key=count_fitness_2) < fit:
            best_strings[best_strings.index(max(best_strings, key=count_fitness_2))] = string1
    print(best_strings)
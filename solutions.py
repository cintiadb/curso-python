with open("solution.csv", "r", encoding="utf-8") as my_file:
    for line in my_file:
        parts = line.strip().split(';')  

        name_of_student = parts[0]
        problem = parts[1]
        expected_result = parts[2]

        if str(eval(problem)) == expected_result:
            with open("correct.csv", "a") as correct_file:
                correct_file.write(line + '\n')
        else:
            with open("incorrect.csv", "a") as incorrect_file:
                incorrect_file.write(line + '\n')
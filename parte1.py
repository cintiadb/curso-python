if False:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

student = {}
with open("students1.csv") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        student[parts[0]] = parts[1:]

exercise = {}

with open("exercises1.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        exercise[parts[0]] = int(parts[1]) +int(parts[2])+int(parts[3])+int(parts[4])+int(parts[5])+int(parts[6])+int(parts[7])

for id, student in student.items():
    if id in exercise:
        total_exercise = exercise[id]
        student_name = ' '.join(student)
        print(f"{student_name} {total_exercise}")
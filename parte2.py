if False:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    examen_class =input("Exam points:")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    examen_class = "exam_points1.csv"

student = {}
with open("students1.csv") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        student[parts[0]] = parts[1:]

points = {}

with open("exam_points1.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        points[parts[0]] = int(parts[1]) +int(parts[2])+int(parts[3])



for id, std in student.items():
    if id in points:
        total_exercise=points[id]
        student_name = ' '.join(std)
    if total_exercise < 14:
        pts = 0
    elif total_exercise > 14 and total_exercise <= 17:
        pts  = 1
    elif total_exercise > 17 and total_exercise <= 20:
        pts  = 2
    elif total_exercise > 20 and total_exercise <= 23:
        pts  = 3
    elif total_exercise > 23 and total_exercise <= 27:
        pts  = 4
    elif total_exercise >= 28:
        pts  = 5
        
    print(f"{student_name} {pts}")
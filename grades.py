def main():
    students_data = []
    while True:
        input_data = input("Exam points and exercises completed: ")
        if input_data == "":
            break
        exam_points, exercises_completed = map(int, input_data.split())
        exercise_points = exercises_completed // 10
    
        total_points = exam_points + exercise_points
        if exam_points < 10:
            grade = 0
        elif total_points <= 14:
            grade = 0
        elif 15 <= total_points <= 17:
            grade = 1
        elif 18 <= total_points <= 20:
            grade = 2
        elif 21 <= total_points <= 23:
            grade = 3
        elif 24 <= total_points <= 27:
            grade = 4
        elif 28 <= total_points <= 30:
            grade = 5
        
        students_data.append(grade)
    
  
    total_points = sum(students_data)
    total_students = len(students_data)
    
  
    points_average = total_points / total_students if total_students > 0 else 0
    
  
    pass_count = len([grade for grade in students_data if grade > 0])
    pass_percentage = (pass_count / total_students) * 100 if total_students > 0 else 0

    grade_distribution = [0] * 6  
    for grade in students_data:
        grade_distribution[grade] += 1
    
    print("Statistics:")
    print(f"Points average: {points_average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        print(f"  {i}: {'*' * grade_distribution[i]}")
    
main()
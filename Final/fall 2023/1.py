def pass_or_fail(grades_dict, minimum_passing_grade):
    passing_students = []
    for student, grades in grades_dict.items():
        average_grade = sum(grades) / len(grades)
        if average_grade >= minimum_passing_grade:
            passing_students.append(student)
    return passing_students


grades_dict = {
    "Alice": [85, 90, 88],
    "Bob": [70, 75, 72],
    "Dane": [10, 25, 32],
    "Charlie": [92, 88, 95],
}
passing_grade = 40
print(pass_or_fail(grades_dict, passing_grade))  # ['Alice', 'Bob', 'Charlie']
import numpy as np

# 1. Create a 5x3 Array for marks (5 Students, 3 Subjects)
# Data given in the assignment sheet:
marks = np.array([
    [50, 85, 80],  # Student 0
    [60, 95, 35],  # Student 1
    [70, 65, 68],  # Student 2
    [85, 55, 65],  # Student 3
    [80, 85, 90]   # Student 4
])

print("--- Original Marks Array (5 Students x 3 Subjects) ---")
print(marks)
print("-" * 50)

# Task 1: Find Overall Maximum, Minimum, and Average Marks
print(f"1. Maximum Marks (Overall) : {np.max(marks)}")
print(f"2. Minimum Marks (Overall) : {np.min(marks)}")
print(f"3. Average Marks (Overall) : {np.mean(marks):.2f}")

# Task 2: Student ID who scored max marks in Subject 1 (Index 0)
top_student_sub1 = np.argmax(marks[:, 0])
print(f"4. Student ID with max marks in Subject 1 : Student {top_student_sub1}")

# Task 3: Subject-wise Maximum Marks
max_sub_wise = np.max(marks, axis=0)
print(f"5. Subject-wise Maximum Marks : {max_sub_wise}")

# Task 4: Subject-wise Average Marks
avg_sub_wise = np.mean(marks, axis=0)
print(f"6. Subject-wise Average Marks : {np.round(avg_sub_wise, 2)}")

# Task 5: Add 10 Marks to students who scored < 50 in Subject 1
marks_updated = marks.copy()
sub1_marks = marks_updated[:, 0]
sub1_marks[sub1_marks < 50] += 10
print("\n--- Updated Marks Array (After Grace Marks in Subject 1) ---")
print(marks_updated)

# Task 6: Number of students scoring > 80 in Subject 1
count_above_80 = np.sum(marks[:, 0] > 80)
print(f"\n7. Number of students scoring > 80 in Subject 1 : {count_above_80}")

# Task 7: Minimum marks of Student 2 (Index 2)
min_student_2 = np.min(marks[2, :])
print(f"8. Minimum marks of Student 2 : {min_student_2}")

# Task 8: Maximum marks of Student 4 (Index 4)
max_student_4 = np.max(marks[4, :])
print(f"9. Maximum marks of Student 4 : {max_student_4}")

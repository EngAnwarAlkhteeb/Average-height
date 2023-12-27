student_heights = input("Insert the students height (with space):\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


total_height = 0
for height in student_heights:
    total_height += height
print(f"Total height = {total_height}")
number_of_student = 0
for student in student_heights:
    number_of_student += 1
print(f"Number of student = {number_of_student}")

average_of_height = total_height // number_of_student
print(f"Average height = {average_of_height}")

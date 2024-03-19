num_students = int(input("Enter the number of students: "))

students_info = []

for i in range(num_students):
    name = input("Enter student {} name: ".format(i+1))
    grade = float(input("Enter {}'s grade: ".format(name)))
    students_info.append((name, grade))

students_info.sort(key=lambda x: x[1], reverse=True)

print("Sorted grades (descending order):")
for name, grade in students_info:
    print(name + ": " + str(grade))

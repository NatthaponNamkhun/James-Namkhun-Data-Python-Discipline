# Sorting Student's name in list
students = []

# recive number of student in list
numStudent = int(input("Enter number of students: "))

for i in range(numStudent):
    # input student's name
    name = input(f"Enter Student's name {i + 1}: ")  
    students.append(name)  # adding name form input to students list

# Sorting(String) name > A-z
students.sort()
print("Student's name:", students)
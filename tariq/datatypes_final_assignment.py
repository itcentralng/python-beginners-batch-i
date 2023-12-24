# Q1. Create a list of 5 students
# Q2. Using slicing, get the first two students
# Q3. Using slicing, get the last two students
# Q4. Create 2 variables holding a name each
# Q5. Using the right method, add the value of each of the variables to the list above
# Q6. Create an empty dictionary called student
# Q7. Using the right method, remove the first student from the list above and add it
# as a value in the above dictionary
# Q8. Remove the last two items from the above list and create a tuple with the values
# Q9. Add age, gender, hieght of the student into the student dictionary above using
# the most appropraite data types.
# Q10. Store a value for the student in the dictionary that indicates whether the student
# is admitted or not using a boolean.

#Q1
students = ["Abdul", "Mansur", "Haruna", "Abubakar", "Ibrahim"]
print(students)

#Q2
x = students[:2]
print(x)

#Q3
last_two_students = students[3:]
print(last_two_students)

#Q4
new_student1 = "Tariq"
new_student2 = "Kabir"

#Q5
students.append(new_student1)
students.append(new_student2)
print(students)

#Q6
student = {}

#Q7
removed_student = students.pop(0)
student["first_student"] = removed_student
print(students) 
print(student)

#Q8.
removed_students = students[-2:]
students = students[:-2]
students_tuple = tuple(removed_students)
print(students)
print(students_tuple)

#Q9.
student["age"] = 15 
student["gender"] = "Male"
student["height"] = 169.5
print(student)

#Q10.
student["admitted"] = True
print(student)
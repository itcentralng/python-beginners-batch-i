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

students = ['muhammad', 'ahmad', 'hamza', 'abbas', 'musa']

print(students[:2])
print(students[3:5])

name = 'kabir'
name2 = 'abdullahi'

students.append(name)
students.append(name2)

print(students)

student = {}

minus_student = students.pop(0)
student['first_student'] = minus_student
print(student)

items2 = students [4:6]
items2_ = tuple(items2)

print(items2_)

student['age'] = 18
student['gender'] = 'male'
student['height'] = 1.80

print(student)

student['admitted'] = True

print(student)






# Q1. Create a list of 5 students
students = ["Ahmad", "Mohd", "Makarfi", "Malam", "Nasir"]
print(students)
# Q2. Using slicing, get the first two students
print(students[:2])
# Q3. Using slicing, get the last two students
print(students[-2:])
# Q4. Create 2 variables holding a name each
name1 = "Mukhtar"
name2 = "Hamza"
# Q5. Using the right method, add the value of each of the variables to the list above
students.append(name1)
students.append(name2)
print(students)
# Q6. Create an empty dictionary called student
student = {}
# Q7. Using the right method, remove the first student from the list above and add it
# as a value in the above dictionary
student['name'] = students.pop(0)
print(student)
# Q8. Remove the last two items from the above list and create a tuple with the values
mytuple = students.pop(), students.pop()
print(mytuple)
# Q9. Add age, gender, hieght of the student into the student dictionary above using
# the most appropraite data types.
student['age'] = 20
student.setdefault('gender', "male")
student.update({'height':1.9})
print(student)
# Q10. Store a value for the student in the dictionary that indicates whether the student
# is admitted or not using a boolean.
student['is_admitted'] = False
print(student)
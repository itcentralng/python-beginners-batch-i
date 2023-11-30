# Integers - Whole numbers, either positive or negative
age = 20
friends = 30
debt = -1000

print(age)

# FLoat - fractions either positive or negative
height = 1.79
weight = 45.5
balance = -1.56

print(height)

# Boolen - True or False values
heIsABoy = True
sheIsAGirl = False

print(heIsABoy)

# String - Sequence of characters stored within quotations - either double or single
name = "Shedrack"
height = "1.79M"
weight = "45.5KG"

print(weight)


# List - A way store mulitple comma separated data within square brackes
friends = ["James", "Amina", "Ibrahim"]
items = [1, 1.2, True, "Amina", [True, False]]

print(items)

# Tuple - A way to store multiple comma separeted data
friends = ("James", "Amina", "Ibrahim")
items = 1, 1.2, True, "Amina", [True, False]

print(items)

# Dictionary - similar to a regular dictionary, it stores data in a key-value pair
person = {"name":"Ibrahim", "age":20, "height":"1.65M", "weight":89.9}
fruit = {'name':'Apple', "taste":"sweet", "color":"red"}

print(person)


# String Methods
name = "james"
print(name.capitalize())

fruit = "APpLE"
print(fruit.casefold())

password = "pass"
print(password.center(11, "*"))

item = "people"
print(item.count("e"))

# List methods
items = [1, 1.3]
print(items)
items.append(True)
items2 = items.copy()
print(items)
items.clear()
print(items)
print(items2)

# Tuple Methods
people = "Ashiru", "Shedrack", "Ashiru"
print(people.count("Shedrack"))
print(people.index("Ashiru"))

# Dictionary Methods
person = {"name":"Ibrahim"}
person2 = person.copy()
print(person)
person.clear()
print(person)
print(person2)
print(person.get("name", "test"))
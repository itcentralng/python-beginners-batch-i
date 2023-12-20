# Q1. Using examples, explain the following list methods:
# append, extend, pop, insert, remove


"""append: method is a list method used to add a single element to the end of a list. example:"""
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)


"""extend: is used to extend a list by appending elements from an iterable (such as another list, tuple, or any iterable object). example:"""
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)


"""pop: is a list method that is used to remove and return the element at a specified index. example:"""
fruits = ['grape', 'orange', 'banana', 'apple']
removed_fruit = fruits.pop()
print(removed_fruit)


"""insert: used to insert an element at a specified position in a list. example:"""
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

fruits = ['apple', 'orange', 'banana']
fruits.insert(0, 'grape')
print(fruits)

"""remove: this method is a list method used to remove the first occurrence of a specified element from the list. example: """
numbers = [1, 2, 3, 4, 3, 5]
numbers.remove(3)
print(numbers)

fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)
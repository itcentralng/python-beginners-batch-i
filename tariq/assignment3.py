# Q1. Practice all the methods treated today
# Q2. Explain how the following list methods work, with an example:
# - index, sort, pop, insert, remove, reverse

"""Index: used to find the index of the first occurrence of a specified element in the list. example:"""
fruits = ['apple', 'banana', 'cherry']
x = fruits.index('banana')
print(x)

numbers = [10, 20, 30, 20, 40, 50]
index_20 = numbers.index(20, 2, 5)
print("Index of 20 between indices 2 and 5:", index_20)

"""sort:  is used to sort the elements of a list in ascending order. example:"""
numbers = [5, 9, 2, 8, 1, 7, 6, 4, 10, 3]
numbers.sort()
print(numbers)

cars = ['Ford', 'Benz', 'BMW', 'Astra', 'Volvo']
cars.sort()
print(cars)

"""pop: is a list method that is used to remove and return the element at a specified index. example:"""
fruits = ['apple', 'orange', 'banana', 'grape']
removed_fruit = fruits.pop()

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

"""reverse: this method reverses the elements of a list in place. This means that it modifies the original list without creating a new one. example:"""
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

fruits = ["apple", "orange", "banana", "grape"]
fruits.reverse()
print(fruits)

mixed_list = [1, "two", 3.0, [4, 5]]
mixed_list.reverse()
print(mixed_list)
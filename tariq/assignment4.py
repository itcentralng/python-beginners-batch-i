# Q1. Write 5 examples of a dictionary
"""1 - Dictionary of Student Information"""
"""2 - Dictionary of Book Information"""
"""3 - Dictionary of Programming Languages"""
"""4 - Dictionary of Car Information"""
"""5 - Dictionary of Country Information"""

# Q2. Using examples, explain how the following methods work:
# - get, update, setdefault, popitem, pop

"""get: is used to retrieve the value associated with a given key. example:"""
car = {"brand": "Benz", "model": "SLS500", "year": 2023}
x = car.get("model")
print(x)

"""update: this method is used to update a dictionary with elements from another dictionary or from an iterable of key-value pairs. example:"""
car = { "brand": "Benz", "model": "C350", "year": 2020}
car.update({"color": "White"})
print(car)

"""setdefault: is a dictionary method that provides a way to set a default value for a key in a dictionary if the key is not already present. example:"""
car = {"brand": "Benz", "model": "C300", "year": 2022}
x = car.setdefault("model")
print(x)

"""popitem: this dictionary method removes and returns an arbitrary key-value pair from the dictionary. example"""
car = {"brand": "Benz", "model": "C300", "year": 2018}
car.popitem()
print(car)

"""pop: method for dictionaries is used to remove and return an item with the specified key. example:"""
car = {"brand": "Benz", "model": "S300", "year": 2021}
car.pop("model")
print(car)
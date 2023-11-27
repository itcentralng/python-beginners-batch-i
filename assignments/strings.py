# Q1. Practice all the methods treated today
# Q2. Explain how the following string methods work, with an example:
# - lower, replace, isupper, title, endswith, find, index, isalnum
# - join, split

test = "Ahmad Musa"
print(test.isalnum())
print(test.endswith('a'))
print(test.endswith('Musa'))
print(test.split())
print(test.split('a'))

people = ['Ahmad', 'Musa', "Sani"]

print(" ".join(people))

print(test.index('d'))
print(test.find('x'))

a = "ahmad musa"
print(a.title())
print(a.capitalize())
# Q1. Practice all the methods treated today
# Q2. Explain how the following list methods work, with an example:
# - index, sort, pop, insert, remove, reverse

items = ['Pencil', 'Cleaner', 'Ruler']
x = items.index('Ruler')
print(x)

items.sort()
print(items)

y = items.pop(1)
print(y)

y = items.pop()
print(y)

print(items)

items.insert(0, 'Biro')
print(items)

items.remove('Cleaner')
print(items)

items.insert(0, 'Fan')
items.insert(0, 'Cream')
print(items)

items.reverse()
print(items)
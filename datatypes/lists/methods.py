item = [1, 2, 3]

item2 = item.copy()

item.clear()

item.append('Something')
item.append('Somewhere')
item.append('Someone')

print(item)
print(item2)

print(item2.count(2))

item2.extend(item)

print(item2)

item2.pop()
item2.pop(0)
item2.pop(0)
print(item2)

item2.remove(3)
print(item2)

item2.reverse()
print(item2)
item2.sort()
print(item2)
shoppingList = ["Mango", "Coke"]
shoppingList.append("Banana")
print(shoppingList)
shoppingList.clear()
print(shoppingList)
shoppingList.append("Cashew")
shoppingList.append("Cashew")
shoppingList.append("Pineapple")
print('s', shoppingList)

a = shoppingList
print('a', a)
t = shoppingList.copy()
print("\n")
shoppingList.clear()
print(a)
print(t)
print(shoppingList)

print(t.count('Cashew'))
print(t.count('Cashews'))

x = ["Apple", "Orange"]

t.extend(x)
t.extend(("ABCD", "Musa"))

print(t)
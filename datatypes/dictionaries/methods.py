person = {"name":"Kabir Abdullahi", "age":12, "height":1.8, "weight":59.8}

color = {"name":"red", "feel":"warm", "status":"danger"}

print(color.get('name', 'Hello'))
print(color.get('feel', 'Hello'))
print(color.get('age', 'Hello'))
print(color.items())
print(color.keys())
print(color.values())
print(color.pop('status'))
print(color.popitem())
print(color)

color.setdefault("status", "danger")
color.setdefault("feel", "warm")
print(color)

person.update(color)
print(person)
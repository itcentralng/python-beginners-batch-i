student = {"name":"Aisha Yakubu", "dob":"10-10-2010", "class":"JSS 1", "score":200}
print(student)
# student.clear()
# print(student)

student2 = student.copy()
student2.clear()
print(student2)
print(student)

student2.setdefault("passport", "passport.jpg")

print(student.get("dob"))
print(student.get("passport", "https://storage.app/images/photo.jpg"))
print(student2.get("passport", "https://storage.app/images/photo.jpg"))

print(student.items())
print(student.keys())
print(student.values())

print(student.pop("dob"))
print(student)

print(student.popitem())

student.update(student2)

print(student)

student = {}

print(student.fromkeys(["name", "age"], ""))
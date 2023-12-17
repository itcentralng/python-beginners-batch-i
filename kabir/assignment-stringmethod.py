# Q1. Using examples, explain the following string methods:
# count, endswith, startswith, isdigit, casefold
# upper, lower, isupper, islower, replace

name = 'kabir abdullahi abubakar'

print(name.count ('a'))
print(name.endswith ('a', 1, 5))
print(name.startswith ('k', 0, 4))
print(name.isdigit())

name2 = 'KABIRU ABDULLAHi'
print(name2.casefold ()) 
print(name2.isupper ())
print(name2.islower ())
print(name.upper ())
print(name2.lower ())
print(name.replace ('kabir', 'musa'))


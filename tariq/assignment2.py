# Q1. Practice all the methods treated today
"""All practiced"""
# Q2. Explain how the following string methods work, with an example:
# - lower, replace, isupper, title, endswith, find, index, isalnum
# - join, split
"""lower: This simply signifies given lowercase to all the labeled string. examples"""
name = "Tariq"
print(name.lower())

item = "PAPER"
print(item.lower())

"""replace: as the name implies, this string method entails entails the replacement of a particular labelled item with another. example"""
name = "Tariq"
print(name.replace ("Tariq", "Nasir"))

y = "I love Manchester City"
print(y.replace("Manchester City", "Manchester United"))

"""isupper: this string method returns TRUE when all the word labelled are in capitals and returns FALSE otherwise. examples"""
text = "MTI LIMITED"
print(text.isupper())

text = "Mti Limited"
print(text.isupper())

"""title: this string method makes the first characters of a labelled word/words capitalized and the rest on lowercase. examples"""
x = "it central"
print(x.title())

animal = "HYENA"
print(animal.title())

"""endswith: this is used to check whether a sentence ends with a specific word. examples"""
sentence = "The boy is very brilliant"
print(sentence.endswith("brilliant"))

sentence = "The boy is very brilliant"
print(sentence.endswith("playful"))

"""find: this simply helps in finding a specific word or alphabet in a labelled string. example:"""
x = "this is just the beginning of somehing huge"
print(x.find("just"))

y = "Being punctual is the beginning of achieving something good"
print(y.find("of", 0, 50))

"""index: this is used to find the number of a specific word or alphabet in a sentence or word.examples"""
x = "This is very amusing"
print(x.index("amusing"))
print(x.index("e"))

"""isalnum: is a string method that checks whether all the characters in a given string are alphanumeric and it answered with TRUE or FALSE. examples:"""
y = "Manchesteris1"
print(y.isalnum())

text = "This is not the one"
print(text.isalnum())

"""join: this is used to join multiple of string words together to become one using assigned symbol.examples"""
words = ["Vamus", "IT", "Central!"]
result = " ".join(words)
print(result)

"""split: this is used to split a string into a list of substrings based on a specified word. examples:"""
animals = "Goat, Horse, Tiger, Hyena"
print(animals.split())

States = "Katsina, Abuja, Bauchi, Kano, Borno"
print(States.split())
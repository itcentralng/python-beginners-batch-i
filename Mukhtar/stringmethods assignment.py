# Q1. Practice all the methods treated today
# Q2. Explain how the following string methods work, with an example:
# - lower, replace, isupper, title, endswith, find, index, isalnum
# - join, split
 
# Q1 Practice all the methods treated today

#capitalize
name = "muhammad"
x = name.capitalize()
print(x)
# casefold
item = 'JAMBOX'
print(item.casefold())

# center
club = "juventus"
print(club.center( 17 ,'+' ))

# count
country = 'nigeria'
print(country.count('e', 0, 6) )

# Q2 Explain how the following string methods work, with an example:
# - lower, replace, isupper, title, endswith, find, index, isalnum
# - join, split
 
#  Upper is used to capitalize all the characters in a string
nigeria = 'country'
print(nigeria.upper())

# lower does the opposite of 'upper'
nigeria = 'COUNTRY'
print(nigeria.lower())

# endswith shows whether or not a character sequence ends with a particular letter
nigeria = 'country'
print(nigeria.endswith('_x'))

# find method tells the index of a particular character in a string sequence
nigeria = 'country'
print(nigeria.find("r"))
# or this .........which only tells us the first character 
print(nigeria.find("country"))

# replace method does replace either a character or the character sequence
item = 'JAMBOX'
print(item.replace('JAMBOX' , 'mango'))
# or 
item = 'JAMBOX'
print(item.replace('JAM' , 'man'))


# format 
item = 'JAMBOX'
message = f'{item} is loud'
print(message)

# index
nigeria = 'country'
print(nigeria.index('t'))

# isalnum..... returns T/F if the character has alphanumeric in a string
item = 'JAMBOX_'
print(item.isalnum())

#  title
month = 'ramadan'
print(month.title())

# isupper return t/f is the first character in a string is in uppercase
month = 'ramadan'
x = month.isupper()
print(x)

# join
i_months = 'ramadan', 'shawwal' ,'jan'
v = '_'.join(i_months)
print(v)

# or
i_months = 'ramadan' 'shawwal' 'jan'
v = '_'.join(i_months)
print(v)

# split
footballers = 'ronaldo, neymar, benzema'
players = footballers.split()
print(players)
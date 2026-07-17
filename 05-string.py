print(type('this is a text'))

print('this is a text')

username = 'supercoder'
password = 'supersecret' 

#string concatenation

print(username + ' ' + password)

long_string = '''
this is so fun to learn 
WOW
O O 
---
'''
print(long_string)


first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

#string concatenation

print(first_name + ' ' + last_name)

#type conversion 
a = str(100)
b = int(a)
c = type(b)
print(c)

#escape characters
weather = "it\'s \"kind of\" sunny day \n hope you have a great day"
print(weather)

#formatted strings
name = 'heiza'
age = 20
print(f"hello {name}, you are {age} years old")

#string indexes 

selfish = 'me me me'
         #'01234567'
print(selfish[3])
 
#[start:stop:step] - called string slicing
print(selfish[0:8:2])
#indexes can also be negative 
print(selfish[-1])
#or 
print(selfish[::-1]) #this will reverse the string  

#immutability of strings - strings in Python are immutable, meaning once they are created, they cannot be changed,
#they can only be reassigned to a new string.
 
#built in functions 

quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be', 'me'))

#booleans
is_cool = True
is_hot = False
print(bool(1))
print(bool(0))

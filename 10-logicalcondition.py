# Conditional Logic
# use of if else , elif , else statements
is_old = True
is_licenced = True

if is_old:
    print('You are old enough to drive!')
elif is_licenced:
    print('You can drive now!')
else:
    print('You are not of age!')

print('ok ok')
print()

# improved version
if is_old and is_licenced:
    print('You are old enough to drive, and you have a licence!')
else:
    print('You are not of age!')

print('ok ok')

# truthy and falsy values
# these are values that evaluate to True or False in a boolean context
# falsy values: False, None, 0, '', [], {}, set(), range(
# truthy values: True, 1, 'hello', [1, 2, 3], {'a': 1}, {1, 2, 3}, range(1)

username ='hello'
password = '1234'

if username and password:
    print('You are logged in!')
else:
    print('Please enter a username and password!')   

print('ok ok')
print(bool(''))  # False
print(bool('hello'))  # True

#TERNARY OPERATOR
# a shorthand way of writing an if else statement
# condition_if_true if condition else condition_if_false
is_adult = True
can_drive = 'Yes' if is_adult else 'No'
print(can_drive)

is_friend = True
can_message = 'Message allowed' if is_friend else 'Not allowed to message'
print(can_message)

#exercise
is_magician = False
is_expert = True
if is_magician and is_expert:
    print("you are a master magician")
elif is_magician and not is_expert:    
    print("atleast you are getting there")
elif not is_magician:
    print("you need magic powers")    
#for loops used for iterating over a sequence (list, tuple, dictionary, set, or string)
for item in 'Python':
    print(item)
print(item)  # This will print the last item in the string 'Python'

for item in [1,2,3,4,5]:
    for x in ('a','b','c'):
        print(item, x)
print(item)  # This will print the last item in the list [1,2,3,4,5]

#iterable - list, tuple, dictionary, set, string
#iterate - to go through each item in an iterable
# iteration - the process of going through each item in an iterable
user = {
    'name': 'John',
    'age': 25 ,
    'address'  :  "123 Main St"
}

for item in user.items():
    print(item)  # This will print each key-value pair in the dictionary as a tuple
for item in user.values():
    print(item)  # This will print each value in the dictionary
for item in user.keys():
    print(item)  # This will print each key in the dictionary        

#counter exercise 

my_list = [1,2,3,4,5]
counter = 0
for item in my_list:
    counter = counter + item 
    print(counter)  # This will print the running total of the sum of items in the list
print(counter)  # This will print the sum of all items in the list, which is 15        

#range() function - generates a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
for item in range(5):
    print(item)  # This will print numbers from 0 to 4
for item in range(0,10,2):
    print(item)  # This will print even numbers from 0 to 8
for _ in range(10, 0 , -1):
    print(_)  # This will print numbers from 10 to 1 in descending order
for item in range(2):
    print(list(range(5)))  # This will print the list [0, 1, 2, 3, 4] two times

#enumerate() function - adds a counter to an iterable and returns it in a form of enumerate object. 
#This enumerate object can then be used directly in for loops or be converted into a list of tuples using the list() method.
#using this function we can get the index of the item in the iterable

for index, item in enumerate(['a','b','c']):
    print(index, item)  # This will print the index and the corresponding item in the list
for i,char in enumerate('python is cool'):
    print(i,char)  # This will print the index and the corresponding character in the string    

for i,item in enumerate(range(100)):
    if item == 50:
        print(f'index of 50 is {i}')  # This will print the index of the item 50 in the range from 0 to 99
        
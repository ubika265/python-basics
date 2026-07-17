#functions are defined using the def keyword, followed by the function name and parentheses. 
# The code block within every function starts with a colon (:) and is indented.
# it is used to group a set of statements together so they can be run more than once.
# it can take parameters and return values.
# using functions allows us to break our program into smaller and modular chunks, making it more organized and manageable.

def greet():
    print("Hello, welcome to the program!")

greet()   # this is a function call for a simple function 

# parameters are variables inside the defined function 
# example 
def greet(name , emoji):
    print(f'hello {name}{emoji}, welcome to the program!')#here name and emoji are parameters 

#arguments are the actual values given to the parameters while function call 
#example 
greet('ubika', '😉')  #here ubika and 😉is the argument (positional arguments)
greet(emoji = '😁', name = 'bibi') #these are keyword arguments 

#types of arguments 
# positional arguments 
# keyword arguments
# default arguments 

def greet(name ='drath vrader', emoji = '😈'):
    print(f'hello {name}{emoji}, welcome to the program!')#here name and emoji are parameters 
greet('ubika', '😉')  
greet(emoji = '😁', name = 'bibi')
greet() #no actual parameters - default will be implemented
greet('pookie') 

#functions must modify or return something 
#should do one thing really well or
#should return something #return exits the function 
def add(num1 , num2):
    return num1 + num2  # if return is not used , print function will print 'none'

print(add(3,5))

def sum1(num1 , num2):
    def another_func(n1,n2):
        return n1 + n2
    return another_func(num1 , num2)

total = add(10,20)
print(total)

#Methods vs Functions 
# Methods example - these functions have dot in front of them
'hello'.capitalize
#functions examples 
def some_randome():
    pass 

#docstrings are comments added in a function , which gives info to the user 
#example 
def test(a):
    '''
    INFO: PRINTS OR RETURNS THE PARAM a
    '''
    print(a)
test(1)    
help(test) #tells what a function does 
print(test.__doc__) #tells what a function does  

#clean code example 
#before
def is_even(num):
    if num % 2 == 0:
        return True 
    elif num % 2 != 0:
        return False 
#after 
def is_even(num):
    return num % 2 == 0
print(is_even(51))

# *arg and **kwargs
def super_func(*args):
    print(args)
    return sum(args)
print(super_func(1,2,3,4,5))

#using *arg any number of arguments can be accepted, other variable can also be used to represent it ex, *hooo
# using **kwargs any number of keyword arguments can be given .
def super_func1(*args , **kwargs):
    total = 0
    for items in kwargs.values():
      total += items
    return sum(args) + total
print(super_func1(1,2,3,4,5, num1=5, num2=10))

#Rule : params, *arg , default parameters , **kwargs




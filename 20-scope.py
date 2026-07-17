#Scope - what variables do i have access to?
# variales declared inside a function can not be used outside the function - functional scope 
# variables declared outside a function, can be accesses anywhere in the file - global scope
#RULES 
#1- start with local scope ( checks inside function if func is called )
#2 - parent local ?
#3 - global
#4 - built in python functions

#The global keyword allows a function to modify a variable declared outside all functions (a global variable).
x = 10      # Global variable

def change():
    global x
    x = 20

change()
print(x)

x = 10
#--------
def change():
    x = 20      # Local variable

change()
print(x)

#The nonlocal keyword is used in nested functions to modify a variable from the enclosing (outer) function.
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()
# global example
count = 0

def increment():
    global count
    count += 1

increment()
print(count)      # Output: 1
# nonlocal example
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1

    increment()
    print(count)

counter()         # Output: 1
# scope help not clog up computers memory and to run programs efficiently 
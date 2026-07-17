# while loop used for repeated execution as long as an expression is true
# while loop is used when we don't know how many times we want to execute a block of code, but we want to keep executing it as long as a certain condition is true.
i = 0
while i < 50:
    print(i) # This will print numbers from 0 to 49
    i += 1  # This increments the value of i by 1 in each iteration
else:
    print('i is no longer less than 50')  # This will print when the while loop condition is no longer true    

while True:
    response = input('say something: ')
    if response == 'bye':
        break # This will exit the loop if the user types 'bye'

# break statement is used to exit a loop prematurely, even if the loop condition is still true. 
# It is often used in conjunction with an if statement to exit the loop when a certain condition is met.    

#continue statement is used to skip the rest of the code inside the loop for the current iteration only.
# The loop does not terminate but continues on with the next iteration.


#pass statement is used as a placeholder for future code.
# It is a null operation; nothing happens when it executes. It is useful in situations where your code will eventually go, but you haven’t written it yet.
# it just allows the code to run without throwing an error, but it does not perform any action.

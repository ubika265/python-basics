
user_name = input("Enter your username: ")
password = input("Enter your password: ")

password_length = len(password)
password2 = '*' * password_length

print(f"{user_name}, your password is {password2} , it is {password_length} characters long.")
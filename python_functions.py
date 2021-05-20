# Let's create a basic function to gree
# Syntax def name()

# First Iteration
# def greetings():
#     return "Welcome to Cyber Security!" # you need to call the funtion in order for you to execute the command
#
# print(greetings())

# Second Iteration

# def greeting_user(name):
#     return "Welcome on board!"
#
# print(greeting_user("engineering 88"))

# Exercise: Take user name as input() and display it back to them with greeting messages of your choice

user_name = str(input("What is your name? "))

def greet_user(user_name):
    return "Welcome " + user_name

print(greet_user(user_name))
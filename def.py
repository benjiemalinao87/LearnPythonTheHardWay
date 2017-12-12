#function for name and age, hardcoded! in the program
def name_age(arg1_name,arg2_age):
    print('Welcome, {arg1_name}!')
    print('You are {arg2_age}} years old!\n Wow thats young! You can do whatever you want!')
    
# Used a variable for the name and age
print('the name and age below came from a variable')
name = 'Benjie'
age = 30

name_age(name, age)

# We get the name and age form the user's input
print("This name and age are from user's input")
print('What is your name: ')
name_in = str(input())
age_in = int(input())

name_age(name_in,age_in)

from sys import argv

script = argv
prompt = f'{script}  > '

print(f'Hi, what is your name:  ')
user_name = input (prompt)

print (f'Ok,Id like you to ask a few questions {user_name}.')
print (f'Do you like me {user_name}? ')

like = input (prompt)

print (f'Where do you live {user_name} ')
live = input(prompt)

print ('How old are you {user_name}? ')
age = int(input(prompt))

print ('What kind of computer do you have? ')
computer = input (prompt)

print (f"""
Alright, so you said {like} about liking  me.
You live in {live} and you are {age} years old. Not soure where that is though.
And you have a {computer} machine. Nice
""")

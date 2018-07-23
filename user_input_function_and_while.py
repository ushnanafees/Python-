name = input("Hey there, whats your name:")
print(name)

message = input("When will you there? I have an important work to you")
print("I am waiting for you there.")

prompt = ("I want to meet with you since last week. I want to talk with you.")
prompt += ("I was text you but you didnt reply")
name = input(prompt)
print(name)

# int() to accept numerical input
age = input("How old are you?")
age = int(age)
age >= 18

age = input("How old are you??")
age = int(age)
age <= 18

height = input("What is your height in inches??")
height = int(height)
if height >= 36:
    print("You are tall enough to ride!")
else:
    print("You will able to ride when you are little older")

# modulo operator
number = input("Enter a number and I will tell you its an even or odd")
number = int(number)
if number % 2 == 0:
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number)+ " is odd.")

# while_loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\n Tell me something and I will repaet it back to you."
prompt += "\n Enter 'quit' to end the program"
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# using flag
prompt = "\n Tell me something and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program \n"
active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)

prompt = "\n Tell me something and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program "
active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    elif message == 'Hello':
        active = True
    elif message == 'Game over':
        active = False
    else:
        print(message)
        
prompt = "\n Enter the city which you have visited:"
prompt += "\n Enter 'quit' if you completed "
active = True
while active:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd like to go to " + city.title() + "!")
        
# exercise
prompt = "\n Tell me your age and I will tell the cost of ticket:"
active = True
while active:
    age = input(prompt)
    age = int(age)
    if age < 3:
        
        print("The cost is free")
    elif age < 12:
        print("The cost is 12$")
    elif age > 12 :
        print("The cost is 15$")
    else:
        print(age)

# while loop with list
unconfirmed_users = ['Alice','Brane','Canadan']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying users:" + current_user.title())
    confirmed_users.append(current_user)
     
print("The following users are confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# Removing an instance from list using while loop
pets = ['cat','dog','rabbit','cat','lion','parrot','dog']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


# Looping through list

my_friends = ['john','alice','david','emma','micheal']
for friend in my_friends:
    print(friend)
    
# Printing a message with list

for friend in my_friends:
    print(friend.title() + ", Have a nice day!")
    print("Meet you next time " + friend.title() + ".\n")
    
 # Working with numeric list
 # Range() Function
for num in range(1,7):
     print(num)


# Using range() to make a list of Numbers
     
numbers = list(range(1,10))
print(numbers)  

# Print list of even_numbers using range()

even_number = list(range(2,11,2))
print(even_number)

squares = []
for num in range(1,6):
    squares.append(num**2)
print(squares)    
    
# Simple Statistics with a list of Numbers

num = [22,99,100,00,45,35,60,20,3,9]
print(max(num))
print(min(num))
print(sum(num))

# List Comprehension

squares = [value**2 for value in range(1,11)]
print(squares)

# Slicing a list

my_friends = ['john','alice','david','emma','micheal']
print(my_friends[0:4])
print(my_friends[-3:])  

# Copying a list

my_friends = ['john','alice','david','emma','micheal']
your_friends = my_friends[:]
print("My friends are:")
print(my_friends)
print("Your Friends are:")
print(your_friends)

    

   
    
 
# List of my cars
my_cars = ['audi','bmw','civic','city','corolla','vitz']
print(my_cars)

# Accessing elements in list
# Index starts with 0 in list
print(my_cars[0].title())      # at index 1 with title case
print(my_cars[2].upper())      #at index 2 with upper case


# Finding the last element in list [-1] always print last element 
print(my_cars[-1])

# Using individual value from list
first_car = ("My first car was "+ my_cars[-1].title() +" !")
print(first_car)

# using individual values from list
for i in my_cars:
    print(i)

# Modifying elements in list
my_cars[3] = 'swift'
print(my_cars)

# Adding elements in list
# Append element to the end of list 
my_cars.append('city')
print(my_cars)

# Inserting elements to the list
my_cars.insert(0, 'Mira')
my_cars.insert(3, 'alto')
print(my_cars)
 
# Removing elements using del Statement
del my_cars[0]
del my_cars[1]
del my_cars[4]
print(my_cars)

#Removing elements using pop() Method
pop_item = my_cars.pop(0)
print(my_cars)
print(pop_item)

# Removing elements by value
my_cars.remove('swift')
print(my_cars)

# Sorting a list Permanently
my_cars.sort()
print(my_cars)

# Sorting a list Temporarily
print(sorted(my_cars))      # Sorted list
print(my_cars)              # original list

# Printing a list in Reverse order
my_cars.reverse()
print(my_cars)

# Length of a list
print(len(my_cars))







     

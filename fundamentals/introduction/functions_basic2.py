#countdown
# 1 Create a function that accepts a number as an input.
# 2 Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(a):
    newList = []
    for i in range (a, -1, -1):
        newList.append(i)
    return newList
print(countdown(10))

#print and return
# Create a function that will receive a list with two numbers.
# Print the first value and return the second.

def printandreturn(list):
    print (list[0])
    return list[1]
print(printandreturn([1,2]))

#first plus length
# Create a function that accepts a list
# and returns the sum of the first value in the list plus the list's length.

def first_plus_length(list):
    x = len(list)
    y = list[0]
    return x + y
print(first_plus_length([1,2,3,4,5,6,7]))

#values greater than second
# Write a function that accepts a list
# and creates a new list containing only the values from the original list that are greater than its 2nd value.
# Print how many values this is
# return the new list
# If the list has less than 2 elements, have the function return False

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    if len(list) > 2:
        newList = []
        for val in list:
            if val > list[1]:
                newList.append(val)
        print(len(newList))
        return newList
print(values_greater_than_second([4,2,6,9,1,2]))
print(values_greater_than_second([4]))
print(values_greater_than_second([40,35,77,95,33,201]))
print(values_greater_than_second([-10,-9,-4,6,0,1,3]))

#this length, that value
# Write a function that accepts two integers as parameters: size and value.
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def this_length_that_value(size, value):
    newList = []
    for i in range (size):
        newList.append(value)
    return newList
print(this_length_that_value(10,2))
print(this_length_that_value(5,8))
print(this_length_that_value(7,7))
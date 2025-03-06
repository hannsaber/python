"""
1 Countdown - Create a function that accepts a number as an input. 
*Return a new list that counts down by one, from the number 
(as the 0th element) down to 0 (as the last element).
Example: countdown(5) should return [5,4,3,2,1,0]

"""
def countdown (n):
    x=range(n,-1,-1)
    for n in x:
        print(n)
countdown(5)
def countdown2 (num):
    output=[]
    for i in range (num,-1,-1):
        output.append(i)
    return output
print (countdown2(5))
"""
2 Print and Return - Create a function that will receive a list with two numbers. 
Print the first value and return the second.
"""
def print_return(list):
    print(list[0])
    return (list[1])
print(print_return([1,2]))
"""
First Plus Length - Create a function that accepts a list and 
returns the sum of the first value in the list plus the list's length.

"""
def first_plus_length(list):
    sum =list[0]+len (list)
    return sum 
print (first_plus_length([1,2,3]))

"""
Values Greater than Second - Write a function that accepts a list and creates a new list 

containing only the values from the original list that are greater than its 2nd value. 
Print how many values this is and then return the new list. 
If the list has less than 2 elements, have the function return False
"""
def value_greater(list):
    if len(list)<2:
        return False
    output=[]
    for i in range (0,len(list)):
        if list[i]>list[1]:
            output.append(list[i])
    print (len(output))
    return output
print(value_greater([5,2,3,2,1,4]))
print(value_greater([3]))

"""
This Length, That Value
"""
def thislength_value(size,value):
    output=[]
    for i in range (0,size):
        output.append(value)
    return output
print (thislength_value(7,2))





    

# Create a function that accepts a number as an input. Return a new list that counts down by one, from the number  down to 0 

def countdown(a):
    b=[]
    for x in range(a,-1,-1):
      b.append(x)

    return b

print(countdown(5))

#Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_and_return(b):
    print(b[0])
    return b[1]
print( print_and_return([2,1])) 

#Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_length(b):
    sum=b[0]+len(b)
    return sum

print(first_plus_length([1,5,6,3]))    

# Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd
def values_greater_than_second(b):
    new_b = []
    if len(b) > 1:
        for x in range(0,len(b),1):
            if b[x] > b[1]:
                new_b += [b[x]]
        
        return (new_b)
    
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


 # Write a function that accepts two integers as parameters: size and value

def length_and_value(s,v):
    new_list = []
    for x in range (0,s,1):
        new_list += [v]
    return new_list

print(length_and_value(5,8))









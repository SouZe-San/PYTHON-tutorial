# Creating a tuple using ()
'''
Tuple are orderable can access by index but Cannot change or add any element after create
'''
t = (1, 2, 4, 5,3,2,4,2,1,1,10,3,4,2,2,"heki",True) 
# can have multiple elements 
# t1 = () # Empty tuple
# t1 = (1) # Wrong way to declare a Tuple with Single it assume that given one element to t1
t1 = (1,) # Tuple with Single element
print(t1)

# Printing the elements of a tuple
print(t[0])

# Cannot update the values of a tuple
# t[0] = 34 # throws an error

# ....... Method ////
print(t)
print(t.count(1)) # give how many times that element present in that tuple
print(t.index(5))
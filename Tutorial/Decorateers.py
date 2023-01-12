# ][[[[[[[[[[[[[[[[[[   LAMBDA FUNCTION ]]]]]]]]]]]]]]]]]]
# def func(a):
#     return a+5

# simple function Code can write in One Line
func = lambda a: a+5
square = lambda x: x*x
sum = lambda a, b, c: a+b+c  # Send multiple Items

x = 3
print(func(x)) # Prints 8
print(square(x)) # Prints 9
print(sum(x, 1, 2)) # Prints 6


# [[[[[[[[[[[[[[[[[[[[ .JOIN ]]]]]]]]]]]]]]]]]]]]
# use in any iterable obj, connect items of list/set/tuple by something and convert them into full string

l = ["Camera", "Laptop", "Phone", "ipad", "Hard Disk", "Nvidia Graphic 3080 card"]
sentence = "~~".join(l) # insert after every item and Join in one string
# sentence = "==".join(l)
# sentence = "\n".join(l)
print(sentence)
print(type(sentence))


# [[[[[[[[[[[[[[[[[[ Format String ]]]]]]]]]]]]]]]]]]]
# it Used in Past now use f-String
name = "Souze"
wort = "Nothing"
type = "Coding"
a = "I {} have {} and do this {}".format(name, wort, type)
# also can pass the index of parameters
b= "I have {1} and {0} do this {2}".format(name, wort, type)
print(a)
print(b)


# [[[[[[[[[[[[[[[[[[[[[[ Map ]]]]]]]]]]]]]]]]]]]]]]
# uae to apply one function on every element of an given list
#  map(function, list) : return type <class 'map'>
def cube(num):
    return num ** 3

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
# Method 1 # long---
# l2 = []
# for item in l1:
#     l2.append(cube(item))
# print(l2)
 
l2 = list(map(cube, l1))  # Can be done One Line
print(l2)


# {[[[[[[[[[[[[[[[[[ Filter ]]]]]]]]]]]]]]]]]}
#filter(function, list ) : return <class 'filter'>type
# Sorting List_items according passing function  ,,
greater_than_5 = lambda x : x>5
print(list(filter(greater_than_5,l1)))


# [[[[[[[[[[[[[[[ Reduce ]]]]]]]]]]]]]]
# apply the given function to every sequential pair in given list
# {(0,1),(1,2),(1,3),(3,4)...  } like take input
#  THE FUNCTION MUST HAVE ONLY 2 PARAMETERS not more than
from functools import reduce

sum = lambda a, b: a+b
l = [1, 2, 3, 4,6,4,3,32,4,3,5]
val = reduce(sum, l)
print(val)
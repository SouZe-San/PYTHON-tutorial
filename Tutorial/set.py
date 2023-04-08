"""
Set is as we know , it collection elements
A set is a collection which is unordered, unchangeable*, and unIndexed.
 we can add/remove element but cannot modify them like list/dict...
 --> Set don't posses Same element Multiple time
 --> As list and dict can be modified that why we can't add them In Set but can add Tuple as it cannot modify after creation


"""
a = {3, 4, 23, 42, 234, 2, 4, 42, 23} 
print(a)  # --> If any elements preset more than one time that element only print only one time

# An empty set can be created using the below syntax:
b = set() ## --> this is a empty set

#------------ Methods --------------------------------
b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4, 5, 6)) # add a tuple
print(len(b)) # Prints the length of this set
b.remove(4) # Removes 5 from set b... Take element as parameter -- if the Argument doesn't exist in set then it throw an error
print(b) # Whatever Way put It print in Sorting
print(b.pop()) # --> Remove the  first element of set and return it



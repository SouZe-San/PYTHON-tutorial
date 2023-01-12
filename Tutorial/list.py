
#  List is like array , can access by index, orderable, immutable --> change the elements after create
# We can create a list with items of different types
c = [45, "Harry", False, 6.9]
# Access using index using a[0], a[1], a[2]
print(c[2])

# Change the value of list using
c[0] = 98
print(c)
#  Can Apply slice method in list just like string 
friends = ["Dj", "Tom", "Rohan", "Sam", "Divya", 45]
print(friends[0:4]) # --> print 0 to 3 index elements
print(friends[-4:]) # 6-4 = 2  print from 2 to all index elements

# ==============-     method =================
l1 = [1, 8, 7, 2, 21, 15]
print(l1)
# l1.sort() # sorts the list --> return nothing Change the original
# l1.reverse() # reverses the list
#l1.append(45) # adds 45 at the end of the list 
# l1.insert(2, 544) # inserts 544 at index 2
# l1.pop(2) # removes element at index 2 -- take index as inout
l1.remove(21) # removes 21 from the list -- take the element as inout what have to delete
print(l1)


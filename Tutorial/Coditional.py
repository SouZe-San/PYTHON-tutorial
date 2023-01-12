a = 8
# Here present two Ladder 
if(a<3): 
    print("The value of a is greater than 3")
if(a>7):
    print("The value of a is greater than 7")
elif(a>17):
    print("The value of a is greater than 17")
else:
    print("The value is not greater than 3 or 7")

'''
  in python there some key word that --> 
  "is" :-->  if (a is None): means that if a is (==) None => return true else false
  "in" :--> if (4 in a): means that if 4 includes in a list/set/tuple/dict  then return true
'''
a = None
if (a is None):
    print("Yes")
elif(a is 49):
    print("r u blind")
else:
    print("No")

llist = [45, 56, 6]
print(435 in llist)

#  Pass : it help to --- execute program withOut Complete the if-else/function/loop complete

def ouch(player):
    pass

if a>0:
    pass

while a>6:
  pass
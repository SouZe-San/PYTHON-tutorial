'''
* * * *
*     *
*     *
* * * *

'''

for i in range(4):
    if i == 0 or i == 3:
        for j in range(4):
            if j == 3:
                print("* ")
            else:
                print("* " , end="")
        
    else:
        print("*", end="")
        print(" "*5, end="")
        print("*")

# * In python there are several type of loop
# 1. while
# 2. for in
# 3. for in range(start, stop, increment/rhythm)   --> It just like normal for loop (initialize; stopCondition; increment)


fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']

# @  1. while ----------------->
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
print('\n')

# @ 2. for in ===========>
for item in fruits:
    print(item)

# @ 3. for in range(_start, _stop, _step) ---------------> Only Count Number
for i in range(0, 4, 1):  # this syntax is like Starting i=0 , stop if i=3 and i+1 every iteration
    print(i, fruits[i])

#  We can add else statements after the for loop that Only execute after the loop completely finished
for i in range(10):  # --> by this it takes 0 to 9 ever time increment by 1
    print(i)
else:
    print("This is inside else of for")

# [[[[[[[[[[[[[ Continue - Brake]]]]]]]]]]]]]
for i in range(10):
    if (i == 3):  # if i=5 without further execute continue the loop
        continue
    print(i)
    if i == 6:  # Here As at i= 8 the loop break with out complete thats why else not shown
        break
else:  # this else not include if-else ladder it connect with loop
    print("This is inside else of for")

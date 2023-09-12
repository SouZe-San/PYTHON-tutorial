
# ! PROGRAM 3: print the series of numbers from 10-21 but do not print 15 & 18.

# in the range function the  Lower BOUND ARE inclusive and the UPPER BOUND Exclusive
for i in range(10, 21):
    if i == 18 or i == 15:
        continue
    print(i)


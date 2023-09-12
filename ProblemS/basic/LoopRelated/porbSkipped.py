
# ! PROGRAM 4: .perform a program in which take input of range for numbers to be print and take an input of the number to be skipped in the series.
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the Upper bound: "))
skippingNumber = list(map(int, input("give the Skipped values in a line: ").split()))

for i in range(lower_bound, upper_bound):
    if (i in skippingNumber):
        continue
    else:
        print(i)

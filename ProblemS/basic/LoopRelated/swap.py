
# ! PROGRAM : 1: Swapping of 2 varbers without using 3rd variable

# * Swapping the Numbers Without 3rd variable .. Static input 
print("-----:::: In Static Mode ::::---")
a = 10
b = 20
print("The First number was: " ,a)
print("The second number was: " ,b)
a = a + b
b = a-b
a = a-b
print("The First number is: " ,a)
print("The second number is: " ,b)

# * Swapping the Numbers Without 3rd variable .. Dynamic input 
print("-----:::: In Dynamic Mode ::::---")
var1 = input("\n Enter The first input: ")
var2 = input(" Enter The second input: ")
var1 = var1, var2
var2 = var1[0]
var1 = var1[1]
print("The First input is: " ,var1)
print("The second input is: ",var2)

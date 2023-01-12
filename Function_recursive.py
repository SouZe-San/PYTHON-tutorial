#   ITERATIVE WAY: 
def factorial(num):
    f = 1;
    for i in range(1, num+1):
        f = f * i
    return f

#   RECURSIVE WAY
def facto(number):
    if number == 0 or number == 1:
        return 1
    return number* facto(number-1)

print(f"The factorial of 5 in Iterative way: {factorial(5)}")
print(f"The factorial of 5 in Recursive way: {facto(5)}")

#   FIBONACCI SERIES -------
def fibo(num):
    if num == 0:
        return 0
    elif  num == 1:
        return 1
    return fibo(num-1) + fibo(num-2)

print(f"In 8th position of fibonacci series the element is: {fibo(8)}")
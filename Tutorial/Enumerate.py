# {{{{{{{{{{{{{ import Other Py file}}}}}}}}}}}}}
import Try_Except as T_E

# --> Can Use Other File's Function Which Not Define in This file
T_E.greet(",sir!")


"""
Global variables --=-==>  are Those Are can Used Every Where...
if We create a variable in Function with same name, still it will be be a Local variable those only exist in the function
"""

a = 54  # Global variable


def func1():
    a = 8  # Local Variable, the value of global'a' will not change ,, a value only in the function
    print(f"Print statement 2: {a}")


def func2():
    global a  # if used this syntax then it Originally assigned the Global variable in function
    print(f"Print statement 1: {a}")
    a = 8  # Local Variable if global keyword is not used
    # the Change is in  the Global variable
    print(f"Print statement 2: {a}")


func2()
print(f"Print statement 3: {a}")

# ^ Enumerate ----> it helps to use both Index and item in loop of any Iterable object(list, set, tuple)
# foe Print one by One use foe in loop but Cant get Index withOut count  ---> the Syntax in loop "first Index then Item "

list = [32, 4, 12, 54, 7, True, 4.23, 53.34, "baby"]
print(list)
for index, item in enumerate(list):
    print(f"in {index} index the item is : {item}")

# When have to Sorting any Iterable items in An specific Condition then this Method should be Convenient
list = [3, 6, 7, 8, 9, 2, 4, 1, 4, 2, 4, 1, 2, 3, 23, 75, 23, 123, 67]
# think Item have to sort in another list which are odd
print(list)
b = [item for item in list if item % 2 != 0]
# means take those item ,which are return true
print(b)

# Or Have to store in Set ;
set = {item for item in list}

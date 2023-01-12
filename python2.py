import os

# register section function


def register():
    return [input("User name : "), int(input("User id : "))]


# # longin section function
def login():
    return [input("User name : "), int(input("User id : "))]


# # input section function


def input_getting():
    if user_choise == 1:
        reg = register()
        os.system("clear")
        print("You have succesfully registered now log in")
        log = login()
    elif user_choise == 2:
        login()
    return [reg, log]


# # outss
key = 1
total_attempts = 3
print("\tThis is a login procedure\t")
user_choise = int(
    input("Type 1. to register\nType 2. sign in\nYour choise is :"))
input = input_getting()
print(input)
print(input[0][0])

# while total_attempts:
#     if (input[0][0] != input[1][0]) or (input[0][1] != input[1][1]):
#         print(f"you have {total_attempts} attempts left")
#         total_attempts -= 1
#         if total_attempts == 0:
#             break
#         user_choise = int(input("Type 1. to register\nType 2. sign in\nYour choise is :"))
#         input = input_getting()
#     else:
#       break

while total_attempts:
    if (
        (input[0][0] != input[1][0])
        or (input[0][1] != input[1][1])
        and (total_attempts != 0)
    ):
        print(f"you have {total_attempts} attempts left")
        total_attempts -= 1

        input = input_getting()
        break
    else:
        break

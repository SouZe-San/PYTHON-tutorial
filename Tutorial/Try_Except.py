'''
If some try to division by zero then Normally programme will fail But now it not stop it work Normally end show the Problem
'''      
def divOfNumber():
    try:
        num1 = int(input("enter a number: "))
        div = 100 / num1
        return div    
    except ZeroDivisionError as e:
        print("Make sure you are not dividing by 0")
    except ValueError as e:
        print("Make sure, enter a valid Input Number") 
    except Exception as e:
        print("Problem Have Occurred")
        print(e)

i =0
while i<5:
    print(divOfNumber())
    i+=2


#^ -==-=-> can make Custom Exception,, but can't name of the ValueError
def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Don't Press Other than Numbers")

a = increment(input("Enter a number: "))
print(a)


#^ Try with Else ---=> the else Path Only Shown if Try Success 
try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print(e)
else:
    print("Thanks for Enter a number")

#^ try_except_finally : ----> 
# the finally Execute Whatever happens... even the Code Exit ,.. Other Code will not but After execute the finally-Statement the code wil execute ..

try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("We are done")

print("Thanks for using the program")



# ^-----------------------------------------------------
'''

        # !WHEN HAVE TO EXPORT A FILE TO ANOTHER FILE THEN :
         import m06_file1 :---> In this Way have to write file name which want to Import then The Whole File's Code Will run here
         m06_file1.greet("Harry")  : In this way can use function form Imported File
        ALSO CAN USE : import file_NAme as FN
                        FN.greet("hhr") : In this can short

    there is  a problem for writing like this THAt it It Export Whole as it then then, this file's operation will run in other file With out called

    That Why it Used in Exported file after define the class function/ after those want to export / before start main code
    if __name__ == "__main__":
        All file's print(__name__) : print this __main__
        it telling like if __main__ then Execute the further code........ For Other file where it export For that file it __name__ will be the file Name.. so those code will Npt Execute in those file

'''


def greet(name):
    print(f"Good morning, {name}")


print(__name__)  # ---> For this file print __main __ ,,,,, But IN Othe file It Shows the file Name and thats Why it Cant Pass the IF statement
if __name__ == "__main__":  # if Export Under COde will Not Execute in that file Only Upper COde will execute
    n = input("Enter a name\n")
    greet(n)

#! Import in Enumerate

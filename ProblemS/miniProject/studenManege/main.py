
# load All dependencies
from DatasetsOfStudent import possible_input_list_for_teach
from DatasetsOfStudent import possible_input_list_for_stu
from DatasetsOfStudent import list_of_possible_lists
from Student import Student
# from DatasetsOfStudent import student_info_lists


print("Welcome to the student management system")
print("Please enter your identity")
user_identity = input(
    "Type 'Student' for student and type 'Teacher' for teacher ").lower()


# this will be in util folder

def return_roll(user_roll, data_list, second_data_list=[]):

    if user_roll in data_list:
        return data_list[0]
    elif user_roll in second_data_list:
        return second_data_list[0]
    # else:
        # print("Your input is invalid try again later")


roll = return_roll(user_roll=user_identity, data_list=possible_input_list_for_stu,
                   second_data_list=possible_input_list_for_teach)
student = Student()

if roll == "student":
    print("Choose your option \n \n1.Display \n2.Search ")
    choice = input().replace(" ", "").lower()
elif roll == "teacher":
    print("___________________")
    print("Choose your option \n \n1.Display \n2.Search \n3.Accept \n4.Delete \n5.Update")
    choice = input().replace(" ", "").lower()


another_variable = ""
memorable_variable = choice

for list in list_of_possible_lists:
    if another_variable != "":
        break
    choice2 = return_roll(choice, data_list=list)
    if choice2 == None:
        choice2 = memorable_variable
    another_variable = choice2

print(another_variable)
match another_variable:
    case "display":
        student.display()
    case "search":
        roll = student.setRollNo()
        print(student.search(roll))
    case "accept":
        name, rN, s1, m1, s2, m2 = student.questions()
        student.accept(name, rN, s1, m1, s2, m2)
    case "delete":
        student.delete(student.setRollNo())
    case "update":
        student.update()

print("\n********* END ***********\n")
# print(student_info_lists)
# Student.another_variable(Student.questions())

# print( return_roll( user_roll = user_identity ) )

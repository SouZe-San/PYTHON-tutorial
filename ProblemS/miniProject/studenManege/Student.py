#
# Data form another fle
from DatasetsOfStudent import student_info_lists


class Student():
    def __init__(self, ):
        pass

    def questions(self):
        name = input("Enter your name ")
        rollno = input("Enter your roll no ")
        subject_one = input("Enter your subject one ")
        subject_one_marks = int(input("Enter your subject one marks "))
        subject_two = input("Enter your subject two ")
        subject_two_marks = int(input("Enter your subject two marks "))
        return name, rollno, subject_one, subject_one_marks, subject_two, subject_two_marks

    def setRollNo(self):
        rollNumber = input("Enter your roll no ")
        return rollNumber

    def display(self):
        for studentData in student_info_lists:
            print(studentData)
        # print(student_info_lists)

    def search(self, rn):
        # for index, data in enumerate(student_info_lists):
        for data in (student_info_lists):
            if rn == data["rollno"]:
                # return (data, index)
                return data

    def accept(self, name, rollno, subject_one, subject_one_marks, subject_two, subject_two_marks):
        self.name = name
        self.rollno = rollno
        self.subject_one = subject_one_marks
        self.subject_two = subject_two_marks

        newData = {
            "name": self.name,
            "rollno": self.rollno,
            subject_one: subject_one_marks,
            subject_two: subject_two_marks,
        }
        student_info_lists.append(newData)

    def delete(self, rollNo):
        data = {}
        data = self.search(rollNo)
        if data == {}:
            print("Sorry You have Put Wrong UID \nThis ULD not Present in database")
        else:
            student_info_lists.remove(data)
            print("Delete Success")

    def update(self):
        old_rollNo = input("Enter your Old roll no : ")
        new_rollNo = input("Enter your New roll no : ")
        data = {}
        # Finding , is the ULD exist or not
        data = self.search(old_rollNo)
        if data == {}:
            print("Sorry You have Put Wrong UID \nThis ULD not Present in database")
        else:
            # Update the roll number in the dataList
            index = student_info_lists.index(data)
            student_info_lists[index].rollno = new_rollNo
            print("Update Success !!")

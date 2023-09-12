import sys

def lengthTuple(tup):
    count =0
    for i in tup:
        count+=1
    return count

def maxMini(tuple):
    max = 0
    min = sys.maxsize
    for i in range(0, len(tuple)):
        if tuple[i] < min:
            min = tuple[i]
        if tuple[i] > max:
            max = tuple[i]
    print("Maximum in Tuple is : ", max)
    print("Minimum in Tuple is : ", min)

def sumOfTuple(tuple):
    sum = 0
    for i in range(len(tuple)):
        sum += tuple[i]
    print("Sum Of Tuple is : ", sum)

def cubeTuple(tup): 
    return list(map(lambda x: (x,x**3), tup))

if __name__ == '__main__':
    t1 = (2,3,27,33,23,24,4,23,2,100,6,4,7,45,73,75,40)

    # !problem 1: Python program to Find the size of a Tuple
    # print(lengthTuple(t1))
    # # !problem 2: Python – Maximum and Minimum K elements in Tuple
    # maxMini(t1)
    # # !problem 3: Sum of tuple elements
    # sumOfTuple(t1)
    # !problem 4: Row-wise element Addition in Tuple Matrix
    tup1 = ((1,2,3),(4,5,6),(7,8,9))
    
    # ----------------------------------- extra --------------
    # col_no = int(input("Enter the number of columns: "))
    # row_no = int(input("Enter the number of rows: "))
    # tup=()
    # for i in range(row_no):
    #     tup += tuple(map(int, input("Enter row's input: ").split(" ")))
    # count = 0
    # for i in range(row_no*col_no):
    #     if count ==0 :
    #         print("(", end="")
    #     print(tup[i], end=",")
    #     count += 1
    #     if count == col_no:
    #         count = 0
    #         print(")")
       
            
    # !problem 5: Create a list of tuples from given list having number and its cube in each tuple
    print(cubeTuple(t1))
    
    
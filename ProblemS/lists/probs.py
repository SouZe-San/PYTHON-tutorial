def swapListNumber(list,len):
    list[0],list[len-1] = list[len-1], list[0]
    return list

def swapAnyNumberInList(list,pos1, pos2):
    temp = list[pos1]
    list[pos1] = list[pos2]
    list[pos2] = temp
    return list

def length(list):
    count =0
    for i in list:
        count+=1
    return count

def isMin(num1, num2):
    print("The Minimum is: ",num1 if num1<num2 else num2)
    
def isMax(num1, num2):
    print("The Maximum is: ",num1 if num1>num2 else num2)

def maxMinInList(l1):
    l1.sort()
    print("\nThe Max Element in List Is : ", l1[len(l1)-1])
    print("The Min Element in List Is : ", l1[0])

        
if __name__ == "__main__":
    l1 = [2,3,27,33,23,24,2,4,23,4,2,100,6,4,7,45,73,75,4]
    # l1 = input("Enter a list: ")
    
    # @ LIST PROBLEMS ---->
    
    # ! Problem 1 : Swap last and first element
    # List = list(map(int,input("Enter The List: ").split()))
    # print("Swap Last and first element-->")
    # print(swapListNumber(List,len(List)))
    
    # ! Problem 2: swap any number in list
    print("\n\n List: ", l1)
    print(swapAnyNumberInList(l1, int(input("Enter the 1st position: ")), int(input("Enter the 2nd position: "))))
    
    #! Problem 3: Length Of a List 
    print("\n\n the Length of List is: ",length(l1))
    
    # ! Problem 4: Maximum / Minimum of two numbers in Python
    isMin(int(input("enter 1st Number: ")),int(input("enter 2nd Number: ")))
    isMax(int(input("enter 1st Number: ")),int(input("enter 2nd Number: ")))
    maxMinInList(l1)
   
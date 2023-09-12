import sys

def lengthOfSet(set):
    count =0
    for i in set:
        count+=1
    return count

def maxMini(set):
    max = 0
    min = sys.maxsize
    for i in set:
        if int(i) < min:
            min = int(i)
        if int(i) > max:
            max = int(i)
    print("Maximum in Tuple is : ", max)
    print("Minimum in Tuple is : ", min) 

def commonElement(set1, set2):
    if (set1 & set2):
        print("Yes! common element present")
        return True
    else:
        print("No! common element not present")
        return False

if __name__=='__main__':
    s1 = {1,2,3,4,23,5,45,62 ,24 ,31 ,4}
    
# ! Problem 1.Find the size of a Set in Python
    print("The Length of Set is: ",lengthOfSet(s1))
    
# ! Problem 2.Iterate over a set in Python
    for value in s1:
        print(value)
        
# ! Problem 3.Maximum and Minimum in a Set
    maxMini(s1)
    
# ! Problem 4.Remove items from Set
    print("Before Remove any element:: ", s1)
    remove_item = int(input("enter Remove Element: "))
    s1.remove(remove_item)
    print("After Remove element:: ", s1)
    
# ! Problem 5.Check if two lists have at least one element common
    s2 ={3 ,32,5,66,75,76,8,54,34}
    
    print(s1)
    print(s2)
    commonElement(s1,s2)
    
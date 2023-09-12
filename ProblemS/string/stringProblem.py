    
def isPalindromeOrSymmetric(string):
    
    half_len = len(string)//2
    if len(string)%2 == 0:
        first_half = string[: half_len]
        end_half = string[half_len:]
    else:
        first_half = string[: half_len]
        end_half = string[half_len+1:]
    
    #Check Symmetries
    if first_half == end_half:
        print("Yes, The Given String Is a Symmetrical")
    else:
        print("No, The Given String Is Not a Symmetrical")
    #Check Palindrome
    if string == string[::-1]:
        print("Yes! The given String Is A Palindrome")
    else:
        print("No, The Given String Is not a Palindrome")

def reverseWord(str):
   print(f"\nThe Reverse of {str} is: ",str[-1:: -1])

def reverseSentence(str):
    wordStock = list(str.split(' '))
    wordStock = wordStock[::-1]
    return " ".join(wordStock)

def removeIthElement(str,pos):
    new_str =""
    for i in range(int(len(str))):
        if i == pos:
            continue
        else:
            new_str += str[i]
    return new_str 
    
def lengthString(str):
    count =0
    for i in str:
        count+=1
    return count
    
def evenWordFind(str):
    word = list(str.split())
    check =False
    for i in word:
        if len(i)%2 == 0:
            print(i)
            check = True
        else:
            continue
    if not check:
        print("Their are no Even Length Word")
        
if __name__ == "__main__":
    #@ STRING PROBLEMS --------->
    #! Problem 5: check whether the string is Symmetrical or Palindrome
    isPalindromeOrSymmetric(input("enter A string for Checking Palindrome: "))
    
    #! Problem 6: Reverse words in a given String in Python
    reverseWord("hello")
    print("\n\n",reverseSentence(input("Enter A Sentence of reverse the whole Sentence: ")))
    
    #! Problem 7: Ways to remove i’th character from string in Python
    str = input("\nEnter A Word : ")
    pos = int(input("Enter The index of removable latter: "))
    print(removeIthElement(str,pos))
    
    #! problem 8: Find length of a string in python (4 ways)
    print("\nthe Length of the string is: ", lengthString(input("Enter a String for Checking the Length: ")))
    #! Problem 9: to print even length words in a string
    evenWordFind(input("\nFor finding Even length word,Enter A Sentence : "))

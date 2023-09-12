
# ! 3. Take a string as an input and find out vowels and capitalize it
str = input("Enter A String : ")
vowels = ['a', 'e', 'i', 'o', 'u']

for i in vowels:
    if i in str:
        str = str.replace(i,i.capitalize())
print(str)


#! problem 4: Take input string and display its ASCII number 
word = input("Enter a Word : ")
for i in word:
    print(i, " :-> ",ord(i))

str = input("Enter A String : ")

# String Operation

# capitalize the string
print("After Capitalized:: ", str.capitalize())
upperString = str.upper()
# -use uppercase
print("Transform to UpperCase :: ", upperString)
# -use lowercase
print("Transform to LowerCase :: ", upperString.lower())
# -count of no of elements in string
print("How Many Letter present in string:-> ", len(str))


vowels = ['a', 'e', 'i', 'o', 'u']
# Count Number of Vowel
count = 0
for vowel in vowels:
    vowelCount = 0
    count += str.lower().count(vowel)
    vowelCount += str.lower().count(vowel)
    print(f"{vowel} is present: {vowelCount}")
print("The Total vowel In String is: ",count)

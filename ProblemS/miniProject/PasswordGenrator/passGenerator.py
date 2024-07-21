import random
import passprint as passArt

#! Print the ---
print(passArt.name_by_number)

# ! Ask How many digit will contain and how :
# digit_count = int(input("How many digit will contain in Yor Password ? -->"))
number_count = int(input("How many numbers you want in password: "))
uppercase_count = int(input("How many Upper case you want in password: "))
lowercase_count = int(input("How many Lower Case you want in password: "))
specialCharacter_count = int(input(
    "How many Special Character you want in password: "))

# Character list which will present in password
specialCharacter_list = specials = [
    "@", "#", "$", "%", "^", "&", "+", "~", "_"]

# ! Create empty List for contain Random Contains
numbers = []
UpLetters = []
lowLetters = []
spChs = []
password = []

# ! GENERATE THE WHOLE PASSWORD :
# * Generate Numbers
for i in range(0, number_count):
    numbers.append(str(random.randint(0, 9)))

password.extend(numbers)

# * Generate Lower case letters
for i in range(0, lowercase_count):
    lowLetters.append(str(chr(random.randint(97, 122))))

password.extend(lowLetters)

# * Generate Upper Case letters
for i in range(0, uppercase_count):
    UpLetters.append(str(chr(random.randint(65, 90))))

password.extend(UpLetters)

# * Generate Special Characters
for i in range(0, specialCharacter_count):
    spChs.append(str(random.choice(specialCharacter_list)))

password.extend(spChs)

#! Convert list to string :
random.shuffle(password)
finalPassword = "".join(password)

# ! NOW  give the password to User :
print("the password is prepared take it : -->")
print(finalPassword)

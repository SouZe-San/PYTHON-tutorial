# string = input("Enter the string you to print\n")
# print(string)

# name = input("enter your name: ")
# date = input("Enter the date: ")
# later = ''' Dear <Name> ,
#                 Your married partner with juicy have been confirmed,
#             you will get married on <date>'''

# later = later.replace('<Name>', name)
# later = later.replace('<date>', date)
# print(later)


newString = ''' hi i am a boy you motherfucker  bastards'''
if newString.find('  '):
    print("Double Space found")
    newString  = newString.replace('  ', ' ')
else:
    print("No Double Space in string")

print("the new string is : \n")
print(newString)
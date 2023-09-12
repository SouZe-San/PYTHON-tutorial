
# @ Reverser the String Also the Words
str3 = input("Enter A String : ")
print("\nReverser the String Also the Words")
print(">>", str3[::-1]
      )
wordStock = str3.split(' ')
wordStock = wordStock[::-1]
print("\nOnly reverse the String Not Its Word")
for i in wordStock:
    print(i, end=" ")

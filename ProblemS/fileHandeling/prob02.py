# ! The Sec prob ->Open in Append mode and add some content.

f = open('file01.txt', 'a')
content = input("Enter some thing that you want to put in a File: ")
f.write(content)
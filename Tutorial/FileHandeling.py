
# using w can write operation
f = open('fileWriting.txt', 'w')
f.write("I am writing")  #--> in the file this contain have write,,,, if any contain present in the file then it Over writes the contents of the file
f.close()

# Use open function to read the content of a file!
# f = open('sample.txt', 'r')
f = open('fileWriting.txt') # by default the mode is r
data = f.read()     #-------------> use to read any file
# data = f.read(5) # reads first 5 characters from the file
print(data)
line = f.readline() # this method help to read Only One line from the file.... if present multiple line then have to use multiple time
print(line)  
f.close()

f = open('fileWriting.txt', 'a') # FIle Open For Append operation by this operation the previous content stay as it was and add extra items..
f.write("  Welcome to my Anime World!")
f.close()



# upper style id basic, always have to open for every operation to work and close also
# for that come With -- open(.txt, op) as f -- come, Don;t have to close it do by itself

with open('fileWriting.txt') as f:
    a = f.read() # contain store in a
    print(a)

with open('fileWriting.txt', 'a') as f:
     f.write("\nJoin In hAnime")



with open("Multiplication_table_of_21.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{21}X{j}={21*j}")
            if j!=10:
                f.write('\n')


with open("fileWriting.txt") as f:
    contain = f.read()

if ("INFO" in contain):  # if Occur any Lowercase/UpperCase problem then transform in One type .lower()
    print("found")
    contain = contain.replace("INFO", "info")  # the Contain change but not in File
else:
    print("Not found")
    


cont = True
lineCount = 1;
with open('fileWriting.txt') as f :
    while cont:
        cont= f.readline()
        if 'INFO' in cont:
            print(f" the 'INFO present in line no {lineCount}")
        lineCount +=1


with open("fileWriting.txt", "w") as f:
        f.write(contain)
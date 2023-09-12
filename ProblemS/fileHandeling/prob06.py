
f = open('file01.txt')
lineList = f.readlines()
lineNo = len(lineList)
print(f"the Number of the Line in the File : {lineNo}")
n = input("Enter the How many Line you want read :: ")
for i in range(n):
    print(lineList[i])
f.close()
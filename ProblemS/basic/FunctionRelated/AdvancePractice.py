list1 = [4.32,43,52,65,2,7,45,78,35,"jdf"]
for index,item in enumerate(list1):
    if  (index != 0 and index%2== 0) :
        print(item)
print ("by loop----------")
for i in range(2,len(list1),2) :
    print(list1[i])


try:
    number = int(input("\nenter the A number: "))
except Exception as e:
    print(e)

mul_list = [number * i for i in range(1,11,1)]
print (mul_list)

with open("Multiplication_table_of_21.txt",'a') as f:
    f.write(f"\n{str(mul_list)}\n")
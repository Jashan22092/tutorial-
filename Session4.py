                       #LOOPS
                       # ( FOR , WHILE )

employee = ["Simmu" ,"Vansh","Naman","Divit","Baabu","Aditya"]

name = input("Enter The Name Of Employee: ")
print("Length Of Employee: " , len(employee))
print("Employee Name Is: " ,name)

      # WHILE LOOP
"""""
flag = False
idx = 0
while idx < 6:
    print("Matching" , name , "With" , employee[idx])

    if name == employee[idx]:
        flag=True
        break
    idx +=1

if flag:
     print("Name Found")
else:
     print("Name Not Found")
"""
       #FOR LOOP

flag = False
idx = 0
for idx in range(6):
    print("Matching" , name , "With" , employee[idx])

    if name == employee[idx]:
        flag=True
        break
    idx +=1

if flag:
     print("Name Found")
else:
     print("Name Not Found")
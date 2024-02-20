numbers = list(range(10,101,10))
print(numbers , type(numbers))

numbers.append(30)
numbers.append(50)
numbers.append(77)

print(numbers)

print("SUM IS: " ,sum(numbers))
print("MAX IS: " ,max(numbers))
print("MIN IS: " ,min(numbers))
print("LENGTH IS: " ,len(numbers))

reverse_number = list(reversed(numbers))
print(reverse_number)

print(numbers.index(50))   # TO FIND THE INDEX OF NUMBER 50
print(numbers.count(30))   # TO FIND THE NUMBER OF 30 IN LIST

data = [20,60,10,30]
data.sort()
print(data)

names = ["Jashan" , "Aditya" , "Divit" , "Simmu"]
names.sort()
print(names)

print("MIN IS: " , min(names))
print("MAX IS: " , max(names))

names.remove("Aditya")
print(names)


data = [20,30,10,40]
data.pop()  # WILL DELETE LAST ELEMENTS
data.pop(1)
print(data)

data.insert(-1,67)
data.insert(len(data) , 80)
data.insert(3,90)
print(data)
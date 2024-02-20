data = list(range(10,101,10))
print(data)

data = set(data)

for element in data:
    print(element)

    student = {
        "rollno": 101,
        "name": "Fionna",
        "age": 21
    }
    print("Dictionary Data...")

    items = student.items()
    for item in items:
        # print(item)
        print(item[0], item[1])

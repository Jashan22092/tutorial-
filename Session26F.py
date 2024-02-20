file = open("ipl_data_2014.csv" , "r")

def fetch():
    file = open("ipl_data_2014.csv", "r")
    lines = file.readlines()
    for line in lines:
        #return line
        yield line  # If a function, yeilds , it means we get Genrator in return

result = fetch()
print("result: ", result)

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result," No More Record"))

while True:
    data = next(result,"Nothing")
    print(data)
    if data == "Nothing":
        break


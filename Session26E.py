file = open("ipl_data_2014.csv" , "r")

lines = file.readlines()

for line in lines:
    print(line)

# with open("ipl_data_2014.csv" , "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line)

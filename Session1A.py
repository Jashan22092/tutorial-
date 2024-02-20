
          #MULTI VALUE CONTAINER

number = 10,20,30,40
print(number , id(number) , type(number))

# data = (10,10.2,"hello","wow")
data = [10,10.2,"hello","wow"]
print(data , id(data) , type(data))

print(data[0], id(data[0]) , type(data[0]))
print(data[0], id(data[1]) , type(data[1]))
print(data[0], id(data[2]) , type(data[2]))

my_data = data
print(my_data , id(my_data) , type(my_data))

              #  UPDATE OPERATION
# IMMUTABLE (TUPLE)    MEANS IT CAN'T BE UPDATED
# MUTABLE (LIST)       MEANS IT CAN BE UPDATED

my_data[2] = "AWESOME"
print(my_data , id(my_data) , type(my_data))


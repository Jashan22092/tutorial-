                              # DICTIONARY

my_tuple = tuple()
print(my_tuple, type(my_tuple))

# my_list = []
my_list = list()
print(my_list, type(my_list))

my_set = set()
print(my_set, type(my_set))

# my_dictionary = {}
my_dictionary = dict()
print(my_dictionary, type(my_dictionary))

my_data = {101: "John", 201: "Fionna", 301: "George", 661: "Harry"}
print(my_data)

print("MIN: " , min(my_data))
print("MAX: " , max(my_data))
print("SUM: " , sum(my_data))

print(my_data[201])

my_data.pop(201)
print(my_data)

my_data[775] = "Leo"
print(my_data)
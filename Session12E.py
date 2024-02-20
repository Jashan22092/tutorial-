name = "Jashan"
age = 21
email = "jashan@example.com"

print(name , age , email)

print("name:{} , age:{} , email:{}".format(name , age , email))
print("name:{0} age:{1} email:{2}".format(name, age, email))
print("name:{1} age:{2} email:{0}".format(name, age, email))

contact = {
"name" : "Jashan",
"age" : 21,
"email" : "jashan@example.com"
}

print("CONTACTS: ","name:{name} , age:{age} , email:{email} " .format_map(contact))
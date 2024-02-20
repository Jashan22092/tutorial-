names = "John, Jennie, Jim, Jack, Joe"

print("Names is: " , names)

upper_case_name = names.upper()
lower_case_name = names.lower()

print("uppercase Name: " , upper_case_name)
print("lower_case_name: " , lower_case_name)

print("S1: " + names.title())
print("S2: " + names.capitalize())
print("S3: " + names.swapcase())
print("S4: " + names.replace("J" , "KO"))

password = input("Enter Password")
print(password.strip())

data = "0069500"
print(data.strip("0"))

number = 036.5000
number = float(str(number).strip('0'))
print(number)

message = "No Internet Connectivity"
print(message)
print(message.center(50))
print(message.ljust(50))
print(message.rjust(50))

quote = "search the candle rather than cursing the darkness"
print(quote.find('sing'))
print(quote.find('the'))
print(quote.index('the'))
print(quote.rindex('the'))
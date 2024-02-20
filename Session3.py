   # Operators
      #Airthmetic Operators

product_price = 125.25
tax = 0.18
price_to_pay = product_price + tax * product_price
print(price_to_pay)

          # ( / , // )
number = 10
# result = number/3 # gives float value
result = number//3  # gives int value
print(result)

            #( * , ** )
base = 2
# result1 = base*2 # Means Multiply
result1 = base**3  # Means Exponential
print(result1)

               # ASSIGNMENT OPERATORS
age = 20
age+=3
age+=10
age-=5
age%=3
print("Age Is: " , age)

                  # Conditional Operators

cab_fare = 500
e_wallet = 300
print("Can I Book Ride : " , e_wallet>=cab_fare)

                      # Logical Operators
email = input("Enter Your Email: ")
password = input("Enter Your Password: ")
print("Email is: " ,email , "Password is: " , password)
print("Email Login Status: " , (email == "jashan@gmail.com"))
print("Password login Status: " , (password == "jashan123"))

                          # we will use AND , OR

print("Final Login Status: " , ((email == "jashan@gmail.com") and (password == "jashan123")))

                         #OTP
otp = 3027
user_otp = int(input("Enter OTP: "))
print("otp status: " , (otp == user_otp))


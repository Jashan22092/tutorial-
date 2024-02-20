                           # Membership Testing
a = 10
b = 10
print(a is b)
print(a is not b)

                         #Bitwise Operator
num1 = 10 # Binary Number Will Be -: 1010
num2 = 8  # Binary Number Will Be -: 1000
print("num1 in Binary: " , bin(num1))
print("num2 in Binary: " , bin(num2))
result = num1 & num2
print("Result is: " , result)

                     #Shift Operator
num3 = 8
num4 = 2
result1 = num3>>num4
result2 = num3<<num4
print( "Result1 is: " , result1)
print( "Result2 is: " , result2)

                    #Shift Operator For Negative Value
num5 = -13   # 1101 -: 0010(1's complement) then +1 (2'scomplement)
num6 = 3
result3 = num5>>num6
result4 = num5<<num6
print( "Result3 is: " , result3)
print( "Result4 is: " , result4)

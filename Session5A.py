def square(num):
    print("[Square] is: " , num , id(num))
    num = num*num
    print("[Square] now is: " , num , id(num))


def main():
    a = 10
    print("[Main] is: " , a , id(a) )
    square(a)
    print("[Main] now is: " , a , id(a))

if __name__ == "__main__" :
         main()
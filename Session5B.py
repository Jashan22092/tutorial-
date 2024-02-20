           # FUNCTIONS IN MEMORY

def square(num):
    print("[Square] is: " , num , id(num))
    for idx in range(1,len(num)):
     num[idx]**=2
     print("[Square] now is: ",num,id(num))

def main():
    data = [10,20,30,40,50]
    print("[Main] is: " , data , id(data))
    square(data)
    print("[Main is: ] now is" , data,id(data))

if __name__ == "__main__":
    main()
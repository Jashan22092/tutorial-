def get_max(A,L):

    if L == 1:
        return A[0]
    else:
        result = get_max(A, L-1)
        if result > A[L-1]:
            return result
        else:
            return A[L-1]

def main():
    data = [20,10,30,40]
    max_data = get_max(data , len(data))
    print("MAX NUMBER: " , max_data)

if __name__ == "__main__":
    main()
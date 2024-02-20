import numpy as np

A = np.array([
                    [1, 2],
                    [3, 4]

])

B = np.array([
                    [5, 6],
                    [7, 8]

])

print("A:" , A.shape)
print(A)

print("``````````````````````````")

print("B:" , A.shape)
print(B)

C = A + B
D = A - B
E = A / B
F = A * B
G = np.dot(A, B)


print("``````````````````````````")

print("G IS: ",G)

print("``````````````````````````")

print(F)

print("``````````````````````````")

print(C)

print("``````````````````````````")

print(D)

print("``````````````````````````")

print(E)

print("``````````````````````````")

result = A.sum()
print("result is: " , result)

P = np.array([

                [1, 2, 3],
                [4, 5, 6]
])

Q = np.transpose(P)
print(P)
print(Q)

print("``````````````````````````")

R = np.array([
    [1, 2],
    [3, 4]
])

R_inv = np.linalg.inv(R)
print(R)
print(R_inv)
print("R IS: ",np.dot(R, R_inv))
print("``````````````````````````")




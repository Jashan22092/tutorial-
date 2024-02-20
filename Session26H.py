import matplotlib.pyplot as plt  # Slicing.....
import numpy as np
from PIL import Image

arr1 = np.array([10, 20, 30, 40, 50])
print(arr1[1:4])
print(arr1[-1])
print("``````````````````````````")
               #Element Wise Arithmetic

arr2 = arr1 ** 2
print(arr2)

print("``````````````````````````")

arr3 = np.array([         # 3x3 Array
                    [10, 20, 30],
                    [40, 50, 60],
                    [70, 80, 90]



               ])
print(arr3)
print(arr3.shape)
print("``````````````````````````")

arr4 = arr3 * 2
print(arr4)

print("``````````````````````````")

#Broadcasting
arr5 = np.array([-1,-2,-3])
arr6 = arr3 + arr5
print(arr6)

print("``````````````````````````")

arr7 = np.array([10,20,30,40,50,60,70,80,90])
print(arr7)
print(arr7.shape)

print("``````````````````````````")

arr8 = arr7.reshape((3,3))
print(arr8)
print(arr8.shape)

print("``````````````````````````")

arr9 = arr8.reshape((9, ))
print(arr9)

print("``````````````````````````")

arr10 = np.array([10,20,30,40,50,60,70,80,90,100])

#arr11 = arr10.reshape((2,5))
arr11 = arr10.reshape((5,2))

print(arr11)

print("``````````````````````````")

arr12 = np.zeros(5)
print(arr12)

print("``````````````````````````")

arr13 = np.zeros((3,3))
print(arr13)

print("``````````````````````````")

arr14 = np.ones((3,3))
print(arr14)

print("``````````````````````````")

arr15 = np.empty(5)
print(arr15)

print("``````````````````````````")

arr16 = np.empty((3,3))
print(arr16)

print("``````````````````````````")

chessboard = np.zeros((8,8))
print(chessboard)

print("``````````````````````````")

# chessboard[0][1] = 1
# chessboard[1][0] = 1
chessboard[1::2] = 1
print(chessboard)

print("``````````````````````````")

chessboard = np.zeros((8,8))
chessboard = chessboard.tolist()
print(chessboard)
print(type(chessboard))

print("``````````````````````````")

chessboard = np.zeros((8,8))
chessboard = chessboard.tolist()

# chessboard[1::2, ::2] = 1
# chessboard[::2, 1::2] = 1


black = '\u2B1B'
white = '\u2B1C'

chessboard[0][0] = black
chessboard[0][1] = white

for row in chessboard:
    print(row)
# print(chessboard)
# print(type(chessboard))

print("``````````````````````````")

image_path = 'dog.jpeg'
image = Image.open(image_path)
image_array = np.array(image)
print(image_array)
print(image_array.shape)

plt.imshow(image)
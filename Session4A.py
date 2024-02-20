""""
They Have To Place Bricks

Jashan 1 2 3 ....

Simmu  3 6 9 ...

Total Bricks = 20

"""
total_bricks = int(input("Enter The Number Of Bricks: "))
bricks_in_walls = 0

for idx in range(1,total_bricks):
    jashan_bricks = idx
    bricks_in_walls += jashan_bricks

    if bricks_in_walls >= total_bricks:
        diffrence = bricks_in_walls - total_bricks
        print("Jashan Placed The Last Brick", (jashan_bricks - diffrence))
        break

    simmu_bricks = idx*3
    bricks_in_walls += simmu_bricks

    if bricks_in_walls >= total_bricks:
        diffrence = bricks_in_walls - total_bricks
        print("Simmu Placed The Last Brick", (simmu_bricks - diffrence))
        break

print("Bricks In Wall Are: " , (bricks_in_walls - diffrence))
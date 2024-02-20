                         # SET

john_followers = {"fionna", "sia", "jack", "joe", "george"}
print(john_followers, type(john_followers))

numbers = list(range(10,101,10))
print(numbers)

numbers = set(numbers)
print( "Numbers Now Are " , numbers)

numbers.add(35)
numbers.add(47)

print("After Adding: " , numbers)

numbers.pop()
print(numbers)

numbers.remove(50)
numbers.discard(40)
print(numbers)

john_followers = {"fionna", "sia", "jack", "joe", "george"}
jake_followers = {"anna", "jack", "leo", "joe", "harry", "mike"}
fionna_followers = {"sia", "joe"}

followers = john_followers.intersection(jake_followers)
followers = john_followers.intersection(jake_followers).intersection(fionna_followers)

print(followers)

followers = fionna_followers.issubset(john_followers)
followers = john_followers.issuperset(fionna_followers)

print(followers)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

C = A - B
print("C is:", C)

D = A & B
print("D is:", D)

E = A ^ B
print("E is:", E)

F = A | B
print("F is:", F)

G = A.symmetric_difference(B)  # returns a set that contains all items from both set, but not the items that are present in both sets
print("G is:", G)

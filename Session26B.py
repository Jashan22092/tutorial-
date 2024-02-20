# Nested Function
# create function inside other function

def outer():
    print("This is the Outer Function")
    def inner(): # nested/local function
        print("This is the Inner Function")
    inner()
outer()
# inner() -> ERROR
import datetime
def show():
    print("This is Show")
    print("Today is: ", datetime.datetime.today())

hello =show

print("Show is: ",show)
print("Hello is: ",hello)

show()
hello()
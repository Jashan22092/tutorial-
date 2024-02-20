          #   OOPS
"""
# Object and Attributes: Dish: name, price, ratings

"""
class dish:

    def __init__(self , Name ="" , Price = 0 ,Rating = 4.0 ):
        self.name = Name
        self.price = Price
        self.rating = Rating

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Name: " , self.name)
        print("Price: ", self.price)
        print("Rating: ", self.rating)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")

dish1 = dish("Noodels" , 90 , 4.5)
dish2 = dish("Burger" , 120 , 4.7)

dish1.show()
dish2.show()
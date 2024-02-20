# Relationship Mapping
# 1 Restaurant Has 1 Menu
# 1 Menu Has Many Dishes

class Dishes:
    def __init__(self , name , price , rating):
        self.name = name
        self.price = price
        self.rating = rating

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Name is: " , self.name)
        print("Price is: ", self.price)
        print("Rating is: ", self.rating)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

class Menu:
    def __init__(self ,  title, num_of_dishes, dishes):
        self.title = title
        self.num_of_dishes = num_of_dishes
        self.dishes = dishes

    def show(self):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("Title is: " , self.title)
        print("Number Of Dishes is: " ,self.dishes )

        for idx in range(len(self.dishes)):
            self.dishes[idx].show()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

class Restraunt:
    def __init__(self , name, address, phone, ratings, menu):
        self.name = name
        self.address = address
        self.phone = phone
        self.ratings = ratings
        self.menu = menu

    def show(self):
        print("==============================")
        print(self.name, "|", self.ratings)
        print(self.address, "|", self.phone)
        print("==============================")

        self.menu.show()

def main():

    dish1 = Dishes("Dal Makhni" , 350 , 4.5)
    dish2 = Dishes("Cheese Tomato", 430, 4.3)
    dish3 = Dishes("Mix Veg", 310, 3.9)

    #Lists
    dishes = [dish1 , dish2, dish3]
    menu = Menu("Indian" ,len(dishes) , dishes )
    restraunt = Restraunt("Basant" , "BRS Nagar" , 9887665441 , 4.2 , menu)

    restraunt.show()


if __name__ == "__main__":
    main()
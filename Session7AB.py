from Session7A import Product , Menu , Category

def main():
    smart_phone_products = [
        Product("iPhone13", "Apple", 70000, 4.5),
        Product("Samsung Fold", "Samsung", 90000, 4.6)
    ]

    mob_categories = [
        Category("Accessories", 21, "40%", None),
        Category("Smart Phones", 2, "30%", smart_phone_products),
        Category("Prime Day Launches", 234, "50%", None),
    ]

    menu = [
        Menu("Sell", None),
        Menu("Best Sellers", None),
        Menu("Today's Deals", None),
        Menu("Mobiles", mob_categories),
        Menu("New Releases", None)
    ]

    print("WELCOME TO AMAZON")

    for idx in range(len(menu)):
        menu[idx].show()

    print()

    menu_option = int(input("Choose Menu Between (1-5)"))
    print("Menu Choosed: " , menu_option)

    if menu_option == 4:
        menu[3].show_categories()

        category_choice = int(input("Choose Category Between (1-5)"))
        print("Category Choosed: " , category_choice)

        if category_choice == 2:
            mob_categories[1].show_products()


if __name__ == "__main__":
    main()
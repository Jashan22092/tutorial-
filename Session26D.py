def upgrade_to_meal(func):

    def inner(amount,taxes , meal_plan):
        if meal_plan == 1:
            print("Thanku For Your Purchase.. :)")
            print("Upgrading to Medium Meal...")
            print("+ Added Coke")
            print("+ Added Fries")
            amount += 100
        elif meal_plan == 2:
            print("Thanku For Your Purchase.. :)")
            print("Upgrading to Large Meal..")
            print("+ Added large Coke")
            print("+ Added large Fries")
            print("+ Added Ice Cream")
            amount += 200
        else:
            print("Thanku For Your Purchase.. :)")
        return func(amount , taxes , meal_plan)
    return inner

    return inner

@upgrade_to_meal
def buy_burger(amount,taxes , meal_plan=0):
    return amount +(amount*taxes)

amount_to_pay = buy_burger(100,0.10 , 2)
print("Mc Donald's Final Charge: " , amount_to_pay)
# Decorator...
# 1.Create a function, which takes function as input
# 2.Create an inner function,which should have same signature of the target function
# 3.Execute the passed function from the inner function
# 4.Return inner function from outer function
# 5.To decorate any function use@function
def compute_taxes(func):

    def inner(amount,taxes):
        if amount > 0 and amount <= 1000:
            taxes = 0.18
        elif amount >10000:
            taxes = 0.25
        else:
            print("Invalid Amount")

        return  func(amount, taxes)

    return inner

@compute_taxes
def pay(amount,taxes):
    return amount +(amount*taxes)

amount_to_pay = pay(50000,0)
print("Amount_to_pay" , amount_to_pay)
message = """"
            WELCOME TO ZOMATO
               
                SUBWAY OFFERS 
                
                WELCOME50 -: 
  Get 50% OFF up to ₹100 Valid on total value of items worth ₹159 or more.
       
                  PAYTMUPI -:
  Get 20% OFF up to ₹50 and up to ₹100 Paytm cashback using Paytm UPIValid on 
            total value of items worth ₹299 or more.                
"""
print(message)

amount = int(input("Enter Amount: "))
promo_code = input("Enter PromoCode: ")

"""if amount>=159:
    print("You Can Apply Promocode")
else:
    print("Promocode Can't Be Applied")"""

if promo_code == "WELCOME 50":
    if amount >= 159:
        print("Promo Code Applied")
        discount = 0.5 * amount
        if discount>=100:
            discount=100
            amount_to_pay = amount-discount
        print("please Pay: \u20b9" ,amount_to_pay)
    else:
        print("Amount Is Lesser For Promo Code")
        print("Please Pay: \u20b9",amount)

elif promo_code== "PAYTMUPI" :
    if amount >= 299:
        print("Promo Code Applied")
        discount = 0.2 * amount
        if discount>=50:
            discount=50
            amount_to_pay = amount-discount
        print("please Pay: \u20b9" ,amount_to_pay)
        print("Upto 100 Cashback Will Be Credited To Paytym Wallet")

    else:
        print("Amount Is Lesser For Promo Code")
        print("Please Pay: \u20b9",amount)
else:
    print("Promo Code Invalid")
    print("Please Pay: \u20b9", amount)
    print("USE WELCOME 50 PROMO CODE TO SAVE MORE MONEY")

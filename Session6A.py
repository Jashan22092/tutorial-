"""
      MAKE A PAYTYM INTERFACE
    Attributes-:

Recharge
Prepaid
Mobile Number
Amount
Proceed to Recharge

"""

class paytm:
    def __init__(self , recharge = "" , mobile_number = 0 , operator = "" ,amount = 0 , proceed_to_recharge= "" ):
        self.recharge = recharge
        self.mobile_number = mobile_number
        self.operator = operator
        self.amount = amount
        self.proceed_to_recharge = proceed_to_recharge

    def show(self):

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Recharge: " , self.recharge)
        print("Mobile Number: ", self.mobile_number)
        print("Operator: ", self.operator)
        print("Amount: ", self.amount)
        print("Proceed To Recharge: ", self.proceed_to_recharge)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

paytm1 = paytm("Postpaid" , 7530000428 ,"Airtel" ,1349 ,"Bill Paid")
paytm2 = paytm("Prepaid" , 9988246643 ," VI" ,799 ,"Recharge Successful")
paytm3 = paytm("Prepaid" , 9888086643 ,"Jio" ,479 ,"Recharge Successful")

paytm1.show()
paytm2.show()
paytm3.show()
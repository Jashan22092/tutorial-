from Session18A import Customer
from Session18B import MongoDBHelper
def main():

    db = MongoDBHelper()



#    customer = Customer()
 #   customer.read_customer_data()


#    document = vars(customer)


 #   db.insert(document)


#    query = {'phone': '9876543210'}
#    db.delete(query)

    db.fetch()

if __name__ == "__main__":
    main()

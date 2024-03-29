import mysql.connector as db

class Customer:

    def __init__(self):
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")


def main():

    customer = Customer()
    print(vars(customer))

    # DataBase Connectivity

    # Step1: Create Connection with Database
    connection = db.connect(user='root',
                            password='Jashan@123',
                            host='127.0.0.1',
                            database='gw2023pds1')

    # Step2: Obtain Cursor to perform SQL operations :)
    cursor = connection.cursor()

    # Step3: Create SQL Statement
    sql = "insert into Customer values" \
          "(null, '{name}', '{phone}', '{email}');".format_map(vars(customer))

    # Step4: Execute SQL Command
    cursor.execute(sql)
    connection.commit()

    print("Customer Inserted...")


if __name__ == "__main__":
    main()
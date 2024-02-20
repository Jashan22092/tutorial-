from Session15 import Pet
from Session14 import Customer
from Session17 import Consultation
from Session14B import DBHelper
from tabulate import tabulate
from datetime import datetime


def consultation_menu():

    db = DBHelper()

    message = """
    >>Consultation Menu<<

    1: Add Consultation
    2: Update Consultation
    3: View All Consultation
    4: View Consultation by Date
    5: View Customer's Pet's Consultation
    0: Quit
    """
    print(message)
    choice = int(input("Enter Your Choice: "))

    pet = Pet()
    customer = Customer()
    consultation = Consultation()

    while True:
        if choice == 1:

            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pets_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            if len(rows) == 0:
                print("Please Add Pet First...")
            if len(rows) == 1:
                pet.pid = rows[0][0]
            else:
                pet.pid = int(input("Enter Pet ID: "))

            consultation.cid = customer.cid
            consultation.pid = pet.pid
            consultation.read_consultation_data()

            print(vars(consultation))

            sql = consultation.get_insert_sql_query()
            db.execute_sql(sql)
            print("Consultation Added....")

        elif choice == 2:
            pass
        elif choice == 3:

            sql = consultation.get_consultation_sql_query()
            rows = db.execute_select_sql(sql)
            columns = ['CNID', 'CID', 'PID', 'PROBLEM', 'HEARTRATE', 'TEMP', 'MEDICINES', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 4:

            date = input("Enter Date (YYYY-MM-DD): ")
            sql = consultation.get_consultation_sql_query_by_date(date)
            rows = db.execute_select_sql(sql)
            columns = ['CNID', 'CID', 'PID', 'PROBLEM', 'HEARTRATE', 'TEMP', 'MEDICINES', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            if len(rows) == 0:
                print("There Is No Consultation At This Date...")
            if len(rows) == 1:
                consultation.cnid = rows[0][0]

        elif choice == 5:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pets_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            pid = input("Enter Pet Id: ")

            sql = consultation.get_consultation_sql_query(pid=pid)
            rows = db.execute_select_sql(sql)
            columns = ['CNID', 'CID', 'PID', 'PROBLEM', 'HEARTRATE', 'TEMP', 'MEDICINES', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 0:
            break
        else:
            print("Invalid Choice")
        print(message)
        choice = int(input("Enter Your Choice: "))
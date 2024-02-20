from Session15 import Pet
from Session14 import Customer
from Session14B import DBHelper
from tabulate import tabulate


def pets_menu():

    db = DBHelper()

    message = """
    >>Pets Menu<<

    1: Add Pet
    2: Update Pet
    3: Delete Pet
    4: View All Pet
    5: View Customer's Pet
    0: Quit
    """
    print(message)
    choice = int(input("Enter Your Choice: "))

    pet = Pet()
    customer = Customer()

    while True:
        if choice == 1:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            pet.cid = customer.cid

            pet.read_pet_data()
            print(vars(pet))

            sql=pet.get_insert_sql_query()
            db.execute_sql(sql)
        elif choice == 2:

            phone = input("Enter Customer Phone: ")
            sql_customer = customer.get_customers_sql_query(phone)
            rows_customer = db.execute_select_sql(sql_customer)
            columns_customer = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows_customer, headers=columns_customer, tablefmt="grid"))

            customer_fetched = rows_customer[0]
            customer.cid = customer_fetched[0]

            sql_pet = pet.get_pets_sql_query(str(customer.cid))
            rows_pet = db.execute_select_sql(sql_pet)
            columns_pet = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows_pet, headers=columns_pet, tablefmt="grid"))

            pid = input("Enter Pet ID: ")
            sql = pet.get_only_pets_sql_query(pid)
            rows = db.execute_select_sql(sql)
            pet_fetched = rows[0]
            pet.pid = pet_fetched[0]

            pet.name = input("Enter Pet Name: ")
            if len(pet.name) == 0:
                pet.name = rows_pet[1]

            pet.age = input("Enter Pet Age: ")
            if len(pet.age) == 0:
                pet.age = rows_pet[2]
            else:
                pet.age = int(pet.age)

            pet.weight = input("Enter Pet Weight: ")
            if len(pet.weight) == 0:
                pet.weight = rows_pet[3]

            pet.breed = input("Enter Pet Breed: ")
            if len(pet.breed) == 0:
                pet.breed = rows_pet[4]

            pet.gender = input("Enter Pet Gender: ")
            if len(pet.gender) == 0:
                pet.gender = rows_pet[5]

            sql_update_pet = pet.get_update_sql_query()
            db.execute_sql(sql_update_pet)

            print("Pet Updated...")

        elif choice == 3:

            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_delete_sql_query()
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print((tabulate(rows, headers=columns, tablefmt="grid")))

            pet.pid = input("Enter Pet ID: ")
            delete_choice = input("Are You Sure To Delete? (yes/no)")

            if delete_choice == "yes":
                sql = pet.get_delete_sql_query()
                db.execute_sql(sql)
                print("Pet Deleted...")

        elif choice == 4:
            sql = pet.get_pets_sql_query()
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print((tabulate(rows, headers=columns, tablefmt="grid")))

        elif choice == 5:

            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            # for row in rows:
            # print(row)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print((tabulate(rows, headers=columns, tablefmt="grid")))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pets_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print((tabulate(rows, headers=columns, tablefmt="grid")))

        elif choice == 0:
            break
        else:
            print("Invalid Choice")

        print(message)
        choice = int(input("Enter Your Choice: "))

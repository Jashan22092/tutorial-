import datetime
from Session16A import customer_menu
from Session16B import pets_menu
from Session16C import consultation_menu


def main_menu():
    message = """
    1: Manage Customer
    2: Manage Pets
    3: Manage Consultations
    0: Quit
    """
    print(message)

    choice = int(input("Enter Your Choice: "))

    while True:
        if choice == 1:
            customer_menu()
        elif choice == 2:
            pets_menu()
        elif choice == 3:
            consultation_menu()
        elif choice == 0:
            break
        else:
            print("Invalid Choice")
        print(message)
        choice = int(input("Enter Your Choice: "))


def main():

    date1 = datetime.datetime.today()

    welcome = """
    ~~~~~~~~~~~~~~~~~~~~~
    Welcome To Vets App
    ~~~~~~~~~~~~~~~~~~~~~
    """
    print(welcome)

    main_menu()

    bye_message = """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Thank You For Using Vets App
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    print(bye_message)

    date2 = datetime.datetime.today()
    print("APP USAGE TIME: ", date2-date1)


if __name__ == "__main__":
    main()


import mysql.connector as db

def main():
    sql1 = "update Customer set name = 'John Watson', age=26 where cid = 1"
    sql2 = "delete from Customer where cid = 2"
    sql3 = "select * from Customer"

    connection = db.connect(user='root',
                            password='Jashan@123',
                            host='127.0.0.1',
                            database='gw2023pds1')
    # Step2: Obtain Cursor to perform SQL operations
    cursor = connection.cursor()

    # Step4: Execute SQL Command
    # cursor.execute(sql1)
    # cursor.execute(sql2)
    # connection.commit()
    # print("SQL Query Executed...")

    cursor.execute(sql3)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()
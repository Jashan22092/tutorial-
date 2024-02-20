import mysql.connector as db


class DBHelper:

    def __init__(self):
        self.connection = db.connect(user='root',
                                password='Jashan@123',
                                host='127.0.0.1',
                                database='gw2023pds1')
        self.cursor = self.connection.cursor()
        print("[DBHelper] Connection Created and Cursor Obtained...")

    #INSERT , DELETE , UPDATE
    def execute_sql(self,sql):
        print("[DBHelper] Executing SQL:", sql)
        self.cursor.execute(sql)
        self.connection.commit()
        print("[DBHelper] Executed")

    def execute_select_sql(self, sql):
        print("[DBHelper] Executing SQL:", sql)
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows





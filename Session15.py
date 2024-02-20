import datetime

"""
    Pet: pid, name, age, weight, breed, gender, cid, createdon

    create table Customer(
        cid int primary key auto_increment,
        name text,
        phone text unique key,
        email text,
        age int,
        gender text,
        address text,
        createdon datetime
    );

    create table Pet(
        pid int primary key auto_increment,
        name text,
        age int,
        weight int,
        breed text,
        gender text,
        cid int,
        createdon datetime,
        FOREIGN KEY (cid) REFERENCES Customer(cid)
    );
"""


class Pet:

    def __init__(self):
        self.pid = 0
        self.name = ""
        self.age = 0
        self.weight = 0
        self.breed = ""
        self.gender = ""
        self.cid = 0
        self.createdon = ""

    def read_pet_data(self):
        self.name = input("Enter Pets Name: ")
        self.age = int(input("Enter Pets Age: "))
        self.weight = int(input("Enter Pets Weight: "))
        self.breed = input("Enter Pets Breed: ")
        self.gender = input("Enter Pets Gender: ").lower()
        self.createdon = str(datetime.datetime.today())

             #ELIMINATE MILLISECONDS

        self.createdon = self.createdon[: self.createdon.rindex(".")]


    def get_insert_sql_query(self):
        sql = "insert into Pet values(null , '{name}', {age}, {weight} ," \
           " '{breed}' ,'{gender}', {cid} ,'{createdon}');".format_map(vars(self))

        return sql


    def get_pets_sql_query(self, cid=""):

        if len(cid) == 0:
            sql = "select * from Pet "

        else:
            sql = "select * from Pet where cid = {}".format(cid)

        return sql


    def get_only_pets_sql_query(self, pid=""):
        sql = "select * from Pet where pid = {}".format(pid)
        return sql

    def get_delete_sql_query(self):
        sql = "delete from Pet where pid = {}".format(self.pid)
        return sql

    def get_update_sql_query(self):
        sql = "update Pet set name='{name}', age={age}, weight='{weight}', breed='{breed}', " \
            "gender='{gender}', cid={cid} where pid = {pid}".format_map(vars(self))
        return sql
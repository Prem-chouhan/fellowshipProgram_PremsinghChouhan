import sys

sys.path.insert(0, '/home/admin-1/PycharmProjects/FunDooapp/configration/')
from db_connection import *


class DbManaged:
    def __init__(self):
        mydbobj = db_connection()
        self.mydb = mydbobj.connection()
        self.mycursor = self.mydb.cursor()

    def registration(self, data):
        print("inside", data)
        sql = "INSERT INTO Registration(email,password,confirm_password) VALUES (%s, %s, %s)"
        val = (data['email'], data['password'], data['confirm_password'])
        print(sql)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        # print(mycursor.rowcount, "record inserted.")

    def login(self, data):
        sql = "INSERT INTO Login(username,password) VALUES (%s, %s)"
        val = (data['username'], data['password'])
        print(sql)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

import sys

sys.path.insert(0, '/home/admin-1/PycharmProjects/FunDooapp/configration/')
from db_connection import *


class DbManaged:
    def __init__(self):
        mydbobj = db_connection()
        self.mydb = mydbobj.connection()
        self.mycursor = self.mydb.cursor()

    def registration(self, data):
        sql = "INSERT INTO Registration(email,password,confirm_password) VALUES (%s, %s, %s)"
        val = (data['email'], data['password'], data['confirm_password'])
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def login_user(self, data):
        sql = "INSERT INTO Login(username,password) VALUES (%s, %s)"
        val = (data['username'], data['password'])
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def email_address_exists(self, data):
        sql = "SELECT email FROM Registration where email = '" + data['email'] + "'"
        self.mycursor.execute(sql)
        my_result = self.mycursor.fetchall()
        if len(my_result):
            return False
        else:
            return True

    def username_exists(self, data):
        print("inside username")
        sql = "SELECT username FROM Login where username = '" + data['username'] + "'"
        self.mycursor.execute(sql)
        my_result = self.mycursor.fetchall()
        if len(my_result):
            return False
        else:
            return True

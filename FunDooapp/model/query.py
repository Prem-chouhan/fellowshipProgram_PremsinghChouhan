import sys
import re

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
        sql = "SELECT username FROM Login where username = '" + data['username'] + "'"
        self.mycursor.execute(sql)
        my_result = self.mycursor.fetchall()
        if len(my_result):
            return False
        else:
            return True

    def email_validate(self, email):
        if re.match(f"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return True
        return False

    def check_password(self, data):
        sql = "SELECT password FROM Login where password = '" + data['password'] + "'"
        self.mycursor.execute(sql)
        my_result = self.mycursor.fetchall()
        if len(my_result):
            return True
        else:
            return False
        # return my_result

    def update_password(self, data, password):
        print(data["username"])
        print(password['password'])
        sql = "UPDATE Login SET password = '" + password['password'] + "' WHERE username = '" + data['username'] + "'"
        self.mycursor.execute(sql)
        my_result=self.mydb.commit()
        if len(my_result):
            return True
        else:
            return False
    #     sql = "UPDATE Login SET password = %s WHERE address = %s"
    #     val = (data["password"],)
    #     self.mycursor.execute(sql, val)
    #     self.mydb.commit()

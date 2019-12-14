import sys
sys.path.insert(0,'/home/admin-1/PycharmProjects/FunDooapp/configration/')
from db_connection import *


class db_maganed:
    def __init__(self):
        mydbobj = db_connection()
        self.mydb = mydbobj.connection()
        self.mycursor = self.mydb.cursor()

    def registration(self):
        sql = "INSERT INTO Registration(fname,lname,email,password,confirm_password) VALUES (%s, %s, %s, %s, %s)"
        val = ("prem", "chouhan", "premchoauha1wn@gmail.com", "Premsingh", "Premsingh")
        self.mycursor.execute(sql, val)
        self.obj.commit()
        print(mycursor.rowcount, "record inserted.")


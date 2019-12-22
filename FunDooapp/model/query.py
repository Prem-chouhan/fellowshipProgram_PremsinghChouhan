import sys
import re
from email.mime.multipart import MIMEMultipart
import smtplib
import socket
from email.mime.text import MIMEText
sys.path.insert(0, '/home/admin-1/PycharmProjects/FunDooapp/configration/')
from db_connection import *
sys.path.insert(0, '/home/admin-1/PycharmProjects/FunDooapp/templates/')
import os
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
        # print(len(my_result))

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

    def update_password(self, data, key):
        sql = "UPDATE Registration SET password = '" + data['password'] + "' WHERE email = '" + key + "' "
        # print(sql)
        self.mycursor.execute(sql)
        self.mydb.commit()
        # if len(my_result):
        #     return False
        # else:
        #     return True

    #     sql = "UPDATE Login SET password = %s WHERE address = %s"
    #     val = (data["password"],)
    #     self.mycursor.execute(sql, val)
    #     self.mydb.commit()

    from email.mime.multipart import MIMEMultipart
    import smtplib, os

    def smtp(self, emailid, message):
        import smtplib

        # creates SMTP session
        s = smtplib.SMTP(os.getenv("SMTP_EXCHANGE_SERVER"), os.getenv("SMTP_EXCHANGE_PORT"))

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(os.getenv("SMTP_EXCHANGE_USER_LOGIN"), os.getenv("SMTP_EXCHANGE_USER_PASSWORD"))

        # message to be sent
        # message = "Message_you_need_to_send"

        msg = MIMEText(message)


        # msg = MIMEText(u'<a href="www.google.com">127.0.0.1:localhost/8080</a>', 'html')
        # sending the mail
        s.sendmail(os.getenv("SMTP_EXCHANGE_USER_LOGIN"), emailid, msg.as_string())

        # terminating the session
        s.quit()










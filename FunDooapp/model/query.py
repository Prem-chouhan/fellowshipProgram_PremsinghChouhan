import sys
import re
from email.mime.multipart import MIMEMultipart
import smtplib
import socket
from email.mime.text import MIMEText

sys.path.insert(0, '/home/admin-1/PycharmProjects/FunDooapp/configration/')
from db_connection import db_connection

sys.path.insert(0, '/home/admin-1/PycharmProjects/FunDooapp/templates/')
import os

my_db_obj = db_connection()


class DbManaged:

    def __init__(self):
        # self.mycursor = self.mydb.cursor()
        pass

    def registration(self, data):
        sql = "INSERT INTO Registration(email,password,confirm_password) VALUES (%s, %s, %s)"
        val = (data['email'], data['password'], data['confirm_password'])
        my_db_obj.queryExecute(sql, val)
        # self.mycursor.execute(sql, val)
        # self.mydb.commit()

    def login_user(self, data):
        sql = "INSERT INTO Login(username,password) VALUES (%s, %s)"
        val = (data['username'], data['password'])
        my_db_obj.queryExecute(sql, val)
        # self.mycursor.execute(sql, val)
        # self.mydb.commit()

    def email_address_exists(self, data):
        sql = "SELECT email FROM Registration where email = '" + data['email'] + "'"
        # mycursor.execute(sql)
        # my_result = self.mycursor.fetchall()
        # print(len(my_result))
        my_result = my_db_obj.queryfetch(sql)
        print(my_result)
        if my_result:
            return False
        else:
            return True

    def username_exists(self, data):
        sql = "SELECT username FROM Login where username = '" + data['username'] + "'"
        # self.mycursor.execute(sql)
        my_result = my_db_obj.queryfetch(sql)
        # my_result = self.mycursor.fetchall()
        if my_result:
            return False
        else:
            return True

    def email_validate(self, email):
        if re.match(f"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return True
        return False

    def check_password(self, data):
        sql = "SELECT password FROM Login where password = '" + data['password'] + "'"
        # self.mycursor.execute(sql)
        my_result = my_db_obj.queryfetch(sql)
        if my_result:
            return True
        else:
            return False
        # return my_result

    def update_password(self, data, key):
        sql = "UPDATE Registration SET password = '" + data['password'] + "' WHERE email = '" + key + "' "
        # print(sql)
        my_db_obj.query(sql)

        # self.mycursor.execute(sql)
        # self.mydb.commit()
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

    def query_insert(self, data):
        sql = "INSERT INTO crud(tittle,description,color,isPinned,isArchive,isTrash) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (data['tittle'], data['description'], data['color'], data['isPinned'], data['isArchive'], data['isTrash'])
        # obj = db_connection()
        my_db_obj.queryExecute(sql, val)
        # self.mycursor.execute(sql, val)
        # self.mydb.commit()
        # return True

    def query_update(self, data):
        sql = "UPDATE crud SET tittle = '" + data['tittle'] + "' WHERE id = '" + data['id'] + "' "
        # self.mycursor.execute(sql)
        # self.mydb.commit()
        my_db_obj.query(sql)

    def query_delete(self, data):
        sql = "DELETE FROM crud WHERE id = '" + data['id'] + "'"
        # self.mycursor.execute(sql)
        # self.mydb.commit()
        my_db_obj.query(sql)


    # def query_read(self, data):
    #     print(data['tablename'])
    #     sql = "select * from " + data['tablename'] + ""
    #     self.mycursor.execute(sql)
    #     print(self.mycursor.fetchall())
    #
    # def query_create(self, data):
    #     key = data['tablename']
    #     print(key)
    #     sql = "CREATE TABLE " + key + "(id int NOT NULL AUTO_INCREMENT,LastName varchar(255) NOT NULL,FirstName " \
    #                                   "varchar(255),Age int,PRIMARY KEY (id)) "
    #     self.mycursor.execute(sql)
    #     self.mydb.commit()

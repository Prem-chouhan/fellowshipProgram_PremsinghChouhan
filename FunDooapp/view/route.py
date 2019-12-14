import cgi

from config.settings import mydb_connection
from files import html_string_regsuc, html_string_regfail
from model.response import Response
from templates import *


def register(self):
    if self.path == '/register':
        # processing user input submitted in Front end(HTML)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        # getting the data
        print(form)
        print(form['email_id'])
        print(form['username'])
        print(form['password'])
        email_id = form['email_id'].value
        username = form['username'].value
        password = form['password'].value
        cursor = mydb_connection.cursor()
        # inserting into the database using sql commands
        sql = "insert into registration (email_id, username, password) values (%s, %s, %s)"
        # The row values are provided in the form of tuple
        val = (email_id, username, password)
        try:
            if cursor.execute(sql, val):
                mydb_connection.commit()
            else:
                mydb_connection.commit()
                val = 1
                if val == 1:
                    # if the data inserted successfully
                    Response(self).html_response(status=202, data=html_string_regsuc)
                    print("reg sucessfull")

                else:
                    # if the data not inserted successfully
                    Response(self).html_response(status=202, data=html_string_regfail)
                    print("registration failed")
        except:
            mydb_connection.rollback()
            mydb_connection.close()
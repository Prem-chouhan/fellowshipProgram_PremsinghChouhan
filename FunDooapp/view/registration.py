import cgi
import sys

sys.path.insert(0, '/home/admin-1/PycharmProjects/FunDooapp/model')
sys.path.insert(0, '/home/admin-1/PycharmProjects/FunDooapp/view')
from query import DbManaged
from response import Response

class registration:
    def register(self):
        try:
            if self.path == '/register':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST',
                             'CONTENT_TYPE': self.headers['Content-Type'],
                             })
                data = {}
                data['email'] = form['email'].value
                data['password'] = form['password'].value
                data['confirm_password'] = form['confirm_password'].value
                print(data)
                my_db_obj = DbManaged()
                my_db_obj.registration(data)
                # obj = Response()
                # obj.jsonResponse(status, data)

        except KeyError:
            pass

    def login(self):
        if self.path == '/login':
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            data = {}
            data['username'] = form['Username'].value
            data['password'] = form['Password'].value
            my_db_obj = DbManaged()
            my_db_obj.login(data)






import cgi
import sys
import os

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
                response_data = {'success': True, "data": [], "message": ""}
                print(len(form), type(form), form)

                # if len(form) == 1 or len(form) == 2 or len(form) == 3 or len(form) is 0:
                if len(form) <= 3:
                    response_data.update({'success': False, "data": [], "message": "Sorry..!!!you have not Entered "
                                                                                   "Email,"
                                                                                   "Password"})
                    Response(self).jsonResponse(status=404, data=response_data)
                data = {}
                data['email'] = form['email'].value
                data['password'] = form['password'].value
                data['confirm_password'] = form['confirm_password'].value
                my_db_obj = DbManaged()
                success = my_db_obj.email_address_exists(data)
                if success:
                    my_db_obj.registration(data)
                    response_data.update({"message": "Registration Done Successfully"})
                    Response(self).jsonResponse(status=202, data=response_data)
                else:
                    response_data.update({"message": "Email Already Exists", "success": False})
                    Response(self).jsonResponse(status=202, data=response_data)
                return len(form)

        except KeyError:
            pass
        except BrokenPipeError:
            response_data = {'success': True, "data": [], "message": ""}

            response_data.update({'success': False, "data": [], "message": "Sorry..!!!you have not Entered "
                                                                           "Email,"
                                                                           "Password"})


    def login(self):
        try:
            if self.path == '/login':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST',
                             'CONTENT_TYPE': self.headers['Content-Type'],
                             })
                response_data = {'success': True, "data": [], "message": ""}
                if len(form) <= 2:
                    response_data.update(
                        {'success': False, "data": [], "message": "Sorry..!!!you have not Entered Username "})
                    Response(self).jsonResponse(status=404, data=response_data)
                data = {}
                data['username'] = form['username'].value
                data['password'] = form['password'].value
                response_data = {'success': True, "data": [], "message": ""}
                print(len(form))
                my_db_obj = DbManaged()
                success = my_db_obj.username_exists(data)

                if success:
                    my_db_obj.login_user(data)
                    response_data.update({"message": "Login done successfully"})
                    Response(self).jsonResponse(status=202, data=response_data)
                else:
                    response_data.update({"message": "Username already exists", "success": False})
                    Response(self).jsonResponse(status=202, data=response_data)

        except KeyError:
            pass

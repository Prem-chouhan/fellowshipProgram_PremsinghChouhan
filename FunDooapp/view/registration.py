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
            my_db_obj = DbManaged()
            if self.path == '/register':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST',
                             'CONTENT_TYPE': self.headers['Content-Type'],
                             })
                response_data = {'success': True, "data": [], "message": ""}
                form_keys = list(form.keys())
                if len(form_keys) < 3:
                    response_data.update({'success': False, "data": [], "message": " some values are missing"})
                    Response(self).jsonResponse(status=404, data=response_data)
                # my_db_obj = DbManaged()
                data = {}
                data['email'] = form['email'].value
                data['password'] = form['password'].value
                data['confirm_password'] = form['confirm_password'].value
                if not my_db_obj.email_validate(form['email'].value):
                    response_data.update(
                        {"message": "Email Format is Invalid please Re-enter Email", "success": False})
                    Response(self).jsonResponse(status=202, data=response_data)
                    # break
                success = my_db_obj.email_address_exists(data)
                if success:
                    my_db_obj.registration(data)
                    response_data.update({"success": True, "data": [], "message": "Registration Done Successfully"})
                    Response(self).jsonResponse(status=202, data=response_data)
                else:
                    response_data.update({"message": "Email Already Exists", "success": False})
                    Response(self).jsonResponse(status=202, data=response_data)
                # return len(form)

        except KeyError:
            pass
        except BrokenPipeError:
            response_data = {'success': True, "data": [], "message": ""}
            Response(self).jsonResponse(status=202, data=response_data)
            response_data.update({'success': False, "data": [], "message": "Sorry..!!!you have not Entered "
                                                                           "Email,"
                                                                           "Password,confirm password"})

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
                form_keys = list(form.keys())

                if len(form_keys) < 2:
                    response_data.update({'success': False, "data": [], "message": " some values are missing"})
                    Response(self).jsonResponse(status=404, data=response_data)
                data = {}
                data['username'] = form['username'].value
                data['password'] = form['password'].value
                response_data = {'success': True, "data": [], "message": ""}
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

    def forgot_password(self):
        try:
            if self.path == '/forgot':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST',
                             'CONTENT_TYPE': self.headers['Content-Type'],
                             })
                response_data = {'success': True, "data": [], "message": ""}
                my_db_obj = DbManaged()
                data = {}
                data['password'] = form['password'].value
                success = my_db_obj.check_password(data)
                # result = success[0][0]
                # print(result)
                # print(data["password"])
                # if data["password"] == result:
                if success:
                    response_data.update({"message": "Please Enter Username and New Password"})
                    Response(self).jsonResponse(status=202, data=response_data)
                    password = {}
                    data['username'] = form['username'].value
                    password['password'] = form['password'].value
                    success = my_db_obj.update_password(data, password)
                    if success:
                        response_data.update({"message": "Successfully changed password"})
                        Response(self).jsonResponse(status=202, data=response_data)
                else:
                    response_data.update({"message": "Entered password did not match..Please Enter a Valid Password"})
                    Response(self).jsonResponse(status=202, data=response_data)
        except KeyError:
            pass

import cgi
import sys
import os
from email.mime.multipart import MIMEMultipart
import smtplib

import jwt

sys.path.insert(0, '/home/admin-1/PycharmProjects/FunDooapp/model')

sys.path.insert(0, '/home/admin-1/PycharmProjects/FunDooapp/view')
from query import DbManaged
from response import Response

my_db_obj = DbManaged()


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
                form_keys = list(form.keys())
                if len(form_keys) < 3:
                    response_data.update({'success': False, "data": [], "message": " some values are missing"})
                    Response(self).jsonResponse(status=404, data=response_data)
                # my_db_obj = DbManaged()
                data = {}
                data['email'] = form['email'].value
                data['password'] = form['password'].value
                data['confirm_password'] = form['confirm_password'].value
                # if not my_db_obj.email_validate(form['email'].value):
                success = my_db_obj.email_address_exists(data)
                present = my_db_obj.email_validate(form['email'].value)
                if not present:
                    response_data.update(
                        {"message": "Email Format is Invalid please Re-enter Email", "success": False})
                    Response(self).jsonResponse(status=202, data=response_data)
                else:
                    if success:
                        my_db_obj.registration(data)
                        response_data.update({"success": True, "data": [], "message": "Registration Done Successfully"})
                        Response(self).jsonResponse(status=202, data=response_data)
                    else:
                        response_data.update({"message": "Email Already Exists", "success": False})
                        Response(self).jsonResponse(status=202, data=response_data)
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
            # my_db_obj = DbManaged()
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
        global my_db_obj
        try:
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            response_data = {'success': True, "data": [], "message": ""}
            # my_db_obj = DbManaged()
            data = {}
            data['email'] = form['email'].value
            present = my_db_obj.email_address_exists(data)
            if present:
                response_data.update({"success": False, "message": "Wrong Credentials"})
                Response(self).jsonResponse(status=202, data=response_data)
            else:
                email = data['email']
                encoded = jwt.encode({"email_id": email}, 'secret', algorithm='HS256').decode("utf-8")
                message = f"http://127.0.0.1:8888/reset/?token={encoded}"
                # my_db_obj = DbManaged()
                my_db_obj.smtp(email, message)
                response_data.update({"success": True, "message": "Successfully sent mail"})
                Response(self).jsonResponse(status=202, data=response_data)
                # from urllib.parse import urlparse, parse_qs
                # query_components = parse_qs(urlparse(self.path).query)
                # token = query_components["token"][0]
                # decoded = jwt.decode(token, "secret", algorithms='HS256')
                # print(decoded["email_id"])

        except KeyError:
            pass

    # def reset_password(self):
    #
    #     global my_db_obj
    #     form = cgi.FieldStorage(
    #         fp=self.rfile,
    #         headers=self.headers,
    #         environ={'REQUEST_METHOD': 'POST',
    #                  'CONTENT_TYPE': self.headers['Content-Type'],
    #                  })
    #     response_data = {'success': True, "data": [], "message": ""}
    #     # my_db_obj = DbManaged()
    #     data = {}
    #     print("dhhdj")
    #     data['email'] = form['email'].value
    #     email = data['email']
    #     success = my_db_obj.email_address_exists(email)
    #     if success:
    #         response_data.update({"success": False, "message": "Wrong Credentials"})
    #         Response(self).jsonResponse(status=202, data=response_data)
    #     else:
    #         form_keys = list(form.keys())
    #         if len(form_keys) > 1:
    #             response_data.update({"message": "Something Went Wrong"})
    #             Response(self).jsonResponse(status=202, data=response_data)
    #     msg = MIMEMultipart()
    #     # payload = {'id': "x"}
    #     # key = os.getenv("JWT_SECRET_KEY")
    #     # algorithm = os.getenv("JWT_ALGORITHM")
    #     # encoded = jwt.encode(payload=payload, key=key, algorithm=algorithm)
    #     # print(encoded)
    #     # message = f"http:(127.0.0.1/reset_token/{encoded}"
    #     payload = {email}
    #     key = os.getenv("JWT_SECRET_KEY")
    #     algorithm = os.getenv("JWT_ALGORITHM")
    #     encoded = jwt.encode(payload=payload, key=key, algorithm=algorithm).decode("utf-8")
    #     message = f"http://127.0.0.1:8888/reset_pass/?token={encoded}"
    #     my_db_obj = DbManaged()
    #     my_db_obj.smtp(email, message)
    #     from urllib.parse import urlparse, parse_qs
    #     query_components = parse_qs(urlparse(self.path).query)
    #     token = query_components["token"][0]
    #     decoded = jwt.decode(token, "secret", algorithms='HS256')
    #     print(decoded["email_id"])
    #     # print(my_db_obj.encode_auth_token(email))
    #     # print("successfully sent email to %s:" % (msg['To']))

    def store(self, key):

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        response_data = {'success': True, "data": [], "message": ""}
        # my_db_obj = DbManaged()
        # response_data = {'success': False, "data": [], "message": "Enter New password in Postman"}
        # Response(self).jsonResponse(status=404, data=response_data)
        data = {}
        data['password'] = form['password'].value
        my_db_obj.update_password(data, key)
        response_data = {'success': False, "data": [], "message": "Password Updated Successfully"}
        Response(self).jsonResponse(status=404, data=response_data)

    def insert(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        # my_db_obj = DbManaged()
        data = {}
        data['tittle'] = form['tittle'].value
        data['description'] = form['description'].value
        data['color'] = form['color'].value
        data['isPinned'] = form['isPinned'].value
        data['isArchive'] = form['isArchive'].value
        data['isTrash'] = form['isTrash'].value
        print(data)
        # my = DbManaged()
        my_db_obj.query_insert(data)
        response_data = {'success': True, "data": [], "message": "Inserted Successfully"}
        Response(self).jsonResponse(status=404, data=response_data)

    def update(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        response_data = {'success': True, "data": [], "message": ""}
        # my_db_obj = DbManaged()
        data = {}
        data['id'] = form['id'].value
        data['tittle'] = form['tittle'].value
        print(data)
        my_db_obj.query_update(data)
        response_data = {'success': True, "data": [], "message": "Updated Successfully"}
        Response(self).jsonResponse(status=404, data=response_data)

    def delete(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        # my_db_obj = DbManaged()
        data = {}
        data['id'] = form['id'].value
        # data['tittle'] = form['tittle'].value
        print(data)
        my_db_obj.query_delete(data)
        response_data = {'success': True, "data": [], "message": "Deleted Successfully"}
        Response(self).jsonResponse(status=404, data=response_data)

    def read(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        # my_db_obj = DbManaged()
        data = {}
        data['tablename'] = form['tablename'].value
        print(data)
        my_db_obj.query_read(data)
        response_data = {'success': True, "data": [], "message": "Read Successfully"}
        Response(self).jsonResponse(status=404, data=response_data)

    def create(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        # my_db_obj = DbManaged()
        data = {}
        data['tablename'] = form['tablename'].value
        print(data)
        my_db_obj.query_create(data)
        response_data = {'success': True, "data": [], "message": "created table Successfully"}
        Response(self).jsonResponse(status=404, data=response_data)
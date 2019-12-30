# import pytest

import sys
import pytest
sys.path.insert(0, '/home/admin-1/PycharmProjects/FunDooapp/view')
from registration import registration

sys.path.insert(0, '/home/admin-1/PycharmProjects/FunDooapp/configration')
from db_connection import db_connection



class TestClass:

    def test_register(self):
        obj = registration
        with pytest.raises(NameError):
            # with pytest.raises(AttributeError):
            obj.register(email, password, confirm_password)
            # form = cgi.FieldStorage()
            # if "email" not in form or "password" not in form or "confirm_password" not in form:
            #     print("<H1>Error</H1>")
            #     print("Please fill in the name and addr fields.")
            #     return
            # print("<p>name:", form["email"].value)
            # print("<p>addr:", form["password"].value)
            # print("<p>addr:", form["confirm_password"].value)

    def test_login(self):
        obj = registration
        with pytest.raises(NameError):
            obj.login(username, password)

    def test_forgotpassword(self):
        obj = registration
        with pytest.raises(NameError):
            obj.forgot_password(email)

    def test_connect(self):
        obj = db_connection
        # with pytest.raises(NameError):
        #     obj.queryExecute()


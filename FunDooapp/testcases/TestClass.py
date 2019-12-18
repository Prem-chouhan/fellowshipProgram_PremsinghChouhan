# import pytest

import sys

sys.path.insert(0, '/home/admin-1/PycharmProjects/FunDooapp/view')


class TestClass:

    def test_register(self):
        obj = registration()
        # with pytest.raises(FileNotFoundError):
        obj.register()

    def test_login(self):
        obj = registration()
        obj.login()

import pytest
from Programs.designpatterns import addresspattren as ap

class TestClass:

    def test_addRecord(self):
        obj = ap.AddressBook()
        with pytest.raises(OSError):
            assert obj.addRecord()

    def test_editRecord(self):
        obj = ap.AddressBook()
        with pytest.raises(OSError):
            assert obj.editRecord("prem")

    def test_deleteRecord(self):
        obj = ap.AddressBook()
        assert obj.deleteRecord("prem") is None

    def test_seachRecord(self):
        obj = ap.AddressBook()
        assert obj.searchRecord("prem") is None

    def test_addressfacade(self):
        obj = ap.AddressFacade()
        with pytest.raises(AttributeError):
            assert obj.startAddressbook()
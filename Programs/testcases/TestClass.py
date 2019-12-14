from json import JSONDecodeError

from Programs.objectorientedprograms.com.bridgelabz.stockmarket import stockmaretutility as st
from Programs.objectorientedprograms.com.bridgelabz.addressbook import addressbook as ab
from Programs.objectorientedprograms.com.bridgelabz.commercial import StockAccount as sa
import pytest


class TestClass:

    def test_total_stock_price(self):
        obj = st.stockPortfolio()
        with pytest.raises(FileNotFoundError):
            obj.total_stock_price()

    def test_answer_add(self):
        obj = st.stock()
        with pytest.raises(FileNotFoundError):
            obj.add("infosys", 200, 100)

    def test_addRecord(self):
        obj = ab.AddressBook()
        with pytest.raises(OSError):
            assert obj.addRecord()

    def test_editRecord(self):
        obj = ab.AddressBook()
        with pytest.raises(OSError):
            assert obj.editRecord("prem")

    def test_deleteRecord(self):
        obj = ab.AddressBook()
        assert obj.deleteRecord("prem") is None

    def test_serachRecord(self):
        obj = ab.AddressBook()
        assert obj.searchRecord("prem") is None

    def test_buy(self):
        obj = sa.stockAccount()
        with pytest.raises(UnboundLocalError):
            assert obj.buy("prem", 20000, "Infosys")

    def test_sell(self):
        obj = sa.stockAccount()
        with pytest.raises(JSONDecodeError):
            assert obj.sell("prem", 20000, "Infosys")

    def test_check_user(self):
        obj = sa.stockAccount()
        with pytest.raises(JSONDecodeError):
            assert obj.check_user("prem")

    def test_check_company(self):
        obj = sa.stockAccount()
        assert obj.check_company("info") is None

    def test_add_user(self):
        obj = sa.stockAccount()
        with pytest.raises(JSONDecodeError):
            assert obj.add_user("prem")

    def test_add_company(self):
        obj = sa.stockAccount()
        with pytest.raises(OSError):
            assert obj.add_company("info") is None

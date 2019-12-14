from Programs.datastructure import Utility as ut
from Programs.datastructure.Utility import linked_list
import pytest


class TestClass:

    def test_prime1(self):
        assert ut.prime1(3, 10) == [3, 5, 7]

    def test_prime1_error(self):
        with pytest.raises(TypeError):
            ut.prime1()

    def test_anagram(self):
        with pytest.raises(AssertionError):
            assert ut.anagram([2, 3, 4])

    def test_factorial(self):
        assert ut.factorial(6)

    def test_add_first(self):
        obj = linked_list()
        assert obj.add_first(20) is None

    def test_push(self):
        obj = linked_list()
        assert obj.push(10) is None

    def test_search_error(self):
        with pytest.raises(TypeError):
            obj = linked_list()
            obj.search_item()

    def test_insert(self):
        obj = linked_list()
        assert obj.insert(10) is None

    def test_add_position(self):
        obj = linked_list()
        with pytest.raises(AttributeError):
            assert obj.add_position(10, 4)

    def test_print_list(self):
        obj = linked_list()
        assert obj.print_list() is None

    def test_delete_end(self):
        obj = linked_list()
        with pytest.raises(AttributeError):
            assert obj.delete_end()

    def test_size(self):
        obj = linked_list()
        assert obj.size() is None

    def test_is_empty(self):
        obj = linked_list()
        assert obj.is_empty() is None

    def test_delete_node(self):
        obj = linked_list()
        assert obj.delete_node(5) is None

    def test_insert_ascending(self):
        obj = linked_list()
        with pytest.raises(AttributeError):
            assert obj.insert_ascending(10)

    def test_sort_ing(self):
        obj = linked_list()
        assert obj.sort_ing([1, 2, 3]) is None

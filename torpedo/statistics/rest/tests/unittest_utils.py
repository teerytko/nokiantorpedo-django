"""
Test Rest utils
"""

from statistics.rest.utils import to_dlist, to_dict
import unittest

class TestUtils(unittest.TestCase):
    def test_to_dlist_empty_list(self):
        # GIVEN empty list
        # WHEN to_dlist is called 
        # THEN empty list is returned
        self.assertEquals(to_dlist([]), [])

    def test_to_dlist(self):
        # GIVEN list with one dictionary
        # WHEN to_dlist is called 
        # THEN list with one sub list is returned
        self.assertEquals(to_dlist([{'test': 1,
                                    'two': 'foo'}]),
                          [[1,'foo']])

    def test_to_dlist_multiple_items(self):
        # GIVEN list with multi dictionary
        # WHEN to_dlist is called 
        # THEN list with one sub list is returned
        self.assertEquals(to_dlist([{'test': 1,
                                    'two': 'foo'},
                                    {'test': 2,
                                    'two': 'bar'}]),
                          [[1,'foo'],
                           [2,'bar']])

    def test_to_dlist_with_columns(self):
        # GIVEN list with one dictionary
        # WHEN to_dlist is called with columns 
        # THEN list with one sub list is returned
        self.assertEquals(to_dlist([{'one': 1,
                                     'two': 'foo',
                                     'three': 4}],
                                   ['one']),
                          [[1]])

    def test_to_one_item_dict(self):
        # GIVEN list with one dictionary
        # WHEN to_dict is called 
        # THEN a dict with name, value pairs is returned
        self.assertEquals(to_dict([{'test': 1,
                                    'two': 'foo'}],
                          'test', 'two'),
                          {1: 'foo'})

    def test_to_item_dict(self):
        # GIVEN list of dictionaries
        # WHEN to_dict is called
        # THEN a dict with name, value pairs is returned
        self.assertEquals(to_dict([{'test': 1,
                                    'two': 'foo'},
                                   {'test': 2,
                                    'two': 'bar'}],
                          'test', 'two'),
                          {1: 'foo',
                           2: 'bar',
                           })

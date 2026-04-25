#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
import sys
import os

# Bu setir Python-a deyir ki, modullari bir ust qovluqda axtarsin
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """max_integer funksiyasini yoxlayan test sinfi."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 5, 2, 1]), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -10, -2]), -1)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

if __name__ == '__main__':
    unittest.main()

import unittest
from pathlib import Path
import os
import jsonfilemaker as jfm

class TestJSONFileMaker(unittest.TestCase):

    def setUp(self):
        self.filename = './test.json'

    def delete_file(self, filename):
        file_location = Path(filename)
        if (file_location.exists()):
            os.remove(filename)

    def test_create_new_json_file(self):
        json = jfm.json(self.filename)
        json.close()
        test_path = Path(self.filename)
        self.assertTrue(test_path.exists())

    def test_opening_and_closing_brackets(self):
        json = jfm.json(self.filename)
        json.close()
        file = open(self.filename, 'r')
        self.assertEqual(['{\n', '}'], file.readlines())
        file.close()

    def test_add_field_one_string_value(self):
        json = jfm.json(self.filename)
        json.add_field('Date', 'Sunday, August 12th 2018')
        json.close()
        file = open(self.filename, 'r')
        self.assertEqual(['{\n','    "Date": "Sunday, August 12th 2018"\n' , '}'], file.readlines())
        file.close()

    def test_add_field_three_number_values(self):
        json = jfm.json(self.filename)
        json.add_field('firstNumber', 5)
        json.add_field('secondNumber', 522)
        json.add_field('thirdNumber', 5.55)
        json.close()
        file = open(self.filename, 'r')
        self.assertEqual(['{\n', '    "firstNumber": 5,\n', '    "secondNumber": 522,\n', '    "thirdNumber": 5.55\n', '}'], file.readlines())
        file.close()

    def test_add_lists(self):
        json = jfm.json(self.filename)
        values = ["First", "Second", 3, 55, "Fifth"]
        json.add_field('listOfItems', values)
        second_values = [1, 2, 3, 4, 5, "Hello", 6]
        json.add_field('secondListOfItems', second_values)
        json.close()
        file = open(self.filename, 'r')
        self.assertEqual(['{\n', '    "listOfItems": [\n', '        "First",\n', '        "Second",\n', '        3,\n', '        55,\n', '        "Fifth"\n', '    ],\n', '    "secondListOfItems": [\n', '        1,\n', '        2,\n', '        3,\n', '        4,\n', '        5,\n', '        "Hello",\n', '        6\n', '    ]\n', '}'], file.readlines())
        file.close()

    def test_full_test(self):
        json = jfm.json(self.filename)
        values = ["First", "Second", 3, 55, "Fifth"]
        json.add_field('listOfItems', values)
        json.add_field('random', 283823823)
        json.add_field('random2', 9129191)
        json.add_field('random3', "random values")
        second_values = [1, 2, 3, 4, 5, "Hello", 6]
        json.add_field('secondListOfItems', second_values)
        json.close()
        file = open(self.filename, 'r')
        self.assertEqual(['{\n', '    "listOfItems": [\n', '        "First",\n', '        "Second",\n', '        3,\n', '        55,\n', '        "Fifth"\n', '    ],\n', '    "random": 283823823,\n', '    "random2": 9129191,\n', '    "random3": "random values",\n', '    "secondListOfItems": [\n', '        1,\n', '        2,\n', '        3,\n', '        4,\n', '        5,\n', '        "Hello",\n', '        6\n', '    ]\n', '}'], file.readlines())
        file.close()

    def tearDown(self):
        self.delete_file(self.filename)
        pass

if __name__ == '__main__':
    unittest.main()
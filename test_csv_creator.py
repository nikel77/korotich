import unittest
import csv
import os


from my_sum.csv_creator import csv_creator

workers_list = [
    {'name': 'Lisa', 'age': 30, 'gender': 'f', 'position': 'Accountant'},
    {'name': 'Mike', 'age': 45, 'gender': 'm', 'position': 'Manager'},
    {'name': 'Nick', 'age': 25, 'gender': 'm', 'position': 'Office Manager'},
    {'name': 'Vera', 'age': 21, 'gender': 'f', 'position': 'Support Manager '},
    {'name': 'Masha', 'age': 33, 'gender': 'f', 'position': 'Accountant'},
    {'name': 'Igor', 'age': 50, 'gender': 'm', 'position': 'Manager'},
    {'name': 'John', 'age': 25, 'gender': 'm', 'position': 'Support'},
    {'name': 'Silvia', 'age': 38, 'gender': 'f', 'position': ' Support Manager'},
    {'name': 'Robert', 'age': 31, 'gender': 'm', 'position': 'Head of department'}
]


class TestCsvCreator(unittest.TestCase):
    def test_csv_header(self):
        expected_data = ['name', 'age', 'gender', 'position']
        csv_creator(workers_list)
        with open('people.csv', 'r') as csvfile:
            filereader = csv.reader(csvfile, delimiter=';')
            self.assertEqual(list(filereader)[0], expected_data)
        os.remove('people.csv')

    def test_csv_column_quantity(self):
        csv_creator(workers_list)
        with open('people.csv', 'r') as csvfile:
            filereader = csv.reader(csvfile, delimiter=';')
            for row in filereader:
                self.assertEqual(len(row), 4)
        os.remove('people.csv')

    def test_csv_full(self):
        csv_creator(workers_list)
        with open('people.csv', 'r') as csvfile:
            filereader = csv.reader(csvfile, delimiter=';')
            result = []
            for row in list(filereader)[1:]:
                result.append({'name': row[0], 'age': int(row[1]), 'gender': row[2], 'position': row[3]})
            self.assertEqual(result, workers_list)
        os.remove('people.csv')

    def test_csv_managers_quantity(self):
        managers_list = csv_creator(workers_list)
        self.assertTrue(len(managers_list) == 5)
        for element in managers_list:
            self.assertTrue(('Manager' in element['position']) is True)
        os.remove('people.csv')


if __name__ == '__main__':
    unittest.main()

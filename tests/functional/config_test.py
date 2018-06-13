import unittest

from tests.functional.TestAbstract import TestAbstract


class AppTest(TestAbstract):

    def test_config_1(self):
        self.add_file('config_1.yml')

        self.assertEqual(self.app.get('parameters').get_parameter('param1'), 'Simple parameter')
        self.assertEqual(self.app.get('parameters').get_parameter('param2'), 'Previous param is: Simple parameter')
        self.assertEqual(self.app.get('parameters').get_parameter('param3'), '"Simple parameter" is a text from first parameter')
        self.assertEqual(self.app.get('parameters').get_parameter('param4.array.first.0'), 'Simple parameter')
        self.assertEqual(self.app.get('parameters').get_parameter('param4.array.first.1'), 'Some text')
        self.assertEqual(self.app.get('parameters').get_parameter('param4.array.first.2'), 'Simple parameter')
        self.assertEqual(self.app.get('parameters').get_parameter('param4.dictionary.hello'), 'Cześć')
        self.assertEqual(self.app.get('parameters').get_parameter('param4.dictionary.hello_bye'), 'Cześć i narazie')

    def test_config_2_and_1(self):
        self.add_file('config_1.yml')
        self.add_file('config_2.yml')

        self.assertEqual(self.app.get('parameters').get_parameter('param5'), 'Simple parameter from another file')
        self.assertEqual(len(self.app.get('parameters').get_parameter('param6')), 3)
        self.assertEqual(self.app.get('parameters').get_parameter('param6.0'), 'Simple parameter')
        self.assertEqual(self.app.get('parameters').get_parameter('param6.1'), 'Some text')
        self.assertEqual(self.app.get('parameters').get_parameter('param6.2'), 'Simple parameter')

if __name__ == '__main__':
    unittest.main()

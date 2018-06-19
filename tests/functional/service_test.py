import unittest

from tests.functional.TestAbstract import TestAbstract


class ServicesTest(TestAbstract):

    def test_service_1(self):
        self.add_file('config_1.yml')
        self.add_file('config_2.yml')
        self.add_file('services_1.yml')
        self.recompile_all()

        self.assertEqual(self.app.get('parameters').get_parameter('param1'), 'Simple parameter from service file')
        self.assertEqual(self.app.get('parameters').get_parameter('param4.array.first.0'), 'Simple parameter from service file')
        self.assertEqual(self.app.get('parameters').get_parameter('param4.array.first.1'), 'Some text')
        self.assertEqual(self.app.get('parameters').get_parameter('param4.array.first.2'), 'Simple parameter from service file')
        self.assertEqual(self.app.get('parameters').get_parameter('param4.dictionary.hello'), 'Cześć')
        self.assertEqual(self.app.get('parameters').get_parameter('param4.dictionary.hello_bye'), 'Cześć i narazie')

if __name__ == '__main__':
    unittest.main()

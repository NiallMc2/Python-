'''
Warning Test by: NMG
Create a test to ensure notifications are sent when temp reaches below 5C or above 30C
Originally created in Source.test_formatter.py Oct 2023
Alpha: 10 NOV 23
'''


import unittest


def Temp_Alert(tests):
    for i, item in enumerate(tests, start=1):
        print(f"Temp Alert Test: Rasp Pi {i} - Temperature is {item['Temperature']}")

class TestTempAlert(unittest.TestCase):
    def test_temp_alert(self):
        Test1 = {'Temperature': '4C'}
        Test2 = {'Temperature': '31C'}

        Temp_Alert([Test1, Test2])


        self.assertLogs('', level='TESTS') 

if __name__ == "__main__":
    unittest.main()


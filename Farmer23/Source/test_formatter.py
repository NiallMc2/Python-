"""
filehandler.py
By NMG Oct 2023
Taken from test_formatter originally created Oct 2023 Exercises_09
"""


import unittest
import formatter

class TestFormatter(unittest.TestCase):
    def test_lower(self):
        test_text = "NIALL MCGRATH"
        result = formatter.convert_lower(test_text)
        self.assertEqual(result, "niall mcgrath")

    def test_upper(self):
        test_text = "Niall McGrath"
        result = formatter.convert_upper(test_text)
        self.assertEqual(result, "NIALL MCGRATH")

if __name__ =="__main__":
    unittest.main()

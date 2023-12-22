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

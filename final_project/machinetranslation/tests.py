import unittest
from translator import english_to_french, french_to_english
 
class TestTranslator(unittest.TestCase):
   
    def test_english_to_french(self):
        """
        This function tests English to French translation.
        """
        self.assertNotEqual(english_to_french("Null"), 'Null')
        # test when null is given as input the output must not be an empty string.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # test when the string 'Hello' is given as imput the output must be 'Bonjour'.
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')
        # test when the string 'Goodbye' is given as imput the output must be 'Au revoir'.
 
    def test_french_to_english(self):
        """
        This function tests French to English translation.
        """
        self.assertNotEqual(french_to_english("Null"), 'Null')
        # test when null is given as input the output must not be an empty string.
        self.assertEqual(french_to_english('Bonjour'),  'Hello')
        # test when the string 'Bonjour' is given as imput the output must be 'Hello'.
        self.assertEqual(french_to_english('Au revoir'),  'Goodbye')
         # test when the string 'Au revoir' is given as imput the output must be 'Goodbye'.
 
if __name__ == '__main__':
    unittest.main()

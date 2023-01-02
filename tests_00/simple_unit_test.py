import unittest

class FirstTestClass(unittest.TestCase):
    def test_upper(self):
        #Arrage
        test_stirng = 'rubiks code'

        #Act
        output = test_stirng.upper()

        #Assert
        self.assertEqual(output,'RUBIKS CODE')
if __name__== '__main__':
    unittest.main()
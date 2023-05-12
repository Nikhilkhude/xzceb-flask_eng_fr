import unittest
from translator import englishToFrench, frenchToEnglish

#to test english to french translation function
class TestEnglishToFrench(unittest.TestCase): #to test english to french translation function
    def test1(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')# tests with result is equal
        self.assertNotEqual(englishToFrench('Hello'),'Hello')# tests with result is not equal 
        self.assertEqual(englishToFrench(' '),' ')# tests with NULL input
        
#to test french to english translation function
class TestFrenchToEnglish(unittest.TestCase):#to test french to english translation function
    def test1(self):#to test french to english translation function
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')# tests with result is equal
        self.assertNotEqual(frenchToEnglish('Bonjour'),'Bonjour')# tests with result is not equal
        self.assertEqual(frenchToEnglish(' '),' ')# tests with NULL input

unittest.main()

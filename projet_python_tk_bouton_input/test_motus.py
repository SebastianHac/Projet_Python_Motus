import unittest

class MotusTestUnit(unittest.TestCase) :
    
    def __init__(self, methodName):
        super().__init__(methodName)
        self.mot1='voitures'
        self.mot2='banane'
        self.mot3='qdz4'
        self.mot4='voiture4'
        self.mot5='voïtures'
        self.mot6=''

    def test_test_mot(self):
        #test si le mot fait la bonne longueur 
        self.assertEqual(len(self.mot1),8)
        self.assertEqual(len(self.mot2),6)
        self.assertEqual(len(self.mot3),4)
        self.assertEqual(len(self.mot4),8)
        self.assertEqual(len(self.mot5),8)
        self.assertEqual(len(self.mot6),0)

    def test_isalpha(self):
        self.assertTrue(self.mot1.isalpha())
        self.assertTrue(self.mot2.isalpha())
        self.assertFalse(self.mot3.isalpha())
        self.assertFalse(self.mot4.isalpha())
        self.assertTrue(self.mot5.isalpha())
        self.assertFalse(self.mot6.isalpha())

if __name__ == '__main__':
    unittest.main()
    
    
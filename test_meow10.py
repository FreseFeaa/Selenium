import unittest

class TestAbs(unittest.TestCase):

    def test_abs1(self):
        self.assertEqual(abs(-50),50,"Должно быть положительное") 
        
    def test_abs2(self):
        self.assertEqual(abs(-50),-50,"Должно быть положительное") 
    
if __name__ == "__main__":
    unittest.main()
    print('Готово')
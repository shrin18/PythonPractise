import unittest
import tests

#gives access to testing functions
class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(tests.add(10,5),15)
        self.assertEqual(tests.add(-1,1),0)
        self.assertEqual(tests.add(-1,-2),-3)
        self.assertEqual(tests.add(19,-9),10)
        self.assertEqual(tests.add(11,3),14)

    def test_sub(self):
        self.assertEqual(tests.subtract(10,5),5)
        self.assertEqual(tests.subtract(-1,1),-2)
        self.assertEqual(tests.subtract(-1,-2),1)
        self.assertEqual(tests.subtract(19,-9),28)
        self.assertEqual(tests.subtract(11,3),8)

    def test_mul(self):
        self.assertEqual(tests.multiply(10,5),50)
        self.assertEqual(tests.multiply(-1,1),-1)
        self.assertEqual(tests.multiply(-1,-2),2)
        self.assertEqual(tests.multiply(19,-9),-171)
        self.assertEqual(tests.multiply(11,3),33)

    def test_div(self):
        self.assertEqual(tests.divide(10,5),2)
        self.assertEqual(tests.divide(-1,1),-1)
        self.assertEqual(tests.divide(-1,1),-1)
        self.assertEqual(tests.divide(19,-1),-19)
        self.assertEqual(tests.divide(33,3),11)

        with self.assertRaises(ValueError):
            tests.divide(10,0)

if __name__ == '__main__':
    unittest.main()

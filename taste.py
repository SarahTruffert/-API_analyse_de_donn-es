import unittest
from back import dico, avg, per_capi

class TestMethods(unittest.TestCase):
    def test_by_country(self):
    
        self.assertEqual({"country": "Algeria", "year": 2017, "value": 130493.653}, dico('Algeria'))
        self.assertNotEqual({"country": "Al", "year": 7, "value": 1.3}, dico('Algeria'))
        self.assertTrue({"country": "Algeria", "year": 2017, "value": 130493.653}, dico('Algeria'))
        self.assertIsNot({"country": "Algeria", "year": 2017, "value": 130493.653}, dico('Algeria'))
        self.assertNotIsInstance(dico('Algeria'),list)
        self.assertIsInstance(dico('Algeria'),dict)
        self.assertEqual(type({"country": "Algeria", "year": 2017, "value": 130493.653}), type(dico('Algeria')))
        

     def test_average_for_year(self):
        self.assertEqual({"year":2017, "total":219666.44571830984}, avg(2017))
        self.assertNotEqual({"year":2017, "total":219666.44571830984}, avg(2016))
        self.assertTrue({"year":2017, "total":219666.44571830984}, avg(2017))
        self.assertIsNot({"year":2017, "total":219666.44571830984}, avg(2017))
        self.assertNotIsInstance(avg(2017),list)
        self.assertIsInstance(avg(2017),dict)
        self.assertEqual(type({"year": 2017, "total" : 219666.44571830984}), type(avg(2017)))



    def test_average_for_year(self):
        self.assertEqual({1975: 7.845, 1985: 6.209, 1995: 5.773, 2005: 5.887, 2010: 5.233, 2015: 4.5, 2016: 4.515, 2017:4.565}, per_capi('France'))
        self.assertNotEqual({1975: 7.84, 1985: 6.209, 1995: 5.773, 205: 5.887, 2010: 5.233, 2015: 4.5, 2016: 4.515, 2017:4.55}, per_capi('France'))
        self.assertTrue({1975: 7.845, 1985: 6.209, 1995: 5.773, 2005: 5.887, 2010: 5.233, 2015: 4.5, 2016: 4.515, 2017:4.565}, per_capi('France'))
        self.assertIsNot({1975: 7.845, 1985: 6.209, 1995: 5.773, 2005: 5.887, 2010: 5.233, 2015: 4.5, 2016: 4.515, 2017:4.56}, per_capi('France'))
        self.assertNotIsInstance(per_capi('france'),list)
        self.assertIsInstance(per_capi('france'),dict)
        self.assertEqual(type({1975: 7.845, 1985: 6.209, 1995: 5.773, 2005: 5.887, 2010: 5.233, 2015: 4.5, 2016: 4.515, 2017:4.565}),type(per_capi('France')))
        
        
if __name__ == '__main__':
    unittest.main()

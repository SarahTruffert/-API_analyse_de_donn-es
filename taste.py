import unittest
from back import dico, avg, per_capi

class TestMethods(unittest.TestCase):
    def test_by_country (self):
        self.assertEqual({
                "country": "Angola", 
                 "value": 0.605, 
                 "year": 2017
                    }, dico(2017))



    def test_average_for_year (self):
        self.assertEqual({"year": "2017", "total": 219666.44571830984}, avg(2017))


    def test_average_for_year (self):
        self.assertEqual({"1975": 7.845, "1985": 6.209, "1995": 5.773, "2005": 5.887, "2010": 5.233, "2015": 4.5, "2016": 4.515, "2017": 4.565}, per_capi("France"))
    
if __name__ == '__main__':
    unittest.main()
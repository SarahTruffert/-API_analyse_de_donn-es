import unittest
from front import app

class TestApiFlask(unittest.TestCase):

#Tester l'API

    #Lance mon app 
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

#Fait le chemin jusqu'a "/"
    def test_home_status_code(self):
        result = self.app.get('/') 
        self.assertEqual(result.status_code, 200) 
        # ".status_code = renvoie, si marche = 200 (ok)

    def test_home_data(self):
        result = self.app.get('/')
        # renvoit data
        self.assertEqual(result.data, b'"Hello, World!"\n')

# tester si c'est bien une app j.son : content_type
    def test_home_type(self):
        result = self.app.get('/')
        self.assertEqual(result.content_type,'application/json')


# tester si le mot dedans, est il dedans ? OUI
    def test_home_word(self):
        result = self.app.get('/')
        self.assertTrue(result.data,'Hello')

#Tester les fonctions : 

#def by_country(country):
    def test_home_by_country(self):
        result = self.app.get('/latest_by_country/Albania')
        self.assertTrue(b'country'in result.data)

# fonction average :
    def test_average_by_year_data(self):
        result = self.app.get("/average_by_year/1975")
        self.assertTrue(b'year' in result.data)
     
# # fonction ('/per_capita/<country>')
#     def test_per_capita(self):
#         result = self.app.get('/per_capita/Algeria')
#         self.assertNotEqual(b'footnotes' in result.data)


if __name__ == '__main__':
    unittest.main()
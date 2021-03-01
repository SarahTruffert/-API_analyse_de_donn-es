import unittest
from fichier_api import app

class TestApiFlask(unittest.TestCase):


    def setUp(self):
        """ def setup run app
        """
        self.app = app.test_client()
        self.app.testing = True 


    def test_home_status_code(self):
        """ def status_code test if path is ok "/"
         """
        result = self.app.get('/') 
        self.assertEqual(result.status_code, 200) 
        # ".status_code = renvoie, si marche = 200 (ok)


    def test_home_data(self):
        """ def data test data "Hello word" 
        """
        result = self.app.get('/')
        # renvoit data
        self.assertEqual(result.data, b'"Hello, World!"\n')


    def test_home_type(self):
        """ test_home_type test if te app is j.son content
         """
        result = self.app.get('/')
        self.assertEqual(result.content_type,'application/json')


    def test_home_word(self):
        """ Test if the word is includes 
        """
        result = self.app.get('/')
        self.assertTrue(result.data,'Hello')


        """ Test les fonctions @app: 
        """

#def by_country(country):
    def test_home_by_country(self):
        """by_country test si country figure dans la requête
        """
        result = self.app.get('/latest_by_country/Albania')
        self.assertTrue(b'country'in result.data)

# fonction average :
        """ test average by year test si year figure dans la requête
        """
    def test_average_by_year_data(self):
        result = self.app.get("/average_by_year/1975")
        self.assertTrue(b'year' in result.data)
     
# fonction ('/per_capita/<country>')
        """ Test per_capita si year ne figure pas dans la 
        """
    def test_per_capita(self):
        result = self.app.get('/per_capita/Algeria')
        self.assertFalse(b'year' in result.data)


if __name__ == '__main__':
    unittest.main()

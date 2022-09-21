from django.test import TestCase

# Create your tests here.
class CatalogViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_view_url(self):
        response = self.client.get('/mywatchlist/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/mywatchlist/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'watchlist.html')

    def test_view_html(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_view_xml(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_view_json(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
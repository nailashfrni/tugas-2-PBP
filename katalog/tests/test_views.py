from django.test import TestCase

from katalog.models import CatalogItem

class CatalogViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create 10 catalog items
        number_of_items = 10

        for item in range(number_of_items):
            CatalogItem.objects.create(item_name="Gelas Mug", item_price=38900, item_stock=5, 
                                        description="Gelas sederhana yang bagus", rating=5, 
                                        item_url='https://shopee.co.id/gosale.id/5182917775')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/katalog/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/katalog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'katalog.html')
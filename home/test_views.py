from django.test import TestCase


class TestIndex(TestCase):
    """
    Test home view to ensure it renders correct template
    """
    def test_get_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

class TestViewCart(TestCase):
    """
    Test home view to ensure it renders correct template
    """
    def test_view_cart(self):
        response = self.client.get('/shopping_cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

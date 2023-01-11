from unittest import TestCase
from app import app

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class FlaskTests(TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_form(self):
        """test if form shows up"""
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<p class="h2">Convert Currency</p>', html)

    # def test_submit(self):
    #     """test if form works"""
    #     with app.test_client() as client:
    #         resp = client.post(
    #             "/convert", date={'source-currency': 'USD', 'target-currency': 'USD', 'amount': 1})
    #         html = resp.get_data(as_text=True)

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn('success', html)

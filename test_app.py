import unittest
from unittest.mock import Mock
import app  # Import your function app code

class TestFunctionApp(unittest.TestCase):

    def test_main_with_name_param(self):
        req = Mock(params={'name': 'TestUser'}, get_json=lambda: None)
        response = app.main(req)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_body().decode(), "Hello, TestUser. This HTTP triggered function executed successfully.")

    def test_main_with_name_body(self):
        req = Mock(params={}, get_json=lambda: {'name': 'TestBodyUser'})
        response = app.main(req)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_body().decode(), "Hello, TestBodyUser. This HTTP triggered function executed successfully.")

    def test_main_no_name(self):
        req = Mock(params={}, get_json=lambda: None)
        response = app.main(req)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_body().decode(), "Please pass a name on the query string or in the request body")

if __name__ == '__main__':
    unittest.main()
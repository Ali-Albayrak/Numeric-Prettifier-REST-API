import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestPrettifyEndpoint(unittest.TestCase):
    def test_valid_numbers(self):
        valid_test_cases = [
            ("500", "500"),
            ("3400", "3.4K"),
            ("1000000", "1.0M"),
            ("2500000.34", "2.5M"),
            ("1123456789", "1.1B"),
            ("0","0"),
            ("-500", "-500"),
            ("-3400.23", "-3.4K"),
            ("-1000000", "-1.0M"),
            ("-2500000.34", "-2.5M"),
            ("-1123456789", "-1.1B"),

            ("1203,456", "1.2K"),
        ]
        for input_str, expected_output in valid_test_cases:
            response = client.get(f"/prettify/{input_str}")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["prettified_number"], expected_output)

    def test_invalid_input_type(self):
        invalid_test_cases = [
            "asd",
            "12x",
            "3.14%",
            "1..2",
            "1.3.1",
            "1234567890123456"
        ]
        
        for input_str in invalid_test_cases:
            response = client.get(f"/prettify/{input_str}")
            self.assertEqual(response.status_code, 400)
            self.assertIn("detail", response.json())

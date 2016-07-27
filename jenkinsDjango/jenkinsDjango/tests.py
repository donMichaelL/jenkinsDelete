from django.test import TestCase

class TestingClass(TestCase):
    def test_number_one(self):
        self.assertEqual(1, 2)

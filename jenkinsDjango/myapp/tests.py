from django.test import TestCase

# Create your tests here.
class TestingClass(TestCase):
    def test_number_one(self):
        print 'hello'
        self.assertEqual(1, 2)

from unittest import TestCase
import homework6


class TestHomework(TestCase):

    def setUp(self):
        """Init"""

    def test_out(self):
        """Test for out"""
        self.assertTrue(homework6.to_json())
        self.assertTrue(homework6.to_yaml())

    def tearDown(self):
        """Finish"""


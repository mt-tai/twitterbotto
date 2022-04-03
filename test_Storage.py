import unittest
from Storage import escape_markdown, link_markdown

class TestEscape(unittest.TestCase):
    def test_escape_markdown(self):
        # Test alphanumeric characters
        result = escape_markdown("foobarbaz123")
        self.assertEqual(result, "foobarbaz123")

        # Test underscore
        result = escape_markdown("__________")
        self.assertEqual(result, "\_\_\_\_\_\_\_\_\_\_")


        # Test underscore and alphanumeric characters
        result = escape_markdown("_cat_dog0_1_2_3_4_")
        self.assertEqual(result, "\_cat\_dog0\_1\_2\_3\_4\_")
        
class TestLink(unittest.TestCase):
    def test_link_markdown(self):
        result = link_markdown("foobarbaz123")
        self.assertEqual(result, "[@foobarbaz123](twitter.com/foobarbaz123/)")

        result = link_markdown("__________")
        self.assertEqual(result, "[@\_\_\_\_\_\_\_\_\_\_](twitter.com/__________/)")

        result = link_markdown("_cat_dog0_1_2_3_4_")
        self.assertEqual(result, "[@\_cat\_dog0\_1\_2\_3\_4\_](twitter.com/_cat_dog0_1_2_3_4_/)")


if __name__ == '__main__':
    unittest.main()
import unittest
import main

class Test(unittest.TestCase):

    def test_find_json_on_page(self):
        test_url = "https://www.vangoghmuseum.nl/en/prints/collection/p2725S2013"
        test_result = "https://vangoghmuseum-assetserver.appspot.com/tiles?id=5524889230376960"

        self.assertEqual(main.find_json_on_page(test_url), test_result)


if __name__ == '__main__':
    unittest.main()
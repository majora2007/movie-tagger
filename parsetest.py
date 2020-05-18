import unittest
import parse

class Test_TestParse(unittest.TestCase):

    def test_parse_nudity(self):
        nude_info = ['Masha is having sex with Sasha in the car.', 
                    'One scene takes place in the city baths where we can see dozens of completly naked women, including Iya and Masha.', 
                    'About 50 women in an area take a bath together. All of the women are completely naked. Genitals and breasts are briefly visible.']
        is_nudity, nudity_score = parse.parse_nudity(nude_info)
        self.assertEqual(is_nudity, True)
        self.assertEqual(nudity_score, 1)
    
    #def test_parse_nudity_2(self):
        # Eurotrip: 0356150


    
if __name__ == '__main__':
    unittest.main()
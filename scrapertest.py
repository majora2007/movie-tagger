import unittest
import scraper

class Test_TestScraper(unittest.TestCase):

    def test_fetch_nudity_info_for_movie(self):
        expected = ['Masha is having sex with Sasha in the car.', 
                    'One scene takes place in the city baths where we can see dozens of completly naked women, including Iya and Masha.', 
                    'About 50 women in an area take a bath together. All of the women are completely naked. Genitals and breasts are briefly visible.']
        result = scraper.fetch_nudity_info('10199640', 'movie')
        self.assertListEqual(result, expected)

        # Eurotrip
        expected = ['Predominantly male nudity including full frontal genitalia. Topless female nudity only', 
                'Jenny flashes her boobs and bra at incoming drivers to get a ride. She is seen to be shirtless, but no nudity. In a deleted scene, the director caputures a shot of her boobs clearly visible.', 
                'Jenny wears a tight blue bikini at the beach. The camera does a full body exam of her outfit and you can see the outline of her breasts through the bra while much of her body is visible. Torso shown, and genitalia faintly outlined through panties.', 
                'Nudity is shown on a beach, woman and men are naked, you see penises and some breasts (Quick and brief, but noticable).', 
                'Naked men (you see penises) get chased by a mob through the street, the public look and laugh at "the size".', 
                'Nudity is from females breasts in some pictures (they are drunk in pictures).',
                'A creepy-looking Italian man gropes a young man as the train they are on goes through many dark tunnels.', 
                'A woman pukes over a man while he\'s driving, and her head is in his lap, the man makes rude noises even though nothing sexual is happening (he says some refrences like, "Oh, that feels nasty. get off it" (meaning lap).', "Numerous Sex scenes. One taking place in a confession booth in the Vatican. Both man and woman are naked and woman's breasts are visible. It is implied that she does oral sex for him. An old lady comes for confession and when she hears strange noises, she tries to peer down inside. A view of female buttocks comes in picture and the buttocks are banging against the glass implying intercourse with loud moaning from the woman.", 'The song "Scotty Doesn\'t Know" is about the singer bragging about having sex with Scott\'s girlfriend Fiona. When singing the song Fiona and the singer look like they are grinding.', 'In one scene a woman in a bikini has beach full of naked men ogling her. Then all the men start to chase after her.', 
                'Three women are topless and one of them is sitting in a small pool. Her breasts and nipples are visible. When a man jumps in the pool, she tries to cover her boobs with her hands and move out. He tells her that she should remove a "something on you" and then he motions towards one of her boob. This makes her reveal her full boobs to him. He asks her to rub under her nipple. Later she pinches her boob and nipple on his advice.', 
                'A woman becomes topless in front of a man. Her boobs and nipples are visible.', 
                'A man visits a BDSM club. There are several women with naked breasts', 
                'A man and a woman kiss wildly in alley. Later she goes down on him and it is suggested that she gives him oral sex. No nudity is visible.', 
                'A woman watches an orange juice commercial in which two topless women are fondling each others boobs.', 
                'A man and woman kiss wildly in a dance bar. They are furiously french kissing each other.']
        result = scraper.fetch_nudity_info('0356150', 'movie')
        self.assertListEqual(result, expected)

    
if __name__ == '__main__':
    unittest.main()
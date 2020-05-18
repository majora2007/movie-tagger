import requests
from lxml import html
from lxml.cssselect import CSSSelector

movie_parental_sex_url = 'https://www.imdb.com/title/tt{0}/parentalguide'

def fetch_nudity_info(id, media_type):
    """ Takes an id and a media_type. Extracts paragraphs of sex/nudity for media type """

    if media_type == 'movie':
        url = movie_parental_sex_url.format(id)
    else:
        raise NotImplementedError('Show lookup isn\'t implemented')
    
    body = requests.get(url).content

    page = html.fromstring(body)
    sel = CSSSelector('#advisory-nudity > ul > li')

    selectors = sel(page)

    return [elem.text.replace('\n', '').strip() for elem in selectors if elem.text.replace('\n', '').strip() != '']
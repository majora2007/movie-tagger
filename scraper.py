import requests
from lxml import html
from lxml.cssselect import CSSSelector

def fetch_nudity_info(id, media_type):
    """ Takes an id and a media_type. Extracts paragraphs of sex/nudity for media type """
    movie_parental_sex_url = 'https://www.imdb.com/title/tt{0}/parentalguide'

    if media_type == 'movie':
        url = movie_parental_sex_url.format(id)
    else:
        raise NotImplementedError('Show lookup isn\'t implemented')
    
    body = requests.get(url).content

    page = html.fromstring(body)
    sel = CSSSelector('#advisory-nudity > ul > li')

    selectors = sel(page)

    return [elem.text.replace('\n', '').strip() for elem in selectors if elem.text.replace('\n', '').strip() != '']

def fetch_known_nudity_moves():

    url = 'https://www.imdb.com/list/ls070980506/'

    r = requests.get(url)

    if r.status_code == 404:
        print('URL not valid.')
        exit(-1)

    page = html.fromstring(r.content)

    headers = page.cssselect('html body#styleguide-v2.fixed div#wrapper div#root.redesign div#pagecontent.pagecontent div#content-2-wide div#main div.article.listo div.lister.list.detail.sub-list div.lister-list div.lister-item.mode-detail div.lister-item-content h3.lister-item-header')
    links = page.cssselect('html body#styleguide-v2.fixed div#wrapper div#root.redesign div#pagecontent.pagecontent div#content-2-wide div#main div.article.listo div.lister.list.detail.sub-list div.lister-list div.lister-item.mode-detail div.lister-item-content h3.lister-item-header a')


    movies = [] #(title, imdbid)

    for header in headers:
        # Get title, get year, get imdb
        title = header.getchildren()[1]
        year = header.getchildren()[2]
        imdbid = title.get('href').split('/')[2]
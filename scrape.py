import requests
from bs4 import BeautifulSoup
import pprint

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'], reverse=True)
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href')
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title' : title, 'link' : href,'votes' : points})
    return sort_stories_by_votes(hn)

def news(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    subtext = soup.select('.subtext')
    links = soup.select('.titleline > a')
    return pprint.pprint(create_custom_hn(links, subtext))


if __name__ == '__main__':
    url = 'https://news.ycombinator.com/'
    news(url)
    i = 2
    url = url + '?p='
    while True:
        more_news = input('want to read more? (y/n)')
        if more_news == 'y':
            new_url = url + str(i)
            news(new_url)
            i+=1
        elif more_news == 'n':
            quit()
        else:
            print('please enter Y/N.')
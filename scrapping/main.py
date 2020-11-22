import requests
from bs4 import BeautifulSoup


class HackerNews:
    def __init__(self):
        self.response = requests.get('https://news.ycombinator.com/news')
        self.soup = BeautifulSoup(self.response.content, 'html.parser')
        self.news = self.soup.select('.athing')

    def json(self):
        items = []
        for item in self.news:
            item_id = item.get('id')
            score_item = self.soup.select(f'#score_{item_id}')
            if len(score_item):
                content = {}
                score = score_item[0].text
                content['id'] = item_id
                content['title'] = item.select('.storylink')[0].text
                content['url'] = item.select('.storylink')[0].get('href')
                content['score'] = int(score.replace(' points', ''))
            items.append(content)
        return sorted(items, key=lambda k: k['score'], reverse=True)


if __name__ == '__main__':
    import pprint
    hn = HackerNews()
    pprint.pprint(hn.json())

import requests
from bs4 import BeautifulSoup


def parser():
    dct = {}
    wiki = 'https://ru.wikipedia.org/'
    url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
    while True:
        print(f'Парсим страницу {url}')
        req = requests.get(url)
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, 'lxml')
            all_li = soup.find(class_='mw-category mw-category-columns').find_all('li')
            for li in all_li:
                dct[li.text[0]] = dct.get(li.text[0], 0) + 1
            try:
                a = soup.find('div', {'id': 'mw-pages'}).find('a', text='Следующая страница').get('href')
                url = wiki + a
            except AttributeError:
                return dct
        else:
            return dct


if __name__ == '__main__':
    result = parser()
    sorted_tuple = sorted(result.items(), key=lambda item: item[0])
    sorted_dct = {key: value for key, value in sorted_tuple}
    for key, value in sorted_dct.items():
        print(f'{key}: {value}')

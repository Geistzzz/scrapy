import requests
from bs4 import BeautifulSoup


class Douban:
    def __init__(self):
        self.URL = "https://movie.douban.com/top250"
        self.start_num = [start_num for start_num in range(0, 250, 25)]
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

    def get_top250(self):
        for start_num in self.start_num:
            html = requests.get(self.URL, params={'start': int(start_num)}, headers=self.header)
            soup = BeautifulSoup(html.text, 'html.parser')
            name = soup.select(
                '#content > div > div.article > ol > li > div > div.info > div.hd > a > span:nth-child(1)')
            for name in name:
                print(name.get_text())


if __name__ == '__main__':
    douban = Douban()
    douban.get_top250()

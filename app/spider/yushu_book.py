from app.libs.httper import HTTP
from flask import current_app


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PRE_PAGE'], self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def calculate_start(self, page):
        return (page-1) * current_app.config['PRE_PAGE']

    @property
    def first(self):
        '''
            返回第一本书的书籍数据，这样做的好处是防止books为空，直接调用第0个元素会报错，同时能够使得语义更加明确
        '''
        return self.books[0] if self.total >= 1 else None


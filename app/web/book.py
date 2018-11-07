from flask import request, jsonify, render_template, flash
import json

from flask_login import current_user

from app.models.gift import Gift
from app.models.wish import Wish
from app.views.trade import TradeInfo
from . import web
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.views.book import BookCollection, BookViewModel
from app import cache


@web.route('/book/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return render_template('search_result.html', books=books)
    else:
        flash('您输入的搜索关键字不符合要求，请重新输入!')
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
@cache.cached(timeout=60)
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    # 获取书籍的详细信息
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                             launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                             launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template('book_detail.html',
                           book=book, wishes=trade_wishes_model,
                           gifts=trade_gifts_model, has_in_gifts=has_in_gifts,
                           has_in_wishes=has_in_wishes)


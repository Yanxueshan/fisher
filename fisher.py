__author__ = 'larry'
__date__ = '2018/7/15 23:49'

from app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=81)

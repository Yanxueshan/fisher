__author__ = 'larry'
__date__ = '2018/8/12 16:40'


from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)

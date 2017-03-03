from flask import Flask, request

app = Flask(__name__)


@app.route('/<name>')
def index(name):
    return '<h1>%s</h1>' % name


@app.route('/')
def index2():
    user_agent = request.headers.get('User-Agent')
    return '<h1>%s</h1>' % user_agent


if __name__ == '__main__':
    app.run(debug=True)

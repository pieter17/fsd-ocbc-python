from flask import (Flask, request)

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login()


def do_the_login():
    return f'Do the login :: used HTTP Request is {request.method}'


def show_the_login():
    return f'Show the login form :: used HTTP Request is {request.method} <br/> and this is login form'


if __name__ == '__main__':
    app.run()
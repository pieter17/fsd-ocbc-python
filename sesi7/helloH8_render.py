from flask import (Flask, render_template)

app = Flask(__name__)


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    age = 20
    pet_list = ['cats', 'dogs', 'birds']
    pet_names = {'cat': 'leo', 'dog': 'brown'}
    return render_template('hello.html',
                           name=name,
                           age=age,
                           pet_list=pet_list,
                           pet_names=pet_names)


if __name__ == '__main__':
    app.run(debug=True)
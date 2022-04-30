from flask import Flask, jsonify, render_template
from random import randrange

from db import db


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    value: int = randrange(10, 21)
    db.insert_data(value=value)
    return jsonify(db.get_data())


if __name__ == '__main__':
    app.run(debug=True)

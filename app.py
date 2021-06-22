from flask import Flask, render_template, request, jsonify
from random import randint
from db import get_database
from bson.json_util import dumps

app = Flask(__name__)

@app.route('/')
def index():
    dice_count = request.args.get('dice_count', default = 1, type = int)
    numbers = []
    total = 0
    for n in range(dice_count):
        random_number = randint(1, 6)
        total += random_number
        numbers.append(random_number)
    return render_template('index.html', dice_count = dice_count, numbers = numbers, total = total)

@app.route('/api/v1/resources/rannad/all', methods = ['GET'])
def api_all():
    dbclient = get_database()
    collections = dbclient['rand']
    return jsonify(dumps(collections.find()))

@app.route('/api/v1/resources/rannad/<nimi>', methods = ['GET'])
def api_get_rand(nimi):
    dbclient = get_database()
    collections = dbclient['rand']
    return jsonify(dumps(collections.find({'nimi': nimi})))

if __name__ == '__main__':
    app.run(debug = True)
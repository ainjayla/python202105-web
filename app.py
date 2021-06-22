from flask import Flask, render_template, request
from random import randint

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

if __name__ == '__main__':
    app.run(debug = True)
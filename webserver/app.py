import csv
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


def write_to_file(**kwargs):
    with open('database.csv', 'a') as db:
        data = csv.writer(db, delimiter=',')
        data.writerow(kwargs.values())


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(**data)
        return data
    else:
        return 'Something wrong Happened!'

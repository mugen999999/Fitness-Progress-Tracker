from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)
DATA_FILE = 'data/workouts.csv'

@app.route('/')
def index():
    workouts = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            workouts = list(reader)
    return render_template('index.html', workouts=workouts)

@app.route('/add', methods=['POST'])
def add():
    entry = {
        'date': request.form['date'],
        'type': request.form['type'],
        'duration': request.form['duration'],
        'calories': request.form['calories']
    }
    file_exists = os.path.exists(DATA_FILE)
    with open(DATA_FILE, 'a', newline='') as csvfile:
        fieldnames = ['date', 'type', 'duration', 'calories']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(entry)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

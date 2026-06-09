from flask import Flask, render_template, request
import os

app = Flask(__name__)
FILE = "schedule.txt"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_schedule')
def get_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f: return f.read()
    return ""

@app.route('/save_schedule', methods=['POST'])
def save_data():
    with open(FILE, "w") as f: f.write(request.data.decode('utf-8'))
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)
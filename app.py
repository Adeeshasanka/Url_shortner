from flask import Flask, render_template
from flask_mysqldb import MySQL
from generator import generate_short_code

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_url', methods=['POST'])
def add_url():
    short_code = generate_short_code()
    return render_template('index.html', message = short_code)


if __name__ == '__main__':
    app.run(debug=True)


    
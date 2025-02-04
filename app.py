from flask import Flask, render_template
from flask_mysqldb import MySQL
from generator import generate_short_code

app = Flask(__name__, template_folder='templates')

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'  # MySQL server host
app.config['MYSQL_USER'] = 'adeesha'  # MySQL username
app.config['MYSQL_PASSWORD'] = 'URL_shortnerDB'  # MySQL password
app.config['MYSQL_DB'] = 'url_shortner_db'  # MySQL database name

mysql = MySQL(app)

@app.route('/<short_code>')
def redirect(short_code):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM url_table')
    urls = cur.fetchall()

    if urls:
        for url in urls:
            if url[1] == short_code:
                your_url = url[2]
                return render_template('index.html', message=your_url)
    else:
        return render_template('index.html', message='fuck everthing!')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_url', methods=['POST'])
def add_url():
    short_code = generate_short_code()
    return render_template('index.html', message = f"http://127.0.0.1:5000/{short_code}")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


    
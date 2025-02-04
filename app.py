from flask import Flask, render_template, redirect, request
from flask_mysqldb import MySQL
from functions import generate_short_code

app = Flask(__name__, template_folder='templates')

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'  # MySQL server host
app.config['MYSQL_USER'] = 'adeesha'  # MySQL username
app.config['MYSQL_PASSWORD'] = 'URL_shortnerDB'  # MySQL password
app.config['MYSQL_DB'] = 'url_shortner_db'  # MySQL database name

mysql = MySQL(app)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    cur = mysql.connection.cursor()
    cur.execute('SELECT url FROM url_table WHERE code_key = %s', (short_code,))
    result = cur.fetchone()
    
    if result:
        return redirect(result[0])
        cur.close()
    else:
        return render_template('index.html', message='Invalid URL! please use a valid URL')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_url', methods=['POST'])
def add_url():
    if request.method == 'POST':
        url = request.form['url']
        cur = mysql.connection.cursor()
        
        while True:
            short_code = generate_short_code()
            cur.execute('SELECT url FROM url_table WHERE code_key = %s', (short_code,))
            result = cur.fetchone()
            if not result:
                break

        cur.execute('INSERT INTO url_table (code_key, url) VALUES (%s, %s)', (short_code, url))
        mysql.connection.commit()
        cur.close()
        return render_template('index.html', message = f"http://127.0.0.1:5000/{short_code}")
    else:
        return render_template('index.html', message = f"wrong request!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


    
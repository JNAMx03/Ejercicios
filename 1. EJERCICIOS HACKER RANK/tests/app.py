from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'fazt_flask'

mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullnamed = request.form['fullname']
        phoned = request.form['phone']
        emaild = request.form['email']
        
        cur = mysql.connection.cursor()
        
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (?, ?, ?)', (fullnamed, phoned, emaild))
        mysql.connection.commit()
        print(fullname)
        print(phone)
        print(email)
        return 'recibido'

@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delete')
def delete_contact():
    return 'delete contact'

if __name__ == '__main__':  #validacion para saber si el archivo que se esta ejecutando es el principal
    app.run(port = 3000, debug = True)
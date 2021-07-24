from flask import Flask
from flask import render_template
from flask import redirect
from flask.helpers import url_for
from flask_mysqldb import MySQL
from flask import request
from flask import flash
from datetime import date, datetime

app = Flask(__name__, template_folder= 'templates')

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='1234'
app.config['MYSQL_DB']='libreria_f&f'

mysql = MySQL(app)

@app.route('/inicio', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html')

@app.route('/login_cliente', methods=['GET', 'POST'])
def ingresoCliente():

    if request.method == 'POST':
        if request.form['usuario_cli'] != 'admin' or request.form['contraseña_cli'] != 'admin':
           
            usuarioCliente = request.form['usuario_cli']
            contraseñaCliente = request.form['contraseña_cli']

            cur = mysql.connection.cursor()

            SQuery= "SELECT usuario_cli from cliente where usuario_cli = %s"
            cur.execute(SQuery,[usuarioCliente])

            usuario = cur.fetchone()

            if (usuario != None):
                return redirect(url_for(homeCliente))
            else:
                flash("Usuario inexistente, intente de nuevo")
            

    return render_template('login_c.html')

@app.route('/login_empleado', methods=['GET', 'POST'])
def ingresoEmpleado():
    return render_template('login_e.html')



@app.route('/registro_empleado', methods=['GET', 'POST'])
def registroEmpleado():
    if request.method == 'POST':
        nombre_emp = request.form['nombre_emp']
        apellido_emp = request.form['apellido_emp']
        email_emp = request.form['email_emp']
        usuario_emp = request.form['usuario_emp']
        contraseña_emp = request.form['contraseña_emp']
        fecha_inicio = date.today()

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO empleado (nombre_emp, apellido_emp, email_emp, usuario_emp, contraseña_emp, fecha_inicio) VALUES (%s, %s, %s, %s, %s, %s)',
        (nombre_emp, apellido_emp, email_emp, usuario_emp, contraseña_emp, fecha_inicio))

        mysql.connection.commit()
        return render_template('home_e.html')
    return render_template('registro_e.html')



@app.route('/registro_cliente', methods=['GET', 'POST'])
def registroCliente():
    if request.method == 'POST':
        nombre_cli = request.form['nombre_cli']
        apellido_cli = request.form['apellido_cli']
        email_cli = request.form['email_cli']
        usuario_cli = request.form['usuario_cli']
        contraseña_cli = request.form['contraseña_cli']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO cliente (nombre_cli, apellido_cli, email_cli, usuario_cli, contraseña_cli) VALUES (%s, %s, %s, %s, %s)',
        (nombre_cli, apellido_cli, email_cli, usuario_cli, contraseña_cli))

        mysql.connection.commit()
        return render_template('home_c.html')#esto no manda a funcion home se queda en registro

    return render_template('registro_c.html')



@app.route('/home_empleado', methods=['GET', 'POST'])
def homeEmpleado():
    return render_template('home_e.html')



@app.route('/home_cliente', methods=['GET', 'POST'])
def homeCliente():
    return render_template('home_c.html')



if __name__ == '__main__':
    app.run(debug = True, port = 5000)
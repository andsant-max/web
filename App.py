#imports
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ta'
mysql = MySQL(app)

app.secret_key = 'mysecretkey' 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrarse')
def redistrars():
    return render_template('registrarse.html')

@app.route('/registrarse', methods=['POST'])
def registrarse():
    if request.method == 'POST':
        telefono = request.form['telefono']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        tipo_documento = request.form['tipo_documento']
        numero_documento = request.form['numero_documento']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuario (telefono, nombre, apellido, correo, contraseña, tipo_documento, numero_documento) rolALUES (%s, %s, %s, %s, %s, %s, %s)', (telefono, nombre, apellido, correo, contraseña, tipo_documento, numero_documento))
        mysql.connection.commit()
        return redirect(url_for('ingresa'))

@app.route('/ingresar')
def ingresa():
    return render_template('ingresar.html')
   
@app.route('/ingresar', methods=['POST'])
def ingresar():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        cur = mysql.connection.cursor()
        cur.execute('SELECT `correo`, `contraseña` FROM usuario WHERE usuario_id_PK = %s', (id))
        mysql.connection.commit()
    return redirect(url_for('home_admin.html'))

@app.route('/menu')
def menu():
    return render_template('menu.html')

#---------------------------------------------------------------------------------------------------------------admin clientes

@app.route('/home_admin')
def home_admin():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuario WHERE rol = "admin"')
    data = cur.fetchall()
    return render_template('home_admin.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        telefono = request.form['telefono']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        tipo_documento = request.form['tipo_documento']
        numero_documento = request.form['numero_documento']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuario (telefono, nombre, apellido, correo, contraseña, tipo_documento, numero_documento) VALUES (%s, %s, %s, %s, %s, %s, %s)', (telefono, nombre, apellido, correo, contraseña, tipo_documento, numero_documento))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('home_admin'))

@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuario WHERE usuario_id_PK = %s', (id,))
    data = cur.fetchall()
    return render_template('edit_contact.html', contact = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        telefono = request.form['telefono']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        tipo_documento = request.form['tipo_documento']
        numero_documento = request.form['numero_documento']
        cur = mysql.connection.cursor()
        cur.execute('''
            UPDATE usuario
            SET telefono = %s,
                nombre = %s,
                apellido = %s,
                correo = %s,
                contraseña = %s,
                tipo_documento = %s,
                numero_documento = %s
            WHERE usuario_id_PK = %s
        ''', (telefono, nombre, apellido, correo, contraseña, tipo_documento, numero_documento, id))
        mysql.connection.commit()
        flash('Contact Updated Successfully')
        return redirect(url_for('home_admin'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur =mysql.connection.cursor()
    cur.execute('DELETE FROM usuario WHERE usuario_id_PK = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('home_admin'))

#---------------------------------------------------------------------------------------------------------------admin probuctos

@app.route('/producto')
def producto():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM producto')
    data = cur.fetchall()
    return render_template('producto.html', producto = data)

@app.route('/add_producto', methods=['POST'])
def add_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio_producto = request.form['precio_producto']
        descripcion = request.form['descripcion']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO producto (nombre, precio_producto, descripcion) VALUES (%s, %s, %s)', (nombre, precio_producto, descripcion))
        mysql.connection.commit()
        flash('Producto Added successfully')
        return redirect(url_for('producto'))
    
@app.route('/edit_producto/<id>')
def get_producto(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM producto WHERE producto_id_PK = %s', (id))
    data = cur.fetchall()
    return render_template('edit_producto.html', producto = data[0])

@app.route('/update_producto/<id>', methods = ['POST'])
def update_producto(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio_producto = request.form['precio_producto']
        descripcion = request.form['descripcion']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE producto
            SET nombre = %s,
                precio_producto = %s,
                descripcion = %s
            WHERE producto_id_PK = %s
        """, (nombre, precio_producto, descripcion, id))
        mysql.connection.commit()
        flash('Producto Updated Successfully')
        return redirect(url_for('producto'))
    
@app.route('/snakej')
def snakej():
    return render_template('snakej.html')


if __name__  == '__main__':
    app.run(port = 5000, debug = True)
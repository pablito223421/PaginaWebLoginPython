
#Instalaciones en el PIP
#pip install flask
#pip install flask-mysqldb

from flask import Flask,render_template,request,redirect,session,flash,url_for
from functools import wraps
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_usuario'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)
 
#Registro de Usuarios
@app.route('/') 
@app.route('/login',methods=['POST','GET'])
def login():
     status=True
     if request.method=='POST':
        correo=request.form["correo"]
        contrasena=request.form["contrasena"]
        cur=mysql.connection.cursor()
        cur.execute("select * from usuarios where correo=%s and contrasena=%s",(correo,contrasena))
        data=cur.fetchone()
        if data:
            session['logged_in']=True
            session['nombreusuario']=data["nombreusuario"]
            flash('Su registro ha sido un exito','es un exito')
            return redirect('home')
        else:
            flash('Es invalido los datos, vuelva a intentarlo','alerta')
     return render_template("login.html")
  
#Verificación de la sesión
def is_logged_in(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('No esta autorizado, por favor inicie la sesión','alerta')
			return redirect(url_for('login'))
	return wrap
  
#Registro de usuarios  
@app.route('/reg',methods=['POST','GET'])
def reg():
    status=False
    if request.method=='POST':
        nombreusuario=request.form["nombreusuario"]
        correo=request.form["correo"]
        contrasena=request.form["contrasena"]
        cur=mysql.connection.cursor()
        cur.execute("insert into usuarios(nombreusuario,contrasena,correo) values(%s,%s,%s)",(nombreusuario,contrasena,correo))
        mysql.connection.commit()
        cur.close()
        flash('Su registro ha sido un exito, entre aquí.','es un exito')
        return redirect('login')
    return render_template("reg.html",status=status)

#Página principal
@app.route("/home")
@is_logged_in
def home():
	return render_template('home.html')
    
#Inicio de sesión
@app.route("/logout")
def logout():
	session.clear()
	flash('Ya estas registrado en la pagina','es un exito')
	return redirect(url_for('login'))
    
if __name__=='__main__':
    app.secret_key='secret123'
    app.run(debug=True)





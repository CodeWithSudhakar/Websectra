from flask import Flask, render_template, g, request, url_for, redirect, session
import sqlite3

DATABASE = 'data.db'
DEBUG = True
SECRET_KEY = 'jksdfsdfjiosdf'


app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('Websectra_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route("/home")
def home():
	current = g.db.execute('select * from user where id = ?',[session.get('id')])
	current = current.fetchall()
	current_posts = g.db.execute('select * from posts where uid = ?',[session.get('id')])
	name = current[0][1]
	current_posts = current_posts.fetchall()
	another_posts = g.db.execute('select * from posts where uid <> ?',[session.get('id')]).fetchall()
	return render_template("home.html",name=name,current_posts=current_posts,another_posts=another_posts)

@app.route("/")
def index():
	if bool(session.get('id')):
		return redirect(url_for('home'))
	return render_template("landing.html")

@app.route("/login", methods = ['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		exists = g.db.execute('select * from user where email = ? and password = ? ',[request.form['email'],request.form['pwd']])
		l=exists.fetchall()
		if len(l):
			
			session['id']=l[0][0]
			return redirect(url_for('home'))
		else:
			error = 'Invalid'
	return error


@app.route("/signup", methods = ['GET', 'POST'])
def signup():
	error = None
	if request.method == 'POST':
		exists = g.db.execute('select * from user where email = ?',[request.form['email']])
		if len(exists.fetchall()):
			error = 'User already exists'
		else:
			g.db.execute('insert into user (name,email,password) values (?,?,?)',[request.form['name'],request.form['email'],request.form['pwd']])
			g.db.commit()
			return redirect(url_for('index'))
	return error

@app.route("/postblog",methods = ['GET','POST'])
def blog():
	error = None
	if request.method == 'POST':
		g.db.execute('insert into posts (title,content,uid) values (?,?,?)',[request.form['title'],request.form['content'],session.get('id')])
		g.db.commit()
		return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('id', None)
    return redirect(url_for('index'))

@app.route('/edit/<e>', methods = ['GET','POST'])
def edit(e):
	if request.method == 'POST':
		if e == "name":
			g.db.execute('update user set name = ? where id = ?',[request.form['param'],session.get('id')])
		else:
			g.db.execute('update user set password = ? where id = ?',[request.form['param'],session.get('id')])
		g.db.commit()
		return redirect(url_for('home'))


if __name__ == '__main__' :
	app.run()
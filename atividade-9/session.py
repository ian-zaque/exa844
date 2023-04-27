from flask import Flask, render_template, request, redirect, session, make_response, url_for
from datetime import datetime, timedelta, timezone
import json

app = Flask(__name__, template_folder='templates')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=60)
app.secret_key = 'Yugioooooh'

@app.route('/')
def toHome():
    return redirect("/home")

@app.route('/home')
def home():
    segundos_vividos = 0

    if 'nascimento' in request.cookies:
        nascimento = request.cookies.get('nascimento') + " 00:00:00"
        segundos_vividos = ( datetime.now() - datetime.strptime(nascimento, '%Y-%m-%d %H:%M:%S') ).total_seconds()
        counter_value = request.args.get('counter',default=0, type=int) + 1

    if 'username' in session:
        username = session['username']
        running_time = (datetime.now(timezone.utc) - session.get('_creation_time'))
        remaining_time = app.permanent_session_lifetime - running_time

        counter_value = request.args.get('counter',default=0, type=int) + 1
        return render_template("index.html", counter=counter_value, username=username, remaining_time=remaining_time, segundos_vividos=segundos_vividos)

    else:
        return 'Exemplo de sessão com campo escondido e cookies! <br> <br> <a href="/login.html">Login</a>'

@app.route("/login.html")
def loginPage():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    nascimento = request.form['nascimento']
    session['username'] = username
    session['_creation_time'] = datetime.now()

    resp = make_response(redirect(url_for('home', nascimento=nascimento)))
    resp.set_cookie('nascimento', str(nascimento).encode('utf-8'), max_age=60)   

    return resp

@app.route("/logout")
def logout():
    resp = make_response(render_template("login.html"))
    resp.set_cookie('nascimento', '0', max_age=0)   
    session.clear()
    return resp

if __name__ == '__main__':
    app.run(debug=True)
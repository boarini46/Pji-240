from flask import Flask
from markupsafe import escape
from flask import render_template
#from sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////univesp.db'
#db = SQLAlchemy(app)
def get_db_connection():
    conn = sqlite3.connect('univesp.db')
    conn.row_factory = sqlite3.Row
    return conn
    
@app.route("/")
def hello_world():
    #self.nome = self.listarnomes()
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM nome_vereadores').fetchall()
    conn.close()
    return render_template('materias-camara.html',teste='Nomes_Vereadores',vereador=posts)#"<p><h1>Hello, World!</h1></p>"

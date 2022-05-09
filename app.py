from flask import Flask, render_template, request
from django.core.paginator import Paginator
import sqlite3
from os.path import exists
from db import db

app = Flask(__name__)

class Conexao(db):
    def __init__(self, bancoDeDados):
        self.bancoDeDados = bancoDeDados

    def conectarBD(self):
        conn = sqlite3.connect(self.bancoDeDados+".sqlite")
        conn.row_factory = sqlite3.Row
        return conn
    
    def verificarDB(self):
        cx = Conexao("data")
        datab = db()

        if exists(self.bancoDeDados+".sqlite"):
            conn = cx.conectarBD()
            cur = conn.cursor()
            stmt = cur.execute("SELECT COUNT(*) FROM vagas").fetchone()[0]
            stmt2 = cur.execute("SELECT COUNT(*) FROM cursos").fetchone()[0]

            if stmt <= 0 and stmt2 <= 0:
                dados_vagas = ["./web-crawler/vagas-ti/vagas-ti.json", "./web-crawler/vagas-geral/vagas-geral.json"]
                for d in dados_vagas:
                    datab.insert_vagas(d)
                datab.insert_cursos("./web-crawler/cursos/cursos.json")
        else:
            datab.create_db()
            dados_vagas = ["./web-crawler/vagas-ti/vagas-ti.json", "./web-crawler/vagas-geral/vagas-geral.json"]
            for d in dados_vagas:
                datab.insert_vagas(d)
            datab.insert_cursos("./web-crawler/cursos/cursos.json")


@app.before_first_request
def inicializar():
    cx = Conexao("data")
    cx.verificarDB()
    return "Inicializando..."
    
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cursos")
def cursos():
    cx = Conexao("data")
    conn = cx.conectarBD()
    cur = conn.cursor()

    stmt = cur.execute("SELECT * FROM vagas WHERE vaga_focada=1 ORDER BY RANDOM()").fetchall()
    conn.commit()
    
    try:
        page_num = int(request.args.get('page', 1))
    except:
        page_num = 1

    paginator = Paginator(stmt, 10)
    objects = list(paginator.get_page(page_num))
    obj = paginator.get_page(page_num)

    return render_template('cursos.html', data=objects, obj=obj)

@app.route("/vagas")
def vagas():
    cx = Conexao("data")
    conn = cx.conectarBD()
    cur = conn.cursor()

    stmt = cur.execute("SELECT * FROM vagas WHERE vaga_focada=1 ORDER BY RANDOM()").fetchall()
    conn.commit()
    
    try:
        page_num = int(request.args.get('page', 1))
    except:
        page_num = 1

    paginator = Paginator(stmt, 10)
    objects = list(paginator.get_page(page_num))
    obj = paginator.get_page(page_num)

    return render_template('vagas.html', data=objects, obj=obj)

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/institucional")
def institucional():
    return render_template("institucional.html")

@app.route("/dados")
def dados():
    datab = db()
    dados = datab.get_data_grafico()
    return render_template("dados.html", data = dados)

if __name__ == "__main__":
    app.run()
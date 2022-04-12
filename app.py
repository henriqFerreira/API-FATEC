from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cursos")
def cursos():
    return render_template("cursos.html")

@app.route("/vagas")
def vagas():
    return render_template("vagas.html")

if __name__ == "__main__":
    app.run()
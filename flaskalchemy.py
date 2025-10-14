from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tarefas.db"
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    concluida = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<task {self.titulo}>"
    
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    nova_tarefa = Task(titulo="Estudando Flas+BD+Template", descricao="Integrando as tecnologias")
    db.session.add(nova_tarefa)
    db.session.commit()

    tarefas = Task.query.all()
    return render_template("index.html", tarefas=tarefas)

if __name__ == "__main__":
    app.run(debug=True)
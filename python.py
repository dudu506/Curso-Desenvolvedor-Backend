from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Banco de Dados   .db'
db = SQLAlchemy(app)

class Task (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descrição = db.Column(db.String(200))
    concluida = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.titulo}>'
    
with app.app_context():
    db.create_all()

with app.app_context():
    nova_tarefa = Task(titulo= "Estudar Flask", descrição= "Aprender sobre modelagem de dados")
    db.session.add(nova_tarefa)
    db.session.commit()
    tarefas = Task.query.all()
    print(tarefas)      
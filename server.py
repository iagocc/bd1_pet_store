from flask import Flask, render_template
from flask import g
from pathlib import Path

from mysql.connector import connect

from src.pet import Pet
from src.owner import Owner

app = Flask(__name__, template_folder=Path("src/views"))


# Criar a conexão na primeira requisição e deixa salvo no contexto da aplicacão
@app.before_request
def connect_db():
    if "db" not in g:
        # Preencher com os dados da sua conexão
        g.db = connect(
            host="HOST",
            user="USUARIO",
            password="SENHA",
            database="DATABASE",
        )


# Quando a aplicação for finalizada a conexão é fechada
@app.teardown_appcontext
def disconnect_db(exception):
    db = g.pop("db", None)

    if db is not None:
        db.close()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/pets")
def list_pets():
    cur = g.db.cursor()
    cur.execute("SELECT * FROM pet, pet_owner WHERE pet.owner_id = pet_owner.id")
    results = cur.fetchall()  # Obetenhos os resultados da consulta acima

    pets = []  # crio uma lista que guardará todos os objetos criados do tipo pet
    for row in results:
        owner = Owner(
            name=row[7], cpf=row[6], contact=row[8]
        )  # Crio o objeto tutor para que eu possa criar o objeto pet
        pet = Pet(
            name=row[1], type=row[2], breed=row[3], owner=owner
        )  # Crio o objeto pet
        pets.append(pet)  # Adiciono o objeto na lista criada

    return render_template(
        "list_pets.html", pets=pets
    )  # renderizo o template passando a lista

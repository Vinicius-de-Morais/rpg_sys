from flask import Flask, render_template, request
from main import Personagem

app = Flask('__name__', template_folder='template', static_folder='template')


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        nome = request.form['nome'].title()
        raca = request.form['raca'].capitalize()
        idade = request.form['idade']
        altura = float(request.form['altura'])
        peso = request.form['peso']
        genero = request.form['genero']
        classe = request.form['classe'].title()

        personagem = Personagem(nome, raca, idade, altura, peso, genero, classe)

        return render_template('Ficha.html', nome=nome, raca=raca, idade=idade, altura=altura, peso=peso,
                               genero=genero, classe=classe, personagem=personagem)

    return render_template('formulario.html')


app.run()

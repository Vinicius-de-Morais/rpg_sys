from flask import Flask, render_template, request
from main import Personagem, Atributos
from raças import DefineRaca
from flask_wtf import FlaskForm
from wtforms.fields import SelectField, StringField, FloatField

app = Flask('__name__', template_folder='template', static_folder='template')
app.config['SECRET_KEY'] = 'vinicius'


class Form(FlaskForm):
    nome = StringField('Nome')
    raca = SelectField('Raça', choices=DefineRaca.racas())
    idade = StringField('Idade')
    altura = FloatField('Altura')
    peso = StringField('Peso')
    genero = StringField('Genero')
    classe = SelectField('Classe', choices=Atributos.retorna_classes())


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    if request.method == 'POST':
        nome = request.form.get('nome').title()
        raca = request.form.get('raca').capitalize()
        idade = request.form.get('idade')
        altura = float(request.form.get('altura').replace(',', '.'))
        peso = request.form.get('peso')
        genero = request.form.get('genero')
        classe = request.form.get('classe')

        personagem = Personagem(nome, raca, idade, altura, peso, genero, classe)

        return render_template('ficha.html', personagem=personagem)

    return render_template('formulario.html', form=form)


@app.route("/informacoes")
def info():
    return render_template('informacoes.html')


if '__main__' == __name__:
    app.run()

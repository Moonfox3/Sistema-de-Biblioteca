from flask import Flask, render_template
from controller.biblioteca_controller import BibliotecaController

app = Flask(__name__)
controller = BibliotecaController()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar_livro')
def cadastrar_livro():
    controller.cadastrar_livro()
    return 'Livro cadastrado com sucesso!'

@app.route('/listar_livros')
def listar_livros():
    livros = controller.listar_livros()
    return render_template('index.html', livros=livros)

@app.route('/emprestar_livro')
def emprestar_livro():
    controller.emprestar_livro()
    return 'Livro emprestado com sucesso!'

@app.route('/devolver_livro')
def devolver_livro():
    controller.devolver_livro()
    return 'Livro devolvido com sucesso!'

if __name__ == "__main__":
    app.run(debug=True)

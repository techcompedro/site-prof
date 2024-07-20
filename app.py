from flask import Flask, render_template


app = Flask(__name__)


alunos = [
    {'avatar': '.','nome': 'pedro', 'idade': '17', 'aniversario': '03-05-2007', 'graduação': 'faixa azul', 'grau': '1'}
    ]

@app.route('/')
def inicio():
    return render_template('index.html',
                           alunos = alunos)



@app.route('/turmas.html')
def turmas():
    return render_template('turmas.html',
                           alunos = alunos)


@app.route('/projeto.html')
def projeto():
    return render_template('projeto.html',
                           alunos = alunos)







if __name__ == '__main__':
    app.run(debug=True)
    
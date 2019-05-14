from flask import Flask,render_template,request
from funclass import Funcionario
from Dao import FuncDAO

app = Flask(__name__,template_folder='template')

@app.route('/')
def home():
    return render_template('menu.html')

@app.route('/form')
def form():
    return render_template('form.html',func = '')

@app.route('/envio', methods = ['POST','GET'])
def trata_form():
    nome = request.form['nome']
    id_depto = int(request.form['idDepto'])
    funclass = Funcionario(nome,id_depto)
    if funclass.id!='':
        fundao = FuncDAO().alterar(funclass)
        return listar()
    else:
        fundao = FuncDAO().inserir(funclass)
        return render_template('template.html',user=fundao)

@app.route('/listar')
def listar():
    fundao = FuncDAO().listar()
    return render_template('lista.html',funcionarios=fundao)

@app.route('/deletar', methods = ['GET'])
def deletar():
    id = request.args.get('id')
    fundao = FuncDAO().deletar(int(id))
    return listar()

@app.route('/alterar', methods = ['GET'])
def alterar():
    cod = request.args.get('id')
    fundao = FuncDAO().buscar(int(cod))
    return render_template('form.html', func = fundao)


def main():
    app.env = 'development'
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()

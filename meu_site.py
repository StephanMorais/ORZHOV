from flask import Flask,render_template,request, flash


app=Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/organizacao")
def org():
    return render_template("org.html")

@app.route("/denuncia")
def denuncia():
    return render_template("denuncia.html")

@app.route("/filiacao")
def filiacao():
    return render_template("filiacao.html")

@app.route("/loja")
def loja():
    return render_template("loja.html")

@app.route("/cadastrar", methods=['POST'])
def cadastrar():
    user=[]
    
    nome = request.form.get('nome')
    guilda = request.form.get('guilda')
    profissao = request.form.get('profissao')
    situacaoEconomica = request.form.get('RENDA')
    corPrincipal = request.form.get('cor')
    comprovante = request.form.get('CIENCIA')
    user=[{
        "nome":nome,
        "guilda":guilda,
        "profissão":profissao,
        "Situação Economica":situacaoEconomica,
        "Cor primária": corPrincipal,
        "Comprovante":comprovante
    }]
    flash('Solicitação enviada com sucesso. Aguarde o retorno.')
    with open('solicitacoesCadastro.json') as solicitacoesCadastro:
        arquivos=json.load(solicitacoesCadastro)
    arquivo=arquivos+user
    with open('solicitacoesCadastro.json', 'w') as responder:
        json.dumps(arquivo, arquivos, indent=4)
        return render_template("filiacao.html")

       

    


if __name__=="__main__":
    app.run(debug=True)
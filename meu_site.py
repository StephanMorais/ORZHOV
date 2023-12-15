from flask import Flask,render_template

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



if __name__=="__main__":
    app.run(debug=True)
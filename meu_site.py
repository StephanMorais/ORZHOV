from flask import Flask,render_template,request, redirect, json, jsonify
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import sqlite3


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

@app.route("/cadastrar", methods=['POST',"GET"])
def cadastrar():
    
   con=sqlite3.connect('dados.db') 
   with con:
       cur=con.cursor()
       cur.execute("IF NOT EXISTS CREATE TABLE SOLICITACOES(NOME TEXT,GUILDA TEXT, PROFISSAO TEXT, RENDA TEXT COR TEXT)")
       
       
    

       

    


if __name__=="__main__":

    app.run(debug=True)
    
    
import pandas as pd
from flask import Flask, jsonfy

app=Flask(__name__)

@app.route('/')

def home():
    return 'Teste API'

@app.route('/vendas')
def vendas():
    tabela = pd.read_csv('advertising.csv')
    total_vendas = tabela['vendas'].sum()
    result= {'Total de Vendas',total_vendas}

    return jsonfy(result)

app.run(host='0.0.0.0')

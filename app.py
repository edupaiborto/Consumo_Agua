from flask import Flask, render_template, request
import pandas as pd
import matplotlib

matplotlib.use('Agg')  # Use 'Agg' backend for rendering graphs in a web environment
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Carregar os dados de consumo de água
data = pd.read_csv('dados/dados_consumo_agua.csv')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analise', methods=['POST'])
def analise():
    acao = request.form['acao']

    # Filtrar os dados de acordo com a ação escolhida
    filtro_acao = data[data['Praticas_Economia'] == acao]

    # Gráfico do consumo real
    plt.figure(figsize=(10, 5))
    plt.bar(data['Residencia'], data['Consumo_Mensal'], color='blue', label='Consumo Real')

    # Estimar o consumo após aplicar a prática escolhida
    reducao = {
        'Fechamento de torneiras': 0.10,
        'Conserto de vazamentos': 0.15,
        'Uso de dispositivos economizadores': 0.20
    }

    consumo_estimado = data['Consumo_Mensal'] * (1 - reducao[acao])

    # Gráfico do consumo estimado
    plt.bar(data['Residencia'], consumo_estimado, color='green', alpha=0.7, label=f'Consumo com {acao}')
    plt.xlabel('Residência')
    plt.ylabel('Consumo Mensal (Litros)')
    plt.legend()

    # Salvar o gráfico
    grafico_path = os.path.join('static', 'grafico_comparativo.png')
    plt.savefig(grafico_path)
    plt.close()

    return render_template('analise.html', grafico_path=grafico_path)


if __name__ == '__main__':
    app.run(debug=True)

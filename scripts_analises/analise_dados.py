import pandas as pd

# Carregar os dados
data = pd.read_csv('dados/dados_consumo_agua.csv')

# Função para calcular a economia estimada
def calcular_economia(pratica):
    media_consumo = data['Consumo_Mensal'].mean()
    economia = 0
    if pratica == "Fechamento de torneiras":
        economia = media_consumo * 0.10  # 10% de economia
    elif pratica == "Conserto de vazamentos":
        economia = media_consumo * 0.15  # 15% de economia
    elif pratica == "Uso de dispositivos economizadores":
        economia = media_consumo * 0.20  # 20% de economia
    return economia

# Teste da função
for pratica in data['Praticas_Economia'].unique():
    economia = calcular_economia(pratica)
    print(f"Prática: {pratica}, Economia estimada: {economia:.2f} litros")

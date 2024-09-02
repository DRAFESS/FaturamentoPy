import json

def calcular_faturamento(data):
    valores = [dia['valor'] for dia in data['faturamento_diario'] if dia['valor'] > 0]

    if not valores:
        return "Não há valores de faturamento disponíveis para cálculo."

    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

with open('faturamento.json', 'r') as file:
    data = json.load(file)

menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_faturamento(data)

print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

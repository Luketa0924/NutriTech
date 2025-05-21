import matplotlib.pyplot as plt

def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)

def calcular_gasto_calorico(peso, met, duracao_min):
    return round((met * peso * 3.5 / 200) * duracao_min, 2)

def gerar_feedback(imc, metas_batidas):
    if imc < 18.5:
        return "Atenção: paciente com baixo peso."
    elif imc > 25:
        return "Paciente acima do peso. Reforçar plano."
    if metas_batidas:
        return "Parabéns! O paciente está no caminho certo."
    return "Paciente em progresso. Acompanhar evolução."

def gerar_grafico_evolucao(pesos, datas, nome):
    plt.plot(datas, pesos, marker='o')
    plt.title(f"Evolução de Peso - {nome}")
    plt.xlabel("Data")
    plt.ylabel("Peso (kg)")
    plt.grid(True)
    plt.savefig(f"evolucao_peso_{nome}.png")
    plt.close()
# grafico.py
import matplotlib.pyplot as plt

def gerar_grafico():
    categorias = ['Janeiro', 'Fevereiro', 'Março']
    verde = [70, 65, 80]
    laranja = [20, 25, 10]
    vermelho = [10, 10, 10]

    largura = 0.25
    x = [i for i, _ in enumerate(categorias)]

    plt.figure(figsize=(6, 4))
    plt.bar([i - largura for i in x], verde, width=largura, color='#4CAF50', label='Meta')
    plt.bar(x, laranja, width=largura, color='#FFA500', label='Intermédio')
    plt.bar([i + largura for i in x], vermelho, width=largura, color='#FF6347', label='Baixo')

    plt.xticks(x, categorias)
    plt.title("Progresso Geral")
    plt.legend()
    plt.tight_layout()
    plt.savefig("grafico.png")

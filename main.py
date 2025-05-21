from database import criar_tabelas
from models import cadastrar_paciente, listar_pacientes_por_objetivo, cadastrar_plano_alimentar, registrar_acompanhamento, obter_dados_evolucao
from processamento import gerar_grafico_evolucao

criar_tabelas()

# Exemplo de uso
cadastrar_paciente("Maria", 30, "F", 65, 1.65, "emagrecer", "maria@gmail.com", "Hipertensão", "sedentário")
pacientes = listar_pacientes_por_objetivo("emagrecer")
print("Pacientes com objetivo de emagrecer:")
for paciente in pacientes:
    print(paciente[0])

# Cadastro de plano alimentar
cadastrar_plano_alimentar(1, "Café, Almoço, Jantar", "Ovos, Arroz, Frango", "2, 1, 1", 1800, "Carb: 40%, Prot: 30%, Gord: 30%", "Plano inicial", True)

# Registro de acompanhamento
registrar_acompanhamento(1, "2025-05-01", 65, {"cintura": 80, "altura": 1.65}, "Paciente iniciou plano.", "Sem alertas")
registrar_acompanhamento(1, "2025-05-15", 63.5, {"cintura": 78, "altura": 1.65}, "Boa evolução", "")

# Geração de gráfico de evolução
datas, pesos = obter_dados_evolucao(1)
gerar_grafico_evolucao(pesos, datas, "Maria")

# Geração do pdf da evolução
from exportacao import exportar_relatorio_pdf

dados = [
    "Peso atual: 70 kg",
    "Objetivo: Emagrecer",
    "Plano alimentar: Café, Frango, Arroz",
    "Evolução: perdeu 3 kg em 2 semanas"
]

exportar_relatorio_pdf("Maria", dados, "relatorio_maria.pdf")

# Login da Nutricionista
from models import cadastrar_nutricionista, autenticar_nutricionista

# Cadastro (executar uma vez)
cadastrar_nutricionista("lucasv", "senha123")

# Login
if autenticar_nutricionista("lucasv", "senha123"):
    print("Login bem-sucedido! Acesso autorizado.")
else:
    print("Usuário ou senha inválidos.")


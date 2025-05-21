import sqlite3
import hashlib
from database import conn, cursor
from database import conectar
from processamento import calcular_imc

def cadastrar_paciente(nome, idade, sexo, peso, altura, objetivo, contato, historico, nivel):
    imc = calcular_imc(peso, altura)
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Paciente (nome, idade, sexo, peso, altura, imc, objetivo, contato, historico, atividade_nivel)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (nome, idade, sexo, peso, altura, imc, objetivo, contato, historico, nivel))
    conn.commit()
    conn.close()

def listar_pacientes_por_objetivo(objetivo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM Paciente WHERE objetivo = ?", (objetivo,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def cadastrar_plano_alimentar(paciente_id, refeicoes, alimentos, porcoes, calorias, macros, observacoes, ativo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO PlanoAlimentar (paciente_id, refeicoes, alimentos, porcoes, calorias, macros, observacoes, ativo)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                   (paciente_id, refeicoes, alimentos, porcoes, calorias, macros, observacoes, ativo))
    conn.commit()
    conn.close()

def registrar_acompanhamento(paciente_id, data, peso, medidas, observacoes, alertas):
    imc = calcular_imc(peso, medidas.get('altura', 1.70))  # altura como exemplo
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Acompanhamento (paciente_id, data, peso, imc, medidas, observacoes, alertas)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (paciente_id, data, peso, imc, str(medidas), observacoes, alertas))
    conn.commit()
    conn.close()

def obter_dados_evolucao(paciente_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT data, peso FROM Acompanhamento WHERE paciente_id = ? ORDER BY data", (paciente_id,))
    dados = cursor.fetchall()
    conn.close()
    datas = [d[0] for d in dados]
    pesos = [d[1] for d in dados]
    return datas, pesos

# Login da Nutricionista
import hashlib

def cadastrar_nutricionista(usuario, senha):
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    try:
        cursor.execute('INSERT INTO nutricionista (usuario, senha_hash) VALUES (?, ?)', (usuario, senha_hash))
        conn.commit()
        print("Nutricionista cadastrado!")
    except sqlite3.IntegrityError:
        print("Usuário já existe.")

def autenticar_nutricionista(usuario, senha):
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    cursor.execute('SELECT * FROM nutricionista WHERE usuario = ? AND senha_hash = ?', (usuario, senha_hash))
    return cursor.fetchone() is not None


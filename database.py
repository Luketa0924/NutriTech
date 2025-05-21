import sqlite3

conn = sqlite3.connect("banco_nutri.db")
cursor = conn.cursor()

def conectar():
    return sqlite3.connect("nutri.db")

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Paciente (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        sexo TEXT,
        peso REAL,
        altura REAL,
        imc REAL,
        objetivo TEXT,
        contato TEXT,
        historico TEXT,
        atividade_nivel TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS PreferenciasAlimentares (
        id INTEGER PRIMARY KEY,
        paciente_id INTEGER,
        preferidos TEXT,
        restricoes TEXT,
        estilo TEXT,
        FOREIGN KEY(paciente_id) REFERENCES Paciente(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS AtividadeFisica (
        id INTEGER PRIMARY KEY,
        paciente_id INTEGER,
        tipo TEXT,
        frequencia TEXT,
        duracao TEXT,
        objetivo TEXT,
        gasto_calorico REAL,
        FOREIGN KEY(paciente_id) REFERENCES Paciente(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS PlanoAlimentar (
        id INTEGER PRIMARY KEY,
        paciente_id INTEGER,
        refeicoes TEXT,
        alimentos TEXT,
        porcoes TEXT,
        calorias REAL,
        macros TEXT,
        observacoes TEXT,
        ativo BOOLEAN,
        FOREIGN KEY(paciente_id) REFERENCES Paciente(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Acompanhamento (
        id INTEGER PRIMARY KEY,
        paciente_id INTEGER,
        data TEXT,
        peso REAL,
        imc REAL,
        medidas TEXT,
        observacoes TEXT,
        alertas TEXT,
        FOREIGN KEY(paciente_id) REFERENCES Paciente(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS FotosRefeicoes (
        id INTEGER PRIMARY KEY,
        paciente_id INTEGER,
        data TEXT,
        caminho_imagem TEXT,
        FOREIGN KEY(paciente_id) REFERENCES Paciente(id)
    )''')

    conn.commit()
    conn.close()

# Login Nutricionista
cursor.execute('''
CREATE TABLE IF NOT EXISTS nutricionista (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL
)
''')

import sqlite3

def conectar_banco():
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
    (id INTEGER PRIMARY KEY, usuario TEXT, senha TEXT, email TEXT)''')
    print(type(conexao))

    conexao.commit()

    if __name__ == '__main__':
        conectar_banco()
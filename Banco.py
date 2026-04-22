                 # IMPORTAÇÃO DO SQLITE.
import sqlite3


conexao = sqlite3.connect("Banco.db")
cursor = conexao.cursor()

                # TABELA DO BANCO DE DADOS.
cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias( 
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               titular TEXT NOT NULL, 
               saldo FLOAT NOT NULL,
               cpf TEXT NOT NULL UNIQUE 
              )""")

                # INSERINDO OS DADOS DO BANCO. 

# cursor.execute("""INSERT INTO contas_bancarias
#               (titular, saldo, cpf ) VALUES
#                ('Kai', -4000, '37712892184') """)

cursor.execute("""UPDATE contas_bancarias
               SET saldo = -5000
               WHERE id =  2 """)

# SELECIONAR TODAS COLUNAS # "*" SELECIONA TODA A TABELA.
# PODE SELECIONAR APENAS SALDO, NOME, CPF USANDO SELEC + A INFO NA FRENTE.
cursor.execute("""SELECT  titular, saldo FROM contas_bancarias""")

# PEGA OS RESULTADOS DO COMANDO SELECT = 
contas = cursor.fetchall()

for conta in contas:
     titular,saldo = conta
     print(f"""Titular: {titular}
saldo: {saldo}""")
     print('\n')        


conexao.commit() 



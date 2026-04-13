import os
import sqlite3

nome_banco = 'banco_peca.db'

# CRIAR BANCO E TABELAS


def criar_banco():
    conexao = sqlite3.connect(nome_banco)
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS caixas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status_caixa TEXT DEFAULT 'aberta'
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pecas (
            id_peca INTEGER PRIMARY KEY,
            peso REAL,
            cor TEXT,
            comprimento REAL,
            aprovada INTEGER,
            status TEXT,
            caixa_id INTEGER
        )
    ''')

    # garantir caixa aberta
    cursor.execute("SELECT * FROM caixas WHERE status_caixa = 'aberta'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO caixas (status_caixa) VALUES ('aberta')")

    conexao.commit()
    conexao.close()

# VALIDAR PEÇA


def validar_peca(peso, cor, comprimento):
    erros = []

    if peso < 95 or peso > 105:

        erros.append(" Peso fora do padrão de fabricação \n")

    if cor.lower() not in ['azul', 'verde']:
        erros.append("Cor inválida")

    if comprimento < 10 or comprimento > 20:
        erros.append(" Comprimento fora  do padrão de fabricação ")

    if len(erros) == 0:
        return True, "Aprovada"
    else:
        return False, " | ".join(erros)


# CADASTRAR PEÇA

def cadastrar_peca():
    conexao = sqlite3.connect(nome_banco)
    cursor = conexao.cursor()

    print("\n--- CADASTRO ---")

    id_peca = int(input("ID: "))
    peso = float(input("Peso: "))
    cor = input("Cor: ")
    comprimento = float(input("Comprimento: "))
    aprovada, status = validar_peca(peso, cor, comprimento)
    id_caixa = None

    if aprovada:
        cursor.execute("SELECT id FROM caixas WHERE status_caixa = 'aberta'")
        caixa = cursor.fetchone()

        if caixa:
            id_caixa = caixa[0]

            cursor.execute(
                "SELECT COUNT(*) FROM pecas WHERE caixa_id = ?", (id_caixa,))
            total = cursor.fetchone()[0]

            if total >= 10:
                cursor.execute(
                    "UPDATE caixas SET status_caixa = 'fechada' WHERE id = ?", (id_caixa,))
                cursor.execute(
                    "INSERT INTO caixas (status_caixa) VALUES ('aberta')")
                conexao.commit()

                id_caixa = cursor.lastrowid
                print("Caixa cheia! Nova criada")

    cursor.execute("""
        INSERT INTO pecas (id_peca, peso, cor, comprimento, aprovada, status, caixa_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (id_peca, peso, cor, comprimento, 1 if aprovada else 0, status, id_caixa))

    conexao.commit()
    conexao.close()

    print("Resultado:", status)


# =========================
# LISTAR PEÇAS
# =========================
def listar_pecas():
    conexao = sqlite3.connect(nome_banco)
    cursor = conexao.cursor()

    print("\n FILTRAR PEÇAS")
    print("1 - Aprovadas")
    print("2 - Reprovadas")

    opcao = input("Escolha: ")

    if opcao == "1":
        cursor.execute("SELECT * FROM pecas WHERE status = 'Aprovada'")
    elif opcao == "2":
        cursor.execute("SELECT * FROM pecas WHERE status != 'Aprovada'")
    else:
        print("Opção inválida!")
        conexao.close()
        return

    pecas = cursor.fetchall()

    print("\n" + "="*40)
    print(" RESULTADO")
    print("="*40)

    if not pecas:
        print(" Nenhuma peça encontrada")
    else:
        for p in pecas:
            print("\n" + "-"*40)
            print(f" ID: {p[0]}")
            print(f" Peso: {p[1]} g")
            print(f" Cor: {p[2]}")
            print(f" Comprimento: {p[3]} cm")
            print(f" Status: {p[5]}")

    print("\n" + "="*40)

    conexao.close()
    input("\nPressione Enter...")


# =========================
# REMOVER PEÇA
# =========================


def remover_peca():
    conexao = sqlite3.connect(nome_banco)
    cursor = conexao.cursor()

    id_remove = int(input("ID para remover: "))

    cursor.execute("DELETE FROM pecas WHERE id_peca = ?", (id_remove,))

    if cursor.rowcount > 0:
        print("Removida!")
    else:
        print("Não encontrada")

    conexao.commit()
    conexao.close()


# =========================
# LISTAR CAIXAS
# =========================

def listar_caixas():
    conexao = sqlite3.connect(nome_banco)
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM caixas WHERE status_caixa = 'fechada'")
    caixas = cursor.fetchall()

    print("\n--- CAIXAS FECHADAS ---")

    if len(caixas) == 0:
        print("Nenhuma caixa fechada ainda")
    else:
        for c in caixas:
            print(f"Caixa {c[0]} está fechada")

    conexao.close()


# =========================
# RELATÓRIO
# =========================

def relatorio():
    conexao = sqlite3.connect(nome_banco)
    cursor = conexao.cursor()

    cursor.execute("SELECT COUNT(*) FROM pecas WHERE aprovada = 1")
    aprovadas = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM pecas WHERE aprovada = 0")
    reprovadas = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM caixas WHERE status_caixa = 'fechada'")
    caixas = cursor.fetchone()[0]

    print("\n--- RELATÓRIO ---")
    print("Aprovadas:", aprovadas)
    print("Reprovadas:", reprovadas)
    print("Caixas fechadas:", caixas)

    conexao.close()


# =========================
# MENU
# =========================

def app():
    criar_banco()

    while True:
        print("\n1 - Cadastrar")
        print("2 - Listar peças")
        print("3 - Remover peça")
        print("4 - Listar caixas")
        print("5 - Relatório")
        print("0 - Sair")

        op = input("Opção: ")

        if op == "1":
            cadastrar_peca()
        elif op == "2":
            listar_pecas()
        elif op == "3":
            remover_peca()
        elif op == "4":
            listar_caixas()
        elif op == "5":
            relatorio()
        elif op == "0":
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    app()

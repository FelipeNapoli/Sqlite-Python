import sqlite3

try:
    with sqlite3.connect(r"C:\Users\napol\Desktop\PY\sqlite\ex_sorveteria\dbSorveteria.db") as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()

        cursor.execute("SELECT * FROM tbProduto")

        for item in cursor:
            print(f"O Produto {item['nome']} custa R${item['valor_uni']:.2f}\n")

except sqlite3.Error as erro:
    print(f"Falha no banco: {erro}")

except Exception as erro:
    print(f"Ocorreu um problema no programa: {erro}")
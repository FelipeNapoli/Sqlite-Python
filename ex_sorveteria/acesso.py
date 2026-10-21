import sqlite3

db = sqlite3.connect(r"C:\Users\napol\Desktop\PY\sqlite\ex_sorveteria\dbSorveteria.db")
cursor = db.cursor()

cursor.execute("SELECT * FROM tbProduto")

resultado = cursor.fetchall()
print(resultado)


cursor.close()
db.close()
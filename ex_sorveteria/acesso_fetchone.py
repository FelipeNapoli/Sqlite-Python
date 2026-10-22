import sqlite3
from rich import print
from rich.panel import Panel
from rich import box

while True:
    print()
    print()
    print(Panel(
    """

    [1] [hot_pink]Buscar por nome[/]   [2] [hot_pink]Buscar por tipo[/]

    """,
        title = "[white]BUSCA [black]MILK[/] MOO[/]",
        border_style = "hot_pink",
        box = box.ROUNDED,
        width = 55,
        subtitle = "Pressione 0 para sair",
        subtitle_align = "right"
        )
    )

    resp = int(input())

    try:
        with sqlite3.connect(r"C:\Users\napol\Desktop\PY\sqlite\ex_sorveteria\dbSorveteria.db") as db:
            db.row_factory = sqlite3.Row
            cursor = db.cursor()

            match resp:
                case 1:
                    print("\n[hot_pink]Digite o nome do produto:")
                    busca = input()
                    cursor.execute("SELECT * FROM tbProduto WHERE nome LIKE ?", (f"%{busca}%",))

                case 2:
                    print("\n[hot_pink]Digite o tipo do produto:[/]")
                    busca = input()
                    cursor.execute("SELECT * FROM tbProduto WHERE tipo LIKE ?", (f"%{busca}%",))

            total = 0
            for total, item in enumerate(cursor, start = 1):
                print(f"\nO Produto [black]{item['nome']}[/] custa R${item['valor_uni']:.2f}")

            print(f"\nSua busca obteve {total} resultado(s)")

    except sqlite3.Error as erro:
        print(f"Falha no banco: {erro}")

    except Exception as erro:
        print(f"Ocorreu um problema no programa: {erro}")
    


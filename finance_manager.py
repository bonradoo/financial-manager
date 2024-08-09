import os
import pandas as pd
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout

console = Console()

DATA_DIR = 'data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Initialize global variables
selected_account = None
selected_envelope = None
selected_year = pd.Timestamp.now().year
selected_month = pd.Timestamp.now().month_name()
selected_currency = "USD"
transactions = []

def list_files():
    return [f for f in os.listdir(DATA_DIR) if os.path.isfile(os.path.join(DATA_DIR, f))]

def get_or_create_account():
    global selected_account
    files = list_files()
    if files:
        console.print("Select an account:")
        for i, file in enumerate(files):
            console.print(f"{i + 1}. {file}")
        choice = Prompt.ask("Enter the number of the account", choices=[str(i + 1) for i in range(len(files))])
        selected_account = files[int(choice) - 1]
    else:
        selected_account = Prompt.ask("Enter new account name")

def select_year():
    global selected_year
    selected_year = int(Prompt.ask("Enter the year", default=str(pd.Timestamp.now().year)))

def select_month():
    global selected_month
    months = {
        "1": "January", "2": "February", "3": "March", "4": "April",
        "5": "May", "6": "June", "7": "July", "8": "August",
        "9": "September", "10": "October", "11": "November", "12": "December"
    }
    console.print("Select a month:")
    for num, name in months.items():
        console.print(f"{num}. {name}")
    choice = Prompt.ask("Enter the number of the month", choices=list(months.keys()))
    selected_month = months[choice]

def select_currency():
    global selected_currency
    selected_currency = Prompt.ask("Enter the currency", default="USD")

def add_transaction():
    payee = Prompt.ask("Enter the payee")
    title = Prompt.ask("Enter the title", default="None")
    category = Prompt.ask("Enter the category", default="None")
    tags = Prompt.ask("Enter the tags (comma separated)", default="None")
    amount = float(Prompt.ask("Enter the amount"))
    transaction = {
        "Payee": payee,
        "Title": title if title != "None" else None,
        "Category": category if category != "None" else None,
        "Tags": tags.split(",") if tags != "None" else None,
        "Amount": amount
    }
    transactions.append(transaction)
    return transaction

def display_header():
    header = f"[bold]Finance Manager[/bold] | Account: {selected_account} | Envelope: {selected_envelope} | Year: {selected_year} | Month: {selected_month} | Currency: {selected_currency}"
    console.print(Panel(header, style="bold cyan"), justify="center")

def display_body():
    if not transactions:
        console.print("No transactions added yet.", style="bold yellow")
    else:
        table = Table(title="Transactions")
        table.add_column("Payee")
        table.add_column("Title")
        table.add_column("Category")
        table.add_column("Tags")
        table.add_column("Amount", justify="right")
        for txn in transactions:
            tags = ", ".join(txn["Tags"]) if txn["Tags"] else ""
            table.add_row(txn["Payee"], txn["Title"] or "", txn["Category"] or "", tags, f"{txn['Amount']}")
        console.print(table)

def display_footer():
    footer_text = """
    Available commands:
    - addtr  : Add new transaction
    - chacc  : Change account
    - chenv  : Change envelope
    - chcur  : Change currency
    - chyear : Change year
    - chmont : Change month
    - editr  : Edit transaction
    - summ   : Summary for this month
    """
    console.print(Panel(footer_text, style="bold green"))

def main():
    console.clear()
    global selected_account, selected_year, selected_month, selected_currency, transactions

    get_or_create_account()
    select_year()
    select_month()
    select_currency()

    while True:
        console.clear()
        display_header()
        display_body()
        display_footer()

        command = Prompt.ask("Enter command")

        if command == "addtr":
            transaction = add_transaction()
            console.print(f"Added transaction: {transaction}")
        elif command == "chacc":
            get_or_create_account()
        elif command == "chenv":
            selected_envelope = Prompt.ask("Enter the envelope", default="None")
        elif command == "chcur":
            select_currency()
        elif command == "chyear":
            select_year()
        elif command == "chmont":
            select_month()
        elif command == "editr":
            console.print("Edit transaction functionality not implemented yet.", style="bold red")
        elif command == "summ":
            console.print("Summary functionality not implemented yet.", style="bold red")
        else:
            console.print(f"Unknown command: {command}", style="bold red")

        # Save transactions to CSV
        file_name = f"{selected_month.lower()}_{selected_year}.csv"
        file_path = os.path.join(DATA_DIR, file_name)
        df = pd.DataFrame(transactions)
        if os.path.exists(file_path):
            df_existing = pd.read_csv(file_path)
            df = pd.concat([df_existing, df], ignore_index=True)
        df.to_csv(file_path, index=False)

if __name__ == "__main__":
    main()

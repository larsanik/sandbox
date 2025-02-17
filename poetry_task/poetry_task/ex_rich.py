# это работает

from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Пример таблицы")
table.add_column("Имя", style="cyan", no_wrap=True)
table.add_column("Фамилия", style="magenta")
table.add_column("Возраст", justify="right", style="green")

table.add_row("Анна", "Иванова", "25")
table.add_row("Сергей", "Петров", "30")

console.print(table)
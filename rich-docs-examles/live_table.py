from rich.live import Live
from rich.table import Table
import time

table = Table(title="Live Data")
table.add_column("Time", style="cyan")
table.add_column("Status", style="green")

with Live(table, refresh_per_second=2) as live:
    for i in range(5):
        table.add_row(time.strftime("%H:%M:%S"), "Running")
        live.update(table)
        time.sleep(1)   

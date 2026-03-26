import time
import psutil
from rich.console import Console
from rich.live import Live
from rich.table import Table

console = Console()

def generate_cpu_load_table():
    # Create a table for displaying CPU load
    table = Table(title="CPU Load")

    table.add_column("CPU Core", justify="center", style="cyan")
    table.add_column("Load (%)", justify="center", style="magenta")

    # Get the percentage load for each CPU core
    cpu_loads = psutil.cpu_percent(percpu=True)

    for i, load in enumerate(cpu_loads):
        table.add_row(str(i), f"{load}%")

    return table

def main():
    with Live(generate_cpu_load_table(), refresh_per_second=1) as live:
        while True:
            # Update the live display table
            live.update(generate_cpu_load_table())
            time.sleep(1)  # Update every second

if __name__ == "__main__":
    main()


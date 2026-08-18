from pathlib import Path
import csv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
CSV_CLIENTS_FILE = DATA_DIR / "clients.csv"


def ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def export_clients_csv(clients):
    ensure_data_dir()
    fieldnames = ['name', 'number', 'status']
    with CSV_CLIENTS_FILE.open('w', newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(clients)



















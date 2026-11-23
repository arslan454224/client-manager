from pathlib import Path
import csv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
CSV_CLIENTS_FILE = DATA_DIR / "clients.csv"
CSV_APPLICATIONS_FILE = DATA_DIR / "applications.csv"


def ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def export_clients_csv(clients):
    ensure_data_dir()
    fieldnames = ['id','name', 'number', 'status']
    with CSV_CLIENTS_FILE.open('w', newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(clients)

def export_applications_csv(applications):
    ensure_data_dir()
    fieldnames = ['id', 'client_number', 'description']
    with CSV_APPLICATIONS_FILE.open('w', newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(applications)



















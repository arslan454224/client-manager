from pathlib import Path
import json
import csv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
CLIENTS_FILE = DATA_DIR / "clients.json"
APPLICATIONS_FILE = DATA_DIR / "applications.json"
CSV_CLIENTS_FILE = DATA_DIR / "clients.csv"


def ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def save_clients(clients):
    ensure_data_dir()

    with CLIENTS_FILE.open("w", encoding="utf-8") as file:
        json.dump(clients, file, ensure_ascii=False, indent=4)


def load_clients():
    if not CLIENTS_FILE.exists():
        return []

    try:
        with CLIENTS_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError as error:
        raise RuntimeError("Файл clients.json повреждён") from error

def export_clients_csv(clients):
    ensure_data_dir()
    fieldnames = ['name', 'number', 'status']
    with CSV_CLIENTS_FILE.open('w', newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(clients)

def save_applications(applications):
    ensure_data_dir()

    with APPLICATIONS_FILE.open('w', encoding='utf-8') as file:
        json.dump(applications, file, ensure_ascii=False, indent=4)

def load_applications():
    if not APPLICATIONS_FILE.exists():
        return []

    try:
        with APPLICATIONS_FILE.open('r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError as error:
        raise RuntimeError('Файл applications.json поврежден') from error

















from pathlib import Path
import json


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
CLIENTS_FILE = DATA_DIR / "clients.json"


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












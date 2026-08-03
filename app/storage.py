from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / 'data'
CLIENTS_FILE = DATA_DIR / 'clients.json'

print(PROJECT_ROOT)
print(DATA_DIR)
print(CLIENTS_FILE)


def ensure_data_dir():
	Path(DATA_DIR).mkdir(parents=True, exist_ok=True)
	return DATA_DIR





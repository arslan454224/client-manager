from app.storage import load_clients, save_clients

clients = load_clients()
ALLOWED_STATUSES = ('new', 'in_progress', 'completed', 'cancelled')


def add_client(name, number):
    name = name.strip()

    if not name:
        raise ValueError('Name cannot be empty')

    number = number.strip()

    if not number:
        raise ValueError('Number cannot be empty')

    for existing_client in clients:
        if existing_client['number'] == number:
            raise ValueError(f'клиент с таким номером {number}, уже был добавлен')

    client = {
        'name': name,
        'number': number,
        'status': 'new'
    }

    clients.append(client)
    save_clients(clients)
    return client


def find_client(name):
    name = name.strip()

    if not name:
        raise ValueError('Name cannot be empty')

    for client in clients:
        if client['name'].lower() == name.lower():
            return client

    return None


def get_clients():
    return clients


def update_client_status(name, status):
    client = find_client(name)
    if status not in ALLOWED_STATUSES:
        raise ValueError('Неверный статус')

    status = status.strip().lower()
    if client is None:
        raise ValueError("клиент не найден")

    client['status'] = status
    save_clients(clients)
    return client


def filter_clients_by_status(status):
    status = status.strip().lower()

    if status not in ALLOWED_STATUSES:
        raise ValueError('Такой статус отсутствует')

    result = [client for client in clients if client['status'] == status]
    return result


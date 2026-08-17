from app.database import (
    add_client_to_database,
    filter_clients_by_status_from_database,
    find_client_by_name_from_database,
    find_client_by_number_from_database,
    get_clients_from_database,
    get_used_statuses_from_database,
    search_clients_in_database,
    update_client_status_in_database,
)

ALLOWED_STATUSES = ('new', 'in_progress', 'completed', 'cancelled')


def add_client(name, number):
    client_row = add_client_to_database(name, number)
    return dict(client_row)


def find_client(name):
    client_row = find_client_by_name_from_database(name)
    if client_row is None:
        return None
    return dict(client_row)


def get_clients():
    client_rows = get_clients_from_database()
    return [dict(client_row) for client_row in client_rows]


def update_client_status(name, status):
    client = find_client(name)
    status = status.strip().lower()

    if client is None:
        raise ValueError('Не найден клиент')
    if status not in ALLOWED_STATUSES:
        raise ValueError('Неверный статус')

    client_number = client['number']
    client_row = update_client_status_in_database(client_number, status)
    return dict(client_row)


def filter_clients_by_status(status):
    client_rows = filter_clients_by_status_from_database(status)
    return [dict(client_row) for client_row in client_rows]


def get_used_statuses():
    status_rows = get_used_statuses_from_database()
    result = {status_row['status'] for status_row in status_rows}
    return result


def get_clients_name_by_number():
    clients_from_database = get_clients()

    clients_names = {client['number']: client['name'] for client in clients_from_database}
    return clients_names


def search_clients(query):
    client_rows = search_clients_in_database(query)
    result = [dict(client_row) for client_row in client_rows]
    return result


def find_client_by_number(number):
    found_client = find_client_by_number_from_database(number)
    if found_client is None:
        return None
    return dict(found_client)
import sqlite3
from multiprocessing import connection
from pathlib import Path

ALLOWED_STATUSES = ('new', 'in_progress', 'completed', 'cancelled')
ALLOWED_APPLICATION_STATUSES = ('new', 'in_progress', 'completed', 'cancelled')


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / 'data'
DATABASE_FILE = DATA_DIR / 'crm.db'

def get_connection():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_FILE)
    connection.execute('PRAGMA foreign_keys = ON')
    connection.row_factory = sqlite3.Row

    return connection


def init_database():
    connection = get_connection()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            number TEXT NOT NULL UNIQUE,
            status TEXT NOT NULL DEFAULT 'new'
        )
        """
    )

    connection.execute(
        '''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'new',
            FOREIGN KEY (client_id) REFERENCES clients(id)
        )'''
    )

    connection.commit()
    connection.close()


def add_client_to_database(name, number):
    name, number = name.strip(), number.strip()

    if not name or not number:
        raise ValueError('Данные не могут быть пустыми')

    connection = get_connection()

    try:
        connection.execute(
            '''INSERT INTO clients (name, number) VALUES (?, ?)''',
            (name, number )
        )
        connection.commit()
    except sqlite3.IntegrityError as test_error:
        raise ValueError('Клиент с таик номер уже добавлен') from test_error
    finally:
        connection.close()


def get_clients_from_database():
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            SELECT id, name, number, status
            FROM clients
            """
        )
        clients_all = cursor.fetchall()
    finally:
        connection.close()

    return clients_all


def find_client_by_number_from_database(number):
    number = number.strip()
    if not number:
        raise ValueError('Номер не найден')

    connection = get_connection()

    try:
        cursor = connection.execute(
            '''
            SELECT id, name, number, status
            FROM clients
            WHERE number = ?
            ''', (number,)
        )


        client_found = cursor.fetchone()
    finally:
        connection.close()

    return client_found


def update_client_status_in_database(number, status):
    number, status = number.strip(), status.strip().lower()

    if not number or not status:
        raise ValueError('Ошибка')
    if status not in ALLOWED_STATUSES:
        raise ValueError('Неверный статус')

    connection = get_connection()

    try:
        cursor = connection.execute(
            '''
            UPDATE clients
            SET status = ?
            WHERE number = ?
            ''', (status, number)
        )

        if cursor.rowcount == 0:
            raise ValueError('Клиент с таким номером не найден')
        connection.commit()
    finally:
        connection.close()

    return find_client_by_number_from_database(number)


def delete_client_from_database(number):
    number = number.strip()
    if not number:
        raise ValueError('Номер пустой')

    found_number = find_client_by_number_from_database(number)
    if found_number is None:
        raise ValueError('Такой номер телефона не найден')

    connection = get_connection()
    try:
        connection.execute(
            '''
            DELETE FROM clients
            WHERE number = ?''', (number,)
        )
        connection.commit()
    except sqlite3.IntegrityError as error:
        connection.rollback()
        raise ValueError(
            'Нельзя удалить клиента: у него есть заявки'
        ) from error
    finally:
        connection.close()

    return found_number


def search_clients_in_database(query):
    query = query.strip()
    if not query:
        raise ValueError('Данные не могут быть пустыми')

    search_client = f'%{query}%'

    connection = get_connection()
    try:
        cursor = connection.execute(
            '''
            SELECT id, name, number, status 
            FROM clients
            WHERE id LIKE ? OR name LIKE ? OR number LIKE ? OR status LIKE ?
            '''
            , (search_client ,search_client, search_client, search_client)
        )
        client_found = cursor.fetchall()
    finally:
        connection.close()

    return client_found


def get_clients_sorted_by_name(descending=False):
    connection = get_connection()

    try:
        if not descending:
            cursor = connection.execute(
                '''
                SELECT id, name, number, status
                FROM clients
                ORDER BY name ASC'''
            )
        else:
            cursor = connection.execute(
                '''
                SELECT id, name, number, status
                FROM clients
                ORDER BY name DESC'''
            )
        found_clients = cursor.fetchall()
    finally:
        connection.close()
    return found_clients


def count_clients_in_database():
    connection = get_connection()
    try:
        cursor = connection.execute(
            '''
            SELECT COUNT(*) AS total
            FROM clients'''
        )
        count_row = cursor.fetchone()
    finally:
        connection.close()
    return count_row['total']


def add_application_to_database(client_number, description):
    client_number, description = client_number.strip(), description.strip()

    if not client_number or not description:
        raise ValueError('Данные не могут быть пустыми')

    client = find_client_by_number_from_database(client_number)
    if client is None:
        raise ValueError('Клиент не найден')

    client_id = client['id']

    connection = get_connection()
    try:
        cursor = connection.execute(
            '''
            INSERT INTO applications (client_id, description)
            VALUES (?, ?)''', (client_id, description)
        )
        application_id = cursor.lastrowid
        connection.commit()
    finally:
        connection.close()

    return application_id


def get_applications_from_database():
    connection = get_connection()
    try:
        cursor = connection.execute(
            '''
            SELECT
                applications.id AS application_id,
                applications.description,
                applications.status,
                clients.name AS client_name,
                clients.number AS client_number
            FROM applications
            JOIN clients
                ON applications.client_id = clients.id
            ORDER BY applications.id ASC'''
        )
        applications_all = cursor.fetchall()
    finally:
        connection.close()

    return applications_all


def find_application_by_id_from_database(application_id):

    if application_id <= 0:
        raise ValueError('Ошибка')

    connection = get_connection()
    try:
        cursor = connection.execute(
            '''
            SELECT applications.id AS application_id,
            applications.description,
            applications.status,
            clients.name AS client_name,
            clients.number AS client_number
            FROM applications
            JOIN clients
                ON applications.client_id = clients.id
            WHERE applications.id = ?''', (application_id,)
        )
        got_application = cursor.fetchone()
    finally:
        connection.close()

    return got_application


def update_application_status_in_database(application_id, status):
    if application_id <= 0:
        raise ValueError('ID не может быть меньше 0')

    status = status.strip().lower()
    if not status:
        raise ValueError('Не нашел статус')
    if status not in ALLOWED_APPLICATION_STATUSES:
        raise ValueError('Такого статуса нет в списке')
    connection = get_connection()
    try:
        cursor = connection.execute(
            '''
             UPDATE applications
             SET status = ?
             WHERE id = ?''', (status, application_id)
        )
        if cursor.rowcount == 0:
            raise ValueError('Заявка не найдена')
        connection.commit()
    finally:
        connection.close()

    return find_application_by_id_from_database(application_id)


def delete_application_from_database(application_id):
    if application_id <= 0:
        raise ValueError('Такого id нет')

    application = find_application_by_id_from_database(application_id)
    if application is None:
        raise ValueError('Такой заявки не существует')

    connection = get_connection()
    try:
        connection.execute(
            '''
            DELETE FROM applications
            WHERE id = ?''', (application_id,)
        )
        connection.commit()
    finally:
        connection.close()

    return application

if __name__ == '__main__':
    init_database()
    print('База данных инициализирована')
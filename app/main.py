from app.clients import add_client, get_clients, update_client_status, filter_clients_by_status
from app.clients import search_clients
from app.storage import export_clients_csv
from app.applications import add_application, get_applications, find_application_by_id, update_application_status, filter_applications_by_status, delete_application
from app.database import init_database

def show_menu():
    print('\nВыбери 1, чтобы добавить клиента')
    print('Выбери 2, чтобы найти клиента')
    print('Выбери 3, чтобы показать всех клиентов')
    print('Выбери 4, чтобы изменить статус клиента')
    print('Выбери 5, чтобы экспортировать клиентов в CSV')
    print('Выбери 6, чтобы отфильтровать клиентов по статусу')
    print('Выбери 7, чтобы добавить заявку')
    print('Выбери 8, чтобы показать все заявки')
    print('Выбери 9, чтобы найти заявку по ID')
    print('Выбери 10, чтобы изменить статус заявки')
    print('Выбери 11, чтобы отфильтровать заявки по статусу')
    print('Выбери 12, чтобы удалить заявку')
    print('Выбери 0, чтобы выйти')


def handle_add_client():
    name = input('Введите имя: ').strip()
    number = input('Введите номер: ').strip()

    try:
        client = add_client(name, number)
    except ValueError as error:
        print(error)
    else:
        print(f'{client}, клиент успешно добавлен, его номер {number}')


def handle_search_clients():
    query = input('Напиши имя клиента,часть имени или номер которого хочешь найти: ').strip()
    try:
        found_clients = search_clients(query)
    except ValueError as error:
        print(error)
    else:
        if not found_clients:
            print('клиент не найден')
            return

        for client in found_clients:
            print(f'{client["name"]}, {client["number"]}, {client["status"]}')


def handle_show_clients():
    all_clients = get_clients()

    if not all_clients:
        print('пустой списко')
        return
    for client in all_clients:
        print(f'{client["name"]}, '
              f'{client["number"]}, '
              f'{client["status"]}')


def handle_update_client_status():
    name = input('введите имя:').strip()
    status = (input('введите новый статус: new, in_progress, completed, cancelled ')).strip()

    try:
        status_of_client = update_client_status(name, status)
    except ValueError as error:
        print(error)
    else:
        print(f'обновили статус {status_of_client}')


def handle_export_clients_csv():
    all_clients = get_clients()

    if not all_clients:
        print('Пустой список')
        return

    export_clients_csv(all_clients)
    print('Клиенты экспортированы в CSV')


def handle_filter_clients_by_status():
    client_status = input("Введите ваш статут: 'new', 'in_progress', 'completed', 'cancelled' ")

    try:
        filtered_clients = filter_clients_by_status(client_status)
    except ValueError as error:
        print(error)
    else:
        if not filtered_clients:
            print('Пустой список')
            return
        for client in filtered_clients:
            print(client['name'], client['status'])


def handle_add_application():
    client_number = input('Введите номер клиента: ').strip()
    description_application = input('Введите заявку: ').strip()

    try:
        new_application = add_application(client_number, description_application)
    except ValueError as error:
        print(error)
    else:
        print(f'{new_application}, заявка клиента')


def handle_show_applications():
    all_applications = get_applications()
    if not all_applications:
        print('Пусто, нет заявок')
        return

    for application in all_applications:
        print(f'{application["id"]}, '
              f'{application["client_number"]}, '
              f'{application["description"]}, '
              f' {application["status"]}')


def handle_find_application_by_id():
    user_input_id = input('Введите id: ')

    try:
        user_input_id = int(user_input_id)
    except ValueError:
        print(f'{user_input_id}, не число, напишите правильное id')
        return

    found_application = find_application_by_id(user_input_id)

    if found_application is None:
        print('id не найдено')
        return

    print(f'{found_application["description"]}, ')


def handle_update_application_status():
    user_input_id = input('Введите id заявки: ')
    try:
        user_input_id = int(user_input_id)
    except ValueError:
        print('введите правильное id')
        return

    found_application = find_application_by_id(user_input_id)
    if found_application is None:
        print('Нету такого id')
        return

    new_status = input('введите новый статус: new, in_progress, completed, cancelled ')

    try:
        application_new_status = update_application_status(user_input_id, new_status)
    except ValueError as error:
        print(error)
    else:
        print(application_new_status)


def handle_filter_applications_by_status():
    user_status = input('Введите ваш статус: new, in_progress, completed, cancelled ')
    try:
        filtered_status = filter_applications_by_status(user_status)
    except ValueError as error:
        print(error)
    else:
        if not filtered_status:
            print('Заявок с таким статусом не найдено')
            return
        for application in filtered_status:
            print(application)


def handle_delete_application():
    user_input = input('Введите id заявки: ')
    try:
        user_input_id = int(user_input)
    except ValueError:
        print('Не правильно введен id')
        return

    try:
        deleted_application = delete_application(user_input_id)
    except ValueError as error:
        print(error)
    else:
        print(deleted_application)

COMMAND_HANDLERS = {
    '1': handle_add_client,
    '2': handle_search_clients,
    '3': handle_show_clients,
    '4': handle_update_client_status,
    '5': handle_export_clients_csv,
    '6': handle_filter_clients_by_status,
    '7': handle_add_application,
    '8': handle_show_applications,
    '9': handle_find_application_by_id,
    '10': handle_update_application_status,
    '11': handle_filter_applications_by_status,
    '12': handle_delete_application
}


def main():
    init_database()
    while True:
        show_menu()

        choice = input().strip()
        if choice == '0':
            break

        handler = COMMAND_HANDLERS.get(choice)

        if handler is None:
            print('Неверная команда')
            continue

        handler()

if __name__ == '__main__':
    main()
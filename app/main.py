from app.clients import add_client, get_clients, update_client_status, filter_clients_by_status
from app.clients import search_clients
from app.storage import export_clients_csv
from app.applications import add_application, get_applications, find_application_by_id, update_application_status, filter_applications_by_status, delete_application


def main():
    while True:
        print(f'\nвыбери 1 для того, чтобы добавить клиента')
        print(f'выбери 2 для того, чтобы показать клиента')
        print(f'выбери 3, чтобы показать всех клиентов')
        print(f'выбери 4 для изменения статуса')
        print(f'выбери 5, для експорта клиентов в CSV')
        print(f'выбери 6 для фильтрации клиента по статусу')
        print(f'выбери 7 для добавления заявки')
        print(f'выбери 8, чтобы показать все заявки')
        print(f'выбери 9, чтобы найти заявку по id')
        print(f'выбери 10, чтобы изменить статус заявки')
        print(f'выбери 11 для фильтрации статуса заявки')
        print(f'выбери 12 для удаления заявки')
        print(f'выбери 0, чтобы выйти')

        choice = (input()).strip()

        if choice == '1':
            name = input('Введите имя: ').strip()
            number = (input('Введите номер: ').strip())

            try:
                client = add_client(name, number)
                print(f'{client}, клиент успешно добавлен, его номер {number}')
            except ValueError as error:
                print(error)

        elif choice == '2':
            query = input('Напиши имя клиента,часть имени или номер которого хочешь найти: ').strip()
            try:
                found_clients = search_clients(query)
            except ValueError as error:
                print(error)
            else:
                if not found_clients:
                    print('клиент не найден')
                    continue

                for client in found_clients:
                    print(f'{client["name"]}, {client["number"]}, {client["status"]}')

        elif choice == '3':
            all_clients = get_clients()

            if not all_clients:
                print(f'пустой списко')
                continue
            for client in all_clients:
                print(f'{client["name"]}, '
                      f'{client["number"]}, '
                      f'{client["status"]}')

        elif choice == '4':
            name = input('введите имя:').strip()
            status = (input('введите новый статус: new, in_progress, completed, cancelled ')).strip()

            try:
                status_of_client = update_client_status(name, status)
            except ValueError as error:
                print(error)
            else:
                print(f'обновили статус {status_of_client}')

        elif choice == '5':
            all_clients = get_clients()

            if not all_clients:
                print('Пустой список')
                continue

            export_clients_csv(all_clients)
            print('Клиенты экспортированы в CSV')

        elif choice == '6':
            client_status = input("Введите ваш статут: 'new', 'in_progress', 'completed', 'cancelled' ")

            try:
                filtered_clients = filter_clients_by_status(client_status)
            except ValueError as error:
                print(error)
            else:
                if not filtered_clients:
                    print('Пустой список')
                    continue
                for client in filtered_clients:
                    print(client['name'], client['status'])

        elif choice == '7':
            client_number = input('Введите номер клиента: ').strip()
            description_application = input('Введите заявку: ').strip()

            try:
                new_application = add_application(client_number, description_application)
            except ValueError as error:
                print(error)
            else:
                print(f'{new_application}, заявка клиента')

        elif choice == '8':
            all_applications = get_applications()
            if not all_applications:
                print('Пусто, нет заявок')
                continue

            for application in all_applications:
                print(f'{application["id"]}, '
                      f'{application["client_number"]}, '
                      f'{application["description"]}, '
                      f' {application["status"]}')

        elif choice == '9':
            user_input_id = input('Введите id: ')

            try:
                user_input_id = int(user_input_id)
            except ValueError:
                print(f'{user_input_id}, не число, напишите правильное id')
                continue

            found_application = find_application_by_id(user_input_id)

            if found_application is None:
                print('id не найдено')
                continue

            print(f'{found_application["description"]}, ')

        elif choice == '10':
            user_input_id = input('Введите id заявки: ')
            try:
                user_input_id = int(user_input_id)
            except ValueError:
                print('введите правильное id')
                continue

            found_application = find_application_by_id(user_input_id)
            if found_application is None:
                print('Нету такого id')
                continue

            new_status = input('введите новый статус: new, in_progress, completed, cancelled ')

            try:
                application_new_status = update_application_status(user_input_id, new_status)
            except ValueError as error:
                print(error)
            else:
                print(application_new_status)

        elif choice == '11':
            user_status = input('Введите ваш статус: new, in_progress, completed, cancelled ')
            try:
                filtered_status = filter_applications_by_status(user_status)
            except ValueError as error:
                print(error)
            else:
                if not filtered_status:
                    print('Заявок с таким статусом не найдено')
                    continue
                for application in filtered_status:
                    print(application)

        elif choice == '12':
            user_input = input('Введите id заявки: ')
            try:
                user_input_id = int(user_input)
            except ValueError:
                print('Не правильно введен id')
                continue

            try:
                deleted_application = delete_application(user_input_id)
            except ValueError as error:
                print(error)
            else:
                print(deleted_application)


        elif choice == '0':
            print('Программа завершилась')
            break

        else:
            print('Неизвестная программа')


if __name__ == '__main__':
    main()

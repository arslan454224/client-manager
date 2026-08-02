from app.clients import add_client, find_client, get_client


def main():
	while True:
		print(f'\nвыбери 1 для того, чтобы добавить клиента')
		print(f'выбери 2 для того, чтобы показать клиента')
		print(f'выбери 3, чтобы показать всех клиентов')
		print(f'выебир 0, чтобы выйти')

		choice = (input()).strip()

		if choice == '1':
			name = input('Введите имя: ').strip()
			number = (input('Введите номер: ').strip())

			client = add_client(name, number)
			print(f'{client}, клиент успешно добавлен, его номер {number}')

		elif choice == '2':
			name = input('Напиши имя клиента, которого хочешь найти: ')
			client_show = find_client(name)

			if client_show is None:
				print('Клиент не найден')
			else:
				print(f'клиент найден {client_show}')

		elif choice == '3':
			all_clients = get_client()

			if not all_clients:
				print(f'пустой списко')
			else:
				for client in all_clients:
					print(
						f'{client['name']}'
					    f'{client["number"]}'
					    f'{client["status"]}'
					)

		elif choice == '0':
			print('Программа завершилась')
			break

		else:
			print('Неизвестная программа')

if __name__ == '__main__':
	main()

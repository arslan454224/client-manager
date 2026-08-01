from app.clients import add_client

def main():
	while True:
		print(f'\nвыбери 1 для того, чтобы добавить клиента')
		print(f'выебир 0, чтобы выйти')

		choice = (input()).strip()

		if choice == '1':
			name = input('Введите имя: ').strip()
			number = (input('Введите номер: ').strip())

			client = add_client(name, number)
			print(f'{client}, клиент успешно добавлен, его номер {number}')

		elif choice == '0':
			print('Программа завершилась')
			break

		else:
			print('Неизвестная программа')

if __name__ == '__main__':
	main()

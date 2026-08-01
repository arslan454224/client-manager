from app.clients import add_client

def main():
	name = input("Enter your name: ")
	number = input("Enter your number: ")


	client = add_client(name, number)
	print(f'{client}, успешно добавлен, его номер {number}')

	return client



if __name__ == '__main__':
	main()
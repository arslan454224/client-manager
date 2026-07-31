from app.clients import add_client

def main():
	name = input("Enter your name: ")
	client = add_client(name)
	print(f'клиент: {client}, успешно добавлен ')
	return client

if __name__ == '__main__':
	main()
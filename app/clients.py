clients = []

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
	return  clients







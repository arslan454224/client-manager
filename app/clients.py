clients = []

def add_client(name, number):
	name = name.strip()

	if not name:
		raise ValueError('Name cannot be empty')

	number = number.strip()

	if not number:
		raise ValueError('Number cannot be empty')

	client = {
		'name': name,
		'number': number,
		'status': 'new'
	}


	clients.append(client)
	return client






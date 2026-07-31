clients = []

def add_client(name):
	name = name.strip()

	if not name:
		raise ValueError('Name cannot be empty')

	clients.append(name)
	return name


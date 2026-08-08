from app.clients import find_client_by_number

applications = []
ALLOWED_APPLICATION_STATUSES = ('new', 'in_progress', 'completed', 'cancelled')

def add_application(client_number, description):
    client_number = client_number.strip()
    description = description.strip()

    client = find_client_by_number(client_number)
    if client is None:
        raise ValueError('Клиент не найден')

    if not description:
        raise ValueError('Нету описания ')

    application_id = len(applications) + 1

    new_application = {
        'id': application_id,
        'client_number': client_number,
        'description': description,
        'status': 'new'
    }

    applications.append(new_application)
    return new_application


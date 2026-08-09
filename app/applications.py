from app.clients import find_client_by_number
from app.storage import save_applications, load_applications

applications = load_applications()
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
    application_id = int(application_id)

    new_application = {
        'id': application_id,
        'client_number': client_number,
        'description': description,
        'status': 'new'
    }

    applications.append(new_application)
    save_applications(applications)
    return new_application

def get_applications():
    return applications

def find_application_by_id(application_id):

    for application in applications:
        if application['id'] == application_id:
            return application

    return None

def update_application_status(application_id, status):
    application = find_application_by_id(application_id)
    if application is None:
        raise ValueError('Неправильный статус')

    status = status.strip().lower()
    if status not in ALLOWED_APPLICATION_STATUSES:
        raise ValueError('Нету такого статуса')

    application['status'] = status
    save_applications(applications)
    return application


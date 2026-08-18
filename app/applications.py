from app.database import (
    add_application_to_database,
    find_application_by_id_from_database,
    get_applications_from_database,
    update_application_status_in_database,
    filter_applications_by_status_from_database,
    delete_application_from_database
)

def add_application(client_number, description):
    client_number = client_number.strip()
    description = description.strip()

    got_applications = add_application_to_database(client_number, description)
    find_applications = find_application_by_id_from_database(got_applications)
    return dict(find_applications)


def get_applications():
    rows = get_applications_from_database()
    result = [dict(row) for row in rows]
    return result


def find_application_by_id(application_id):
    application_row = find_application_by_id_from_database(application_id)
    if application_row is None:
        return None

    return dict(application_row)


def update_application_status(application_id, status):
    application_row = update_application_status_in_database(application_id, status)
    return dict(application_row)


def filter_applications_by_status(status):
    application_rows = filter_applications_by_status_from_database(status)
    result = [dict(application_row) for application_row in application_rows]
    return result


def delete_application(application_id):
    application_row = delete_application_from_database(application_id)
    return dict(application_row)


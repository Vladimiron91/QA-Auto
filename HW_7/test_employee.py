from employee_api import EmployeeApi

BASE_URL = "http://5.101.50.27:8000"
api = EmployeeApi(BASE_URL)


def test_create_employee():
    """Проверка: создание нового сотрудника"""

    employee = {
        "first_name": "John",
        "last_name": "Doe",
        "middle_name": "Edward",
        "company_id": 1,
        "email": "johndoe@example.com",
        "phone": "+1234567890",
        "birthdate": "1990-01-15",
        "is_active": True
    }

    response = api.create_employee(employee)

    # Проверка HTTP-кода
    assert response.status_code == 200

    data = response.json()

    # Проверка, что данные совпадают
    for key, value in employee.items():
        assert data[key] == value

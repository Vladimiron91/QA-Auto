import requests


class EmployeeApi:
    """Класс-обёртка для работы с Employee API"""

    def __init__(self, base_url: str):
        self.base_url = base_url

    def create_employee(self, employee_data: dict):
        """Создание нового сотрудника"""
        return requests.post(
            f"{self.base_url}/employee/create",
            json=employee_data
        )

    def get_employees_by_company(self, company_id: int):
        """Получение списка сотрудников по ID компании"""
        return requests.get(
            f"{self.base_url}/employee/list/{company_id}"
        )

    def update_employee(self, employee_id: int, update_data: dict, token: str):
        """Изменение данных сотрудника"""
        return requests.patch(
            f"{self.base_url}/employee/change/{employee_id}",
            params={"client_token": token},
            json=update_data
        )

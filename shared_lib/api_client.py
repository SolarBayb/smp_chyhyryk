import requests
import logging

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)  # Встановлення рівня логування

        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get(self, path, params=None):
        """Виконує GET-запит до API."""
        try:
            self.logger.info(f"Виконання GET-запиту до {self.base_url}{path} з параметрами {params}")
            response = requests.get(self.base_url + path, params=params)
            response.raise_for_status()
            self.logger.info(f"Отримано відповідь: {response.json()}")
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Помилка при виконанні запиту: {e}")
            return f"Помилка при виконанні запиту: {e}"

    def post(self, path, data=None):
        """Виконує POST-запит до API."""
        try:
            self.logger.info(f"Виконання POST-запиту до {self.base_url}{path} з даними {data}")
            response = requests.post(self.base_url + path, json=data)
            response.raise_for_status()
            self.logger.info(f"Отримано відповідь: {response.json()}")
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Помилка при виконанні запиту: {e}")
            return f"Помилка при виконанні запиту: {e}"

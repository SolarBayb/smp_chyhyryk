import requests

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com/posts"

    @staticmethod
    def get_posts():
        """Retrieve posts from the API."""
        try:
            response = requests.get(APIClient.BASE_URL)
            response.raise_for_status()  # Raises an error for response codes 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            return f"Error during request: {e}"

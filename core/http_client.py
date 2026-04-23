import httpx
from core.logger import get_logger
from config.config import config


class HttpClient:
    def __init__(self):
        # Инициализируем логгер с именем класса
        self.logger = get_logger(self.__class__.__name__)

        # Создаем сессию httpx
        self.client = httpx.Client(
            base_url=config.BASE_URL,
            timeout=config.TIMEOUT,
            headers={"Content-Type": "application/json"}
        )

    def _send_request(self, method, url, **kwargs):
        """Внутренний метод для отправки запросов и логирования"""
        self.logger.info(f"\n{method} {url}")

        try:
            response = self.client.request(method, url, **kwargs)
            self.logger.info(f"STATUS: {response.status_code}")
            return response
        except Exception as e:
            self.logger.error(f"Request failed: {e}")
            raise e

    def get(self, url, **kwargs):
        return self._send_request("GET", url, **kwargs)

    def post(self, url, **kwargs):
        return self._send_request("POST", url, **kwargs)

    def put(self, url, **kwargs):
        return self._send_request("PUT", url, **kwargs)

    def delete(self, url, **kwargs):
        return self._send_request("DELETE", url, **kwargs)

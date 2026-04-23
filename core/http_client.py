import httpx
from config.config import BASE_URL, TIMEOUT, HEADERS
from core.logger import get_logger


class HttpClient:
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)

        self.client = httpx.Client(
            base_url=BASE_URL,
            timeout=TIMEOUT,
            headers=HEADERS
        )

    def get(self, url, **kwargs):
        print()
        self.logger.info(f"GET {url}")
        response = self.client.get(url, **kwargs)
        self.logger.info(f"STATUS: {response.status_code}")
        return response

    def post(self, url, **kwargs):
        print()
        self.logger.info(f"POST {url}")
        response = self.client.post(url, **kwargs)
        self.logger.info(f"STATUS: {response.status_code}")
        return response

    def put(self, url, **kwargs):
        print()
        self.logger.info(f"PUT {url}")
        response = self.client.put(url, **kwargs)
        self.logger.info(f"STATUS: {response.status_code}")
        return response

    def delete(self, url, **kwargs):
        print()
        self.logger.info(f"DELETE {url}")
        response = self.client.delete(url, **kwargs)
        self.logger.info(f"STATUS: {response.status_code}")
        return response
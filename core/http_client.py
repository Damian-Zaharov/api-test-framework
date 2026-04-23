import httpx
from config.config import BASE_URL, TIMEOUT


class HttpClient:
    def __init__(self):
        self.client = httpx.Client(base_url=BASE_URL, timeout=TIMEOUT)

    def get(self, url, **kwargs):
        return self.client.get(url, **kwargs)

    def post(self, url, **kwargs):
        return self.client.post(url, **kwargs)

    def put(self, url, **kwargs):
        return self.client.put(url, **kwargs)

    def delete(self, url, **kwargs):
        return self.client.delete(url, **kwargs)
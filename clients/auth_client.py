from core.http_client import HttpClient

class AuthClient(HttpClient):
    def login(self, username, password):
        return self.post(
            "/auth/login",
            json={"username": username, "password": password}
        )

    def get_me(self, token: str):
        return self.get(
            "/auth/me",
            headers={"Authorization": f"Bearer {token}"}
        )

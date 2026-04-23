from core.http_client import HttpClient


class ProductsClient(HttpClient):
    def get_products(self, limit: int = 30, skip: int = 0):
        return self.get("/products", params={"limit": limit, "skip": skip})

    def get_product_by_id(self, product_id: int):
        return self.get(f"/products/{product_id}")

    def search_products(self, query: str):
        return self.get("/products/search", params={"q": query})

    def add_product(self, product_data: dict):
        return self.post("/products/add", json=product_data)

    def update_product(self, product_id: int, update_data: dict):
        return self.put(f"/products/{product_id}", json=update_data)

    def delete_product(self, product_id: int):
        return self.delete(f"/products/{product_id}")

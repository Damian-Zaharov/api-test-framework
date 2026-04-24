from clients.products_client import ProductsClient
from schemas.product_schema import ProductListResponse, Product
from utils.retry import retry
import allure


class ProductsService:
    def __init__(self):
        self.client = ProductsClient()

    @allure.step("Получение списка товаров")
    @retry()
    def get_all_products(self, limit: int = 30) -> ProductListResponse:
        """Метод для получения товаров"""
        response = self.client.get_products(limit=limit)
        response.raise_for_status()
        return ProductListResponse(**response.json())

    @allure.step("Получение одного товара по id")
    @retry()
    def get_single_product(self, product_id: int) -> Product:
        """Метод для получения одного товара"""
        response = self.client.get_product_by_id(product_id)
        response.raise_for_status()
        return Product(**response.json())

    @allure.step("Поиск товаров по названию")
    @retry()
    def search_for_product(self, query: str) -> ProductListResponse:
        """Метод для поиска"""
        response = self.client.search_products(query)
        response.raise_for_status()
        return ProductListResponse(**response.json())

    @allure.step("Создание нового товара")
    @retry()
    def create_new_product(self, payload: dict) -> Product:
        """Метод для добавления нового товара"""
        response = self.client.add_product(payload)
        response.raise_for_status()
        return Product(**response.json())

    @allure.step("Редактирование товара")
    @retry()
    def update_existing_product(self, product_id: int, payload: dict) -> Product:
        response = self.client.update_product(product_id, payload)
        response.raise_for_status()
        return Product(**response.json())

    @allure.step("Удаление товара")
    @retry()
    def remove_product(self, product_id: int):
        response = self.client.delete_product(product_id)
        response.raise_for_status()
        return response.json()

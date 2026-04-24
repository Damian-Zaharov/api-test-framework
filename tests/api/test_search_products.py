
import pytest
@pytest.mark.parametrize("query, expected_category", [
    ("iPhone", "mobile-accessories"),  # Поправили здесь
    ("Laptop", "laptops"),
    ("Mascara", "beauty")
])
def test_search_product_parametrization(products_service, query, expected_category):
    data = products_service.search_for_product(query)

    assert len(data.products) > 0, f"Ничего не найдено по запросу {query}"

    # Проверяем, что хотя бы у первого товара категория совпадает
    assert data.products[0].category == expected_category
    print(f"\n[DDT] Поиск '{query}' успешно нашел категорию '{expected_category}'")

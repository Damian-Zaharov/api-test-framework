
def test_search_product(products_service):
    query = "phone"
    data = products_service.search_for_product(query)

    # список не пуст?
    assert len(data.products) > 0, f"По запросу '{query}' ничего не найдено"

    # всё в нижний регистр (.lower()), чтобы поиск был нечувствителен к регистру
    for product in data.products:
        content = (product.title + product.description).lower()
        assert query.lower() in content, f"Товар {product.id} не соответствует поиску '{query}'"

    print(f"\n[INFO] Поиск по слову '{query}' прошел успешно. Найдено: {len(data.products)}")

def test_search_product(products_service):
    query = "111phone"
    data = products_service.search_for_product(query)

    assert data.total == 0
    assert len(data.products) == 0, f"По запросу '{query}' найдены товары"
    assert isinstance(data.products, list)

    print(f"\n[SUCCESS] Поиск корректно вернул 0 результатов для запроса: {query}")

def test_get_all_products(products_service):
    limit = 30
    data = products_service.get_all_products(limit=limit)

    # Проверяем метаданные
    assert len(data.products) == limit
    assert data.total > 0

    # Проверяем данные первого товара в списке
    first_product = data.products[0]
    assert first_product.id is not None
    assert isinstance(first_product.title, str)

    print(f"\n[INFO] Получено товаров: {len(data.products)} из {data.total}")

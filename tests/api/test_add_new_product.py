
def test_add_new_product(products_service):
    new_product_payload = {
        "title": "BMW Pencil",
        "description": "Very expensive pencil",
        "price": 999.99,
        "category": "stationery"
    }

    product = products_service.create_new_product(new_product_payload)

    # сервер вернул ID (значит товар создан)
    assert product.id is not None

    # данные созданного товара совпадают с нашими
    assert product.title == new_product_payload["title"]
    assert product.price == new_product_payload["price"]

    print(f"\n[SUCCESS] Товар создан с ID: {product.id}")

def test_update_product(products_service):
    # Тест 9: Изменяем цену товара №1
    product_id = 1
    new_data = {"price": 1.99}

    updated_product = products_service.update_existing_product(product_id, new_data)

    assert updated_product.price == 1.99
    print(f"\n[SUCCESS] Цена товара {product_id} обновлена")




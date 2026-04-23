
def test_get_single_product(products_service):
    target_id = 7
    product = products_service.get_single_product(target_id)
    assert product.id == target_id

    assert product.title is not None
    assert product.price > 0

    print(f"\n[INFO] Товар найден: {product.title} (Цена: {product.price})")

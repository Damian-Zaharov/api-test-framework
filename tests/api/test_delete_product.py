def test_delete_product(products_service):
    product_id = 1
    result = products_service.remove_product(product_id)

    assert result["isDeleted"] is True
    print(f"\n[SUCCESS] Товар {product_id} помечен как удаленный")

from services.store_service import StoreService
import allure

@allure.feature("Store API")
@allure.story("Get Product - Positive Case")
def test_get_single_product():
    request = StoreService()
    response = request.get_single_products(1)

    assert response.status_code in [200, 404]

    if response.status_code == 200:
        assert response.json()["id"] == 1

@allure.feature("Store API")
@allure.story("Get Product - Negative Case")
def test_get_single_product_fail():
    request = StoreService()
    response = request.get_single_products(9999)
    
    assert response.status_code in [400, 404]

@allure.feature("Store API")
@allure.story("Get Product - Negative Case")
def test_get_single_product_string_id():
    request = StoreService()
    response = request.get_single_products("abc")

    assert response.status_code in [400, 404]

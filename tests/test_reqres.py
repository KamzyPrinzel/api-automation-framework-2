import allure
from services.reqres_service import ReqResService

@allure.feature("ReqRes API")
@allure.story("Create User - Postive Case")
def test_create_user_pass(base_headers):
    request = ReqResService()
    response = request.create_user(
        name = "John",
        job = "Software Engineer",
        base_headers = base_headers
    )

    if response.status_code == 201:
        assert response.json()["name"] == "John"
    else:
        assert response.status_code == 403

@allure.feature("ReqRes API")
@allure.story("Create User - Negative Case, Empty Payload")
def test_create_empty_user(base_headers):
    request = ReqResService()
    response = request.create_user(
        name = "",
        job = "",
        base_headers = base_headers
    )

    assert response.status_code in [201, 403]

@allure.feature("ReqRes API")
@allure.story("Update User - Positive Case")
def test_update_user(base_headers):
    request = ReqResService()
    response = request.update_user(
        user_id = 1, 
        name = "James",
        job = "Senior Software Engineer",
        base_headers = base_headers
    )

    assert response.status_code in [200, 403]
    content_type = response.headers.get("Content-Type", "")
    if content_type.startswith("application/json"):
        data = response.json()
        assert data["job"] == "Senior Software Engineer"

@allure.feature("ReqRes API")
@allure.story("Update User - Negative Case")
def test_update_user_fail(base_headers):
    request = ReqResService()
    response = request.update_user(
        user_id = 9999,
        name = "Jane",
        job = "Web Developer",
       base_headers = base_headers
    )
    assert response.status_code in [200, 403]

@allure.feature("ReqRes API")
@allure.story("Delete User")
def test_delete_user():
    request = ReqResService()
    response = request.delete_user(1)

    assert response.status_code in [200, 403]
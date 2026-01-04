import allure
from services.post_service import PostService

@allure.feature("Store API")
@allure.story("Get Post")
def get_post():
    request = PostService()
    response = request.get_post()

    assert response.status_code == 200
    assert len(response.json()) > 0

@allure.feature("Store API")
@allure.story("Create Post - Positive")
def create_post_pass(headers):
    request = PostService()
    response = request.create_post(
        title = "Job Description", 
        body = "This is a role for Senior Software Developers with 5 years experience in Python",
        post_id = 1,
        headers = headers
    )
    
    assert response.status_code in [201, 403]
    assert response.json()["title"] == "Job Description"

@allure.feature("Store API")
@allure.story("Create Post - Negative Case")
def create_post_fail(headers):
    request = PostService()
    response = request.create_post(
        title = "", 
        body = "This is a role for Senior Software Developers with 5 years experience in Python",
        post_id = 2,
        headers = headers
    )
    
    assert response.status_code in [201, 403]
    assert response.json()["title"] == ""

@allure.feature("Store API")
@allure.story("Update Post - Positive Case")
def update_post_pass(headers):
    request = PostService()
    response = request.update_post(
        title = "Job Role",
        post_id = 1,
        headers = headers
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Job Role"

@allure.feature("Store API")
@allure.story("Update Post - Negative Case")
def update_post_pass(headers):
    request = PostService()
    response = request.update_post(
        title = "Job Vacancy",
        post_id = 99999,
        headers = headers
    )

    assert response.status_code in [200, 404]
    assert response.json()["title"] == "Job Vacancy"
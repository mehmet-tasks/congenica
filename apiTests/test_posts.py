import pytest
from apiStructure.posts_api import Posts


@pytest.fixture(scope="module")
def posts_api():
    return Posts()


def test_get_all_posts(posts_api):
    response = posts_api.get_all_posts()
    assert response.status_code == 200
    print(response.json())
    assert len(response.json()) == 100


def test_get_a_post_by_id(posts_api):
    response = posts_api.get_a_post_by_id(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"


def test_create_a_post(posts_api):
    payload = {'title': 'New Post', 'body': 'This is a new post', 'userId': 101}
    response = posts_api.create_a_post(payload)
    assert response.status_code == 201
    assert response.json()["id"] == 101


def test_update_a_post(posts_api):
    payload = {'title': 'Updated Post', 'body': 'This post has been updated', 'userId': 1}
    response = posts_api.update_a_post(1, payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Post"
    assert response.json()["body"] == "This post has been updated"
    assert response.json()["userId"] == 1


def test_partial_update_a_post(posts_api):
    payload = {'title': 'Partially Updated Post'}
    response = posts_api.partially_update_a_post(1, payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Partially Updated Post"
    assert response.json()["title"] != "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    assert response.json()[
               "body"] == "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"


def test_delete_a_post(posts_api):
    response = posts_api.delete_a_post(1)
    assert response.status_code == 200
    assert response.json() == {}


def test_negative_try_to_get_a_post_by_id_which_does_not_exist(posts_api):
    response = posts_api.get_a_post_by_id(101)
    assert response.status_code == 404
    assert response.json() == {}


def test_negative_try_to_create_a_post_with_an_improper_payload(posts_api):
    # THERE IS A BUG FOR THIS CONDITION.
    # IT SHOULD NOT ALLOW ME TO CREATE A POST WITH AN IMPROPER PAYLOAD, BUT IT RETURNS 201 INSTEAD OF 404.
    # FOR THAT REASON THIS TEST CASE IS FAILING.
    payload = {'unavailableVariable': 'N/A'}
    response = posts_api.create_a_post(payload)
    assert response.status_code == 404


def test_negative_try_to_update_a_nonexistent_post(posts_api):
    # THERE IS A BUG FOR THIS CONDITION.
    # NORMALLY IT SHOULD RETURN 404(NOT FOUND), BUT IT'S RETURNING 500 INTERNAL SERVER ERROR WHICH IS NOT CORRECT.
    # FOR THAT REASON THIS TEST CASE IS FAILING.
    payload = {'title': 'Updated Post', 'body': 'This post has been updated', 'userId': 101}
    response = posts_api.update_a_post(101, payload)
    assert response.status_code == 404


def test_negative_try_to_partially_update_a_nonexistent_post(posts_api):
    # THERE IS A BUG FOR THIS CONDITION.
    # NORMALLY IT SHOULD RETURN 404(NOT FOUND), BUT IT'S RETURNING 200 WHICH IS NOT CORRECT.
    # FOR THAT REASON THIS TEST CASE IS FAILING.
    payload = {'title': 'Partially Updated Post'}
    response = posts_api.partially_update_a_post(101, payload)
    assert response.status_code == 404

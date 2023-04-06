import pytest
from apiStructure.comments_api import Comments


@pytest.fixture(scope="module")
def comments_api():
    return Comments()


def test_get_all_comments(comments_api):
    response = comments_api.get_all_comments()
    assert response.status_code == 200
    assert len(response.json()) == 500


def test_get_a_specific_comment(comments_api):
    response = comments_api.get_a_comment_by_id(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["email"] == "Eliseo@gardner.biz"
    assert response.json()["postId"] == 1


def test_create_a_comment(comments_api):
    payload = {'postId': 501, 'id': 501, 'name': 'Comment User', 'email': 'commentuser@gmail.com',
               'body': 'New Comment'}
    response = comments_api.create_a_comment(payload)
    assert response.status_code == 201
    assert response.json()["id"] == 501
    assert response.json()["postId"] == 501
    assert response.json()["name"] == "Comment User"
    assert response.json()["email"] == "commentuser@gmail.com"
    assert response.json()["body"] == "New Comment"


def test_update_a_comment(comments_api):
    payload = {'postId': 1, 'id': 1, 'name': 'Updated User', 'email': 'updatedEmail@gmail.com',
               'body': 'Updated comment body'}
    response = comments_api.update_a_comment(1, payload)
    assert response.status_code == 200
    assert response.json()["postId"] == 1
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Updated User"
    assert response.json()["email"] == "updatedEmail@gmail.com"
    assert response.json()["body"] == "Updated comment body"


def test_partially_update_a_comment(comments_api):
    payload = {'name': 'Updated User'}
    response = comments_api.partially_update_a_comment(1, payload)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Updated User"
    assert response.json()["email"] == "Eliseo@gardner.biz"


def test_delete_a_comment(comments_api):
    response = comments_api.delete_a_comment(1)
    assert response.status_code == 200
    assert response.json() == {}


def test_negative_try_to_get_a_comment_by_id_which_does_not_exist(comments_api):
    response = comments_api.get_a_comment_by_id(501)
    assert response.status_code == 404
    assert response.json() == {}


def test_negative_try_to_create_a_comment_with_an_improper_payload(comments_api):
    # THERE IS A BUG FOR THIS CONDITION.
    # IT SHOULD NOT ALLOW ME TO CREATE A POST WITH AN IMPROPER PAYLOAD, BUT IT RETURNS 201 INSTEAD OF 404.
    # FOR THAT REASON THIS TEST CASE IS FAILING.
    payload = {'unavailableVariable': 'N/A'}
    response = comments_api.create_a_comment(payload)
    assert response.status_code == 404


def test_negative_try_to_update_a_nonexistent_comment(comments_api):
    # THERE IS A BUG FOR THIS CONDITION.
    # NORMALLY IT SHOULD RETURN 404(NOT FOUND), BUT IT'S RETURNING 500 INTERNAL SERVER ERROR WHICH IS NOT CORRECT.
    # FOR THAT REASON THIS TEST CASE IS FAILING.
    payload = {'title': 'Updated Post', 'body': 'This post has been updated', 'userId': 101}
    response = comments_api.update_a_comment(501, payload)
    assert response.status_code == 404


def test_negative_try_to_partially_update_a_nonexistent_comment(comments_api):
    # THERE IS A BUG FOR THIS CONDITION.
    # NORMALLY IT SHOULD RETURN 404(NOT FOUND), BUT IT'S RETURNING 200 WHICH IS NOT CORRECT.
    # FOR THAT REASON THIS TEST CASE IS FAILING.
    payload = {'title': 'Partially Updated Post'}
    response = comments_api.partially_update_a_comment(501, payload)
    assert response.status_code == 404

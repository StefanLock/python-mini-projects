import pytest
import requests
from unittest.mock import MagicMock, patch
from client import UserNotFoundError, ApiError, get_github_user

@pytest.fixture
def mock_github_payload():
    return {
        'login': 'stefanlock', 
        'public_repos': 5,
        'followers': 100
    }

@patch("client.requests.get")
def test_get_github_user_success(mock_get, mock_github_payload):

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_github_payload

    mock_get.return_value = mock_response

    result = get_github_user("stefanlock")

    assert result == {
        'login': 'stefanlock', 
        'public_repos': 5,
        'followers': 100
    }
    mock_get.assert_called_once_with(
        "https://api.github.com/users/stefanlock", timeout=5
    )


@patch("client.requests.get")
def test_get_github_user_not_found(mock_get):
    # Simulate a 404 response
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    # Assert that your custom Exception is raised
    with pytest.raises(UserNotFoundError):
        get_github_user("nobody-here-12345")


@patch("client.requests.get")
def test_get_github_user_timeout(mock_get):
    # side_effect is used when you want the mock to actually raise an error
    mock_get.side_effect = requests.exceptions.Timeout("Connection timed out")

    # Assert that your script catches it and raises an ApiError
    with pytest.raises(ApiError):
        get_github_user("octocat")

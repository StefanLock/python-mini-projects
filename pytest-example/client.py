import requests

class UserNotFoundError(Exception):
    pass

class ApiError(Exception):
    pass

def get_github_user(username: str) -> dict:
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=5)
    except requests.RequestException as e:
        raise ApiError(f"Network error occurred: {e}")

    if response.status_code == 404:
        raise UserNotFoundError(f"User '{username}' was not found.")
    elif response.status_code != 200:
        raise ApiError(f"API response returned {response.status_code}")

    data = response.json()

    return {
        "login": data["login"],
        "public_repos": data["public_repos"],
        "followers": data["followers"],
    }

def main():
    try:
        info = get_github_user("stefanlock")
        print("Result:", info)
    except Exception as e:
        print(f"Failed with {type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
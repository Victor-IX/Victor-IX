import requests

REQUEST_COUNT = 0


def request_get(url: str, headers: dict = None, params: dict = None):
    global REQUEST_COUNT
    REQUEST_COUNT += 1

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response
        else:
            print(f"Error: API request failed with status code {response.status_code}")
            print(f"Response: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to connect to API: {e}")

    return None

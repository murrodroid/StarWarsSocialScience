import requests

def call_api(url, params=None, headers=None, method="GET", data=None):
    try:
        response = requests.request(method, url, params=params, headers=headers, json=data)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()  # or response.text if it's not JSON
    except requests.RequestException as e:
        print(f"API call failed: {e}")
        return None
import requests

SERVER_URL = "http://localhost:8080"  # change to your deployed URL later

def call_api(endpoint, data):
    try:
        response = requests.post(f"{SERVER_URL}/{endpoint}", json=data, timeout=2)
        response.raise_for_status()
        return response.json()['result']
    except requests.exceptions.Timeout:
        print("Request timed out")
    except Exception as e:
        print("Error:", e)

print("add(2,3) =", call_api("add", {"x": 2, "y": 3}))
print("multiply(4,5) =", call_api("multiply", {"x": 4, "y": 5}))

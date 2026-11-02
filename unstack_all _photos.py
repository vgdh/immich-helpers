import requests

BASE_URL = "http://localhost:2283/api"  # Change to your Immich instance URL
API_KEY = "YOUR_API_KEY_HERE"

headers = {
    "x-api-key": API_KEY,
    "Accept": "application/json",
    "Content-Type": "application/json",
}

# 1. Fetch all stacks
response = requests.get(f"{BASE_URL}/stacks", headers=headers)
response.raise_for_status()
stacks = response.json()

stack_ids = [stack["id"] for stack in stacks]
print(f"Found {len(stack_ids)} stacks to delete.")

# 2. Delete stacks in bulk
if stack_ids:
    del_response = requests.delete(
        f"{BASE_URL}/stacks", headers=headers, json={"ids": stack_ids}
    )
    del_response.raise_for_status()
    print("Successfully unstacked all images.")
else:
    print("No stacks found.")
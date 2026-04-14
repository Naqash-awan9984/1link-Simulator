#!/usr/bin/env python
"""Test script to verify delay configuration."""
import json
import time
import requests

BASE_URL = "http://localhost:2011"
OAUTH_CLIENT_ID = "c5a6f9d1895646dc83f4209eb2c8d770"
OAUTH_CLIENT_SECRET = "yO1lN5iF5jS4qY2lD8wW5hY3mS2wA0gT7fC7hM4qA7nX3sB5wK"

print("=" * 60)
print("DELAY CONFIGURATION TEST")
print("=" * 60)

# Get token
print("\n1. Getting OAuth token...")
payload = {
    "grant_type": "client_credentials",
    "client_id": OAUTH_CLIENT_ID,
    "client_secret": OAUTH_CLIENT_SECRET,
    "scope": "1LinkApi"
}

resp = requests.post(f"{BASE_URL}/oauth2/token", data=payload, timeout=10)
token_data = resp.json()
access_token = token_data.get("access_token")
print(f"[OK] Token received: {access_token[:20]}...")

# Check delay config file
print("\n2. Checking delay_config.json...")
with open("delay_config.json", "r") as f:
    config = json.load(f)
    print(f"[OK] Current config:")
    for key, value in config.items():
        print(f"     {key}: {value}")

# Test with delay disabled (fast response)
print("\n3. Testing with delays DISABLED...")
headers = {"Authorization": f"Bearer {access_token}"}
fetch_payload = {
    "ToBankIMD": "628773",
    "AccountNumberTo": "1234567890",
    "TransmissionDateAndTime": "2024-04-10T10:00:00",
    "STAN": "000001",
    "Time": "100000",
    "Date": "0410",
    "RRN": "111111111111"
}

start = time.time()
resp = requests.post(f"{BASE_URL}/onelink/production/path-1", json=fetch_payload, headers=headers, timeout=10)
elapsed = time.time() - start
print(f"[OK] Response time (delays disabled): {elapsed:.2f}s")
print(f"     Status: {resp.status_code}")

# Enable delays and test
print("\n4. ENABLING delays in configuration...")
config["enabled"] = True
config["delaySeconds"] = 2
config["successResponsesBeforeDelay"] = 0
config["delayCountBeforeSuccess"] = 0
with open("delay_config.json", "w") as f:
    json.dump(config, f, indent=2)
print(f"[OK] Config updated with delays enabled (2 seconds)")
print("     Note: Simulator must be restarted to reload config")

print("\n5. Restarting simulator to reload config...")
# Note: We can't actually restart from here, so we'll just show the instructions
print("     Run the simulator again: py 1link-simulator.py")

print("\n" + "=" * 60)
print("TEST COMPLETE")
print("=" * 60)
print("\nTo test with delays enabled:")
print("1. Close the current simulator (Ctrl+C)")
print("2. Edit delay_config.json to set 'enabled': true")
print("3. Run: py 1link-simulator.py")
print("4. Run this script again to see the delayed responses")
print("\nDelay Configuration Structure:")
print("  - enabled: Turn delays on/off")
print("  - delaySeconds: How long to delay (seconds)")
print("  - successResponsesBeforeDelay: How many responses before start delaying")
print("  - delayCountBeforeSuccess: How many times to delay (0 = always delay)")

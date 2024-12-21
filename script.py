import requests
import time
from datetime import datetime

# URL to call
url = "https://bwo-orcin.vercel.app/API/fetching_files"

# Function to trigger the API request
def trigger_api():
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            print(f"API triggered successfully: {response.text}")
        else:
            print(f"Failed to trigger API. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

# Run the API trigger every day between 8 AM to 10 AM
while True:
    current_time = datetime.now().time()
    if current_time.hour >= 8 and current_time.hour < 10:
        print(f"Triggering API at {current_time}")
        trigger_api()
        time.sleep(2)  # Wait for 1 hour before checking again
    else:
        print(f"Not the scheduled time. Current time is {current_time}.")
        time.sleep(2)  # Check every 10 minutes
trigger_api()
import os
import time
import base64
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
refresh_token = os.getenv('REFRESH_TOKEN')
token_url = os.getenv('TOKEN_URL')

# Function to refresh the access token
def refresh_access_token():
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode('ascii')).decode('ascii')
    headers = {
        'Authorization': f"Basic {auth_header}",
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    response = requests.post(token_url, headers=headers, data=data)
    
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get('access_token')
        new_refresh_token = token_data.get('refresh_token')
        expires_in = token_data.get('expires_in')
        scope = token_data.get('scope')

        print(f"New Access Token: {access_token}")
        print(f"New Refresh Token: {new_refresh_token}")
        print(f"Expires In: {expires_in}")
        print(f"Scope: {scope}")

        # Save the new refresh token to the .env file (or another secure location)
        with open('.env', 'a') as f:
            f.write(f"\nREFRESH_TOKEN={new_refresh_token}")

        return access_token, new_refresh_token
    else:
        print(f"Error: {response.json().get('error_description', 'No error description provided')}")
        return None, None

# Check if the access token is about to expire (within 5 minutes)
def is_token_expiring(expires_in):
    # Assuming expires_in is in seconds
    return expires_in <= 300

# Main function
def main():
    access_token = None
    expires_in = 3599  # Assume the token is new and valid for 1 hour (3600 seconds)

    while True:
        if is_token_expiring(expires_in):
            access_token, _ = refresh_access_token()
            expires_in = 3599  # Reset the expiry time for the new token

        # Sleep for a short period before checking again
        time.sleep(60)

if __name__ == "__main__":
    main()

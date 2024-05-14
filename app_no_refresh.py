from urllib.parse import urlencode
import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')
authorization_url = os.getenv('AUTHORIZATION_URL')
token_url = os.getenv('TOKEN_URL')


# Step 1: User Authorization
auth_params = {
    'response_type': 'code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    # Add any additional scopes here
}
auth_url = f"{authorization_url}?{urlencode(auth_params)}"
print(
    f"Navigate to the following URL to authorize the application: {auth_url}")

# Step 2: Receive Authorization Code
auth_code = input("Enter the authorization code: ")

# Step 3: Request Access Token
auth_header = base64.b64encode(
    f"{client_id}:{client_secret}".encode('ascii')).decode('ascii')
headers = {
    'Authorization': f"Basic {auth_header}",
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'grant_type': 'authorization_code',
    'code': auth_code,
    'redirect_uri': redirect_uri
}
token_response = requests.post(token_url, headers=headers, data=data)

if token_response.status_code == 200:
    token_data = token_response.json()
    access_token = token_data.get('access_token')
    token_type = token_data.get('token_type')
    refresh_token = token_data.get('refresh_token')
    expires_in = token_data.get('expires_in')
    scope = token_data.get('scope')

    print(f"Access Token: {access_token}")
    print(f"Token Type: {token_type}")
    print(f"Refresh Token: {refresh_token}")
    print(f"Expires In: {expires_in}")
    print(f"Scope: {scope}")

    # Use the access token to make API requests
else:
    print(f"Error: {token_response.json()['error_description']}")

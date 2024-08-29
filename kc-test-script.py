# %%
import requests

import json

from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single InsecureRequestWarning from urllib3 needed
requests.urllib3.disable_warnings(InsecureRequestWarning)

# %%
# Keycloak server details
KEYCLOAK_URL = 'https://your-keycloak-address.internal.go.id'
REALM = 'qa'  # or the name of the realm you created
CLIENT_ID = 'qa_client'  # your client ID
CLIENT_SECRET = 'my-client-secret'  # if applicable
USERNAME = 'qa_user'
PASSWORD = 'qa.user.password.!@#$^&*()'

# Endpoints from your OpenID configuration
TOKEN_URL = f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/token"
USERINFO_URL = f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/userinfo"
LOGOUT_URL = f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/logout"
INTROSPECT_URL = f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/token/introspect"

# %%
# Function to generate token
def generate_token():
    payload = {
        'client_id': CLIENT_ID,
        'username': USERNAME,
        'password': PASSWORD,
        'grant_type': 'password',
        'scope': 'openid profile email',  # Include necessary scopes
    }
    if CLIENT_SECRET:
        payload['client_secret'] = CLIENT_SECRET

    response = requests.post(TOKEN_URL, data=payload, verify=False)  # Ignore SSL cert verification
    response.raise_for_status()
    token_data = response.json()
    return token_data['access_token'], token_data['refresh_token']

# Function to get user details
def get_user_details(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(USERINFO_URL, headers=headers, verify=False)  # Ignore SSL cert verification
    response.raise_for_status()
    return response.json()

# Function to introspect token (check token validity)
def check_token(access_token):
    payload = {
        'token': access_token,
        'client_id': CLIENT_ID,
    }
    if CLIENT_SECRET:
        payload['client_secret'] = CLIENT_SECRET

    response = requests.post(INTROSPECT_URL, data=payload, verify=False)  # Ignore SSL cert verification
    response.raise_for_status()
    return response.json()

# Function to logout
def logout(refresh_token):
    payload = {
        'client_id': CLIENT_ID,
        'refresh_token': refresh_token,
    }
    if CLIENT_SECRET:
        payload['client_secret'] = CLIENT_SECRET

    response = requests.post(LOGOUT_URL, data=payload, verify=False)  # Ignore SSL cert verification
    response.raise_for_status()
    return response.status_code

# %%
# Main script
if __name__ == '__main__':
    try:
        # 1. Generate token
        access_token, refresh_token = generate_token()
        print("Access Token:", access_token)

        # 2. Get user details
        user_info = get_user_details(access_token)
        print("User Info:")
        print(json.dumps(user_info, indent=4))  # Pretty-print User Info

        # 3. Check token validity
        token_status = check_token(access_token)
        print("Token Status:")
        print(json.dumps(token_status, indent=4))  # Pretty-print Token Status

        # 4. Logout
        logout_status = logout(refresh_token)
        if logout_status == 204:
            print("Logout successful!")
        else:
            print("Logout failed!")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")



# %%

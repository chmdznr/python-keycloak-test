# Keycloak Authentication Test Script

This repository contains a Python script for testing Keycloak authentication and related operations. The script demonstrates how to interact with Keycloak's OpenID Connect endpoints for token generation, user information retrieval, token introspection, and logout.

## Features

- Generate access and refresh tokens
- Retrieve user information
- Check token validity
- Perform user logout

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/chmdznr/python-keycloak-test.git
   cd python-keycloak-test
   ```

2. Install the required dependencies:
   ```bash
   pip install requests
   ```

## Configuration

Before running the script, update the following variables in the `kc-test-script.py` file:

- `KEYCLOAK_URL`: The URL of your Keycloak server.
- `REALM`: The name of the realm you are using.
- `CLIENT_ID`: The client ID of your application.
- `CLIENT_SECRET`: The client secret of your application (if applicable).
- `USERNAME` and `PASSWORD`: The username and password for the user you want to authenticate.

## Running the Script

To run the script, execute the following command:

```bash
python kc-test-script.py
```

This will perform the following operations:
1. Generate an access token and refresh token
2. Retrieve user information
3. Check token validity
4. Perform user logout

## Script Structure

The script is organized into several functions:

- `generate_token()`: Generates access and refresh tokens
- `get_user_details(access_token)`: Retrieves user information
- `check_token(access_token)`: Checks token validity
- `logout(refresh_token)`: Performs user logout

The main execution block demonstrates the usage of these functions.

## Security Note

This script disables SSL certificate verification for testing purposes. In a production environment, always use proper SSL certificate validation.

## License

[MIT License](LICENSE)
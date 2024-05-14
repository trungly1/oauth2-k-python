# OAuth2 Token Management

This project provides scripts to handle OAuth2 token management, including obtaining access tokens and refreshing them automatically or manually. The scripts use environment variables to manage sensitive information securely.

## Setup

### Prerequisites

- Python 3.6 or later
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Unix or MacOS
    # or
    .\venv\Scripts\activate  # On Windows
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of the project and add the following environment variables:

    ```ini
    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    REDIRECT_URI=your_redirect_uri
    AUTHORIZATION_URL=https://api.trial.lsk.lightspeed.app/oauth/authorize
    TOKEN_URL=https://api.trial.lsk.lightspeed.app/oauth/token
    REFRESH_TOKEN=your_initial_refresh_token
    ```

## Usage

### Obtain Access Token

To obtain an access token, run the `oauth2_token.py` script. This script guides you through the authorization process and saves the access and refresh tokens to the `.env` file.

```bash
python oauth2_token.py
```

### Automated Token Refresh

The `refresh_token_auto.py` script automatically refreshes the access token if it is about to expire. You can set up a cron job (Unix/MacOS) or a scheduled task (Windows) to run this script periodically.

```bash
python refresh_token_auto.py
```

### Manual Token Refresh

The `refresh_token_manual.py` script allows you to manually refresh the access token.

```bash
python refresh_token_manual.py
```

## Environment Variables

The `.env` file should contain the following variables:

- `CLIENT_ID`: The client ID for your OAuth2 application.
- `CLIENT_SECRET`: The client secret for your OAuth2 application.
- `REDIRECT_URI`: The redirect URI for your OAuth2 application.
- `AUTHORIZATION_URL`: The URL to obtain the authorization code.
- `TOKEN_URL`: The URL to obtain the access token.
- `REFRESH_TOKEN`: The refresh token to obtain a new access token.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Requests](https://docs.python-requests.org/en/latest/) - HTTP library for Python
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Read key-value pairs from a .env file and set them as environment variables
- [ConfigParser](https://docs.python.org/3/library/configparser.html) - Configuration file parser included in the Python Standard Library


### Explanation

1. **Setup and Prerequisites**: Instructions for setting up the project, including Python version and virtual environment recommendations.
2. **Installation**: Steps to clone the repository, create a virtual environment, install dependencies, and set up the `.env` file.
3. **Usage**: Instructions on how to run the scripts for obtaining access tokens and refreshing tokens automatically or manually.
4. **Environment Variables**: Detailed explanation of the required environment variables in the `.env` file.
5. **License**: Licensing information (replace with your specific license if different).
6. **Acknowledgments**: Credit to the libraries used in the project.

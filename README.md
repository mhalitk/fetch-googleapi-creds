# Google Authentication Script

This script automates the process of generating OAuth 2.0 credentials for accessing Google APIs. It handles the OAuth flow, redirecting the user to the authentication page and saving the acquired credentials to a file. This is particularly useful for applications that need to interact with Google APIs and require offline access or specific scopes.

## Features

- OAuth 2.0 authentication flow
- Saves credentials to a JSON file for later use
- Customizable OAuth scopes

## Prerequisites

- Python 3.x
- `google-auth-oauthlib` library
- Google Cloud project with OAuth 2.0 Client ID and secret

## Installation

Before running the script, ensure you have Python installed and then install the required Python library using pip:

```bash
pip install google-auth-oauthlib
```

## Configuration

1. **Create OAuth 2.0 Client ID and Secret:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Navigate to the credentials section.
   - Follow the steps to [create an OAuth 2.0 Client ID and secret](https://support.google.com/cloud/answer/6158849?hl=en#zippy=%2Cstep-create-a-new-client-secret).
   - Download the JSON file containing the Client ID and secret.

2. **Set Up Scopes:**
   - Edit the `SCOPES` variable in the script to include the OAuth scopes needed for your application. By default, it is set to `https://www.googleapis.com/auth/drive` for Google Drive access. You can find a list of scopes [here](https://developers.google.com/identity/protocols/oauth2/scopes).

3. **Place the Client Secret File:**
   - Ensure the downloaded JSON file is named `client_secret.json` and is located in the same directory as the script.

## Usage

To run the script, simply execute it from the command line:

```bash
python get_credentials.py
```

Follow the instructions printed to the console:
1. The script will opens a url with default browser.
2. Log in with your Google account and authorize the application.

The script will save the credentials to `credentials.json` in the same directory. This file can then be used for authenticating requests to the Google APIs.

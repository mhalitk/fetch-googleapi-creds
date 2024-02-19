import os

from google_auth_oauthlib.flow import Flow

SCOPES = [
    # Add scopes you need here -- /auth/drive is an example
    "https://www.googleapis.com/auth/drive",
]

# This is the output file
CREDENTIALS_FILE = "credentials.json"
# OAuth 2.0 Client ID file. It can be downloaded from Google Cloud Console.
# https://support.google.com/cloud/answer/6158849?hl=en#zippy=%2Cstep-create-a-new-client-secret
CLIENT_SECRET_FILE = "client_secret.json"


def main():
    if not os.path.exists(CLIENT_SECRET_FILE):
        print(
            f"Client secret file is not found in location {CLIENT_SECRET_FILE}, exiting"
        )
        return 1

    # Auth code is not auto-handled yet. But the auth screen will try to redirect
    # to localhost. You can manually copy the value of `code` url parameter.
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE, scopes=SCOPES, redirect_uri="http://127.0.0.1:8000"
    )

    auth_url = flow.authorization_url(prompt="consent")

    print(f"Please go to this URL: {auth_url[0]}")

    code = input("Enter the authorization code: ")
    flow.fetch_token(code=code)

    with open(CREDENTIALS_FILE, "w") as f:
        f.write(flow.credentials.to_json())
        print(f"Credentials saved to {CREDENTIALS_FILE}")

    return 0


if __name__ == "__main__":
    exit(main())

import http.server
import os
import threading
import webbrowser

from google_auth_oauthlib.flow import Flow

SCOPES = [
    # Add scopes you need here -- /auth/drive is an example
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive.metadata",
]

# This is the output file
CREDENTIALS_FILE = "credentials.json"
# OAuth 2.0 Client ID file. It can be downloaded from Google Cloud Console.
# https://support.google.com/cloud/answer/6158849?hl=en#zippy=%2Cstep-create-a-new-client-secret
CLIENT_SECRET_FILE = "client_secret.json"


class RedirectHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if "code" in self.path:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(
                b"<html><head><title>Authentication Successful</title></head>"
            )
            self.wfile.write(b"<body><h2>Authentication successful.</h2>")
            self.wfile.write(b"<p>You can now close this tab.</p></body></html>")

            code = self.path.split("code=")[1].split("&")[0]
            self.server.flow.fetch_token(code=code)
            with open(CREDENTIALS_FILE, "w") as f:
                f.write(self.server.flow.credentials.to_json())

            print(f"Credentials saved to {CREDENTIALS_FILE}")
            threading.Thread(target=self.server.shutdown, daemon=True).start()
        else:
            self.send_response(400)
            self.end_headers()


def run_server(flow):
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, RedirectHandler)
    httpd.flow = flow
    httpd.serve_forever()


def main():
    if not os.path.exists(CLIENT_SECRET_FILE):
        print(
            f"Client secret file is not found in location {CLIENT_SECRET_FILE}, exiting"
        )
        return 1

    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE, scopes=SCOPES, redirect_uri="http://127.0.0.1:8000"
    )

    auth_url, _ = flow.authorization_url(prompt="consent")

    print(f"Opening url: {auth_url}")
    webbrowser.open(auth_url)

    run_server(flow)

    return 0


if __name__ == "__main__":
    exit(main())

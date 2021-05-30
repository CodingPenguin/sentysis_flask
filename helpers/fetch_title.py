import os, config, webbrowser

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def fetch_title(video_id):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # TODO: SET TO 0 ON PROD

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = config.client_secret
    print(client_secrets_file)

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    flow.redirect_uri = 'http://localhost:4200' # TODO: SET TO https://sentysis-angular.herokuapp.com
    # lol come back to this maybe webbrowser.open(flow.authorization_url())
    credentials = flow.run_console()
    
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()

    return response

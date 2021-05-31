import os
import googleapiclient.discovery

def fetch_comments(video_id):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1" # TODO: SET TO 0 ON PROD

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY =  os.environ.get("API_KEY") # config.API_KEY
    print(DEVELOPER_KEY)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY
    )

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=50,
        order="relevance",
        videoId=video_id
    )
    response = request.execute()
    return response

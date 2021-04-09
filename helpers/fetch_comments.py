import os, config

def fetch_comments(video_id):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # if(config.IS_DEV):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1" # OAUTHLIB VERIFICATION DISABLED
    # else:
    #     os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = config.API_KEY

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY
    )

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        order="relevance"
    )
    response = request.execute()

    return response

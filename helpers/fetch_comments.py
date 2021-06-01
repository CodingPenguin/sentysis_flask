import os
import googleapiclient.discovery

def fetch_comments(video_id):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY =  os.environ.get("API_KEY")
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY
    )

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=25,
        order="relevance",
        videoId=video_id
    )
    response = request.execute()
    return response

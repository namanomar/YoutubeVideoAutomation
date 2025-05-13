from googleapiclient.discovery import build
import isodate
from datetime import datetime, timedelta, timezone
from config import YOUTUBE_API_KEY

def fetch_youtube_videos(query, max_results=20):
    """
    Fetches YouTube videos based on a search query.
    Filters videos to include only those with a duration between 4 and 20 minutes,
    and posted within the last 14 days.
    """
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    published_after = (datetime.now(timezone.utc) - timedelta(days=14)).isoformat()

    search_response = youtube.search().list(
        q=query,
        type="video",
        part="id,snippet",
        maxResults=max_results,
        publishedAfter=published_after,
        videoDuration="medium"
    ).execute()

    video_ids = [item['id']['videoId'] for item in search_response['items']]

    if not video_ids:
        return []

    details_response = youtube.videos().list(
        part="snippet,contentDetails",
        id=",".join(video_ids)
    ).execute()
    
    results = []
    
    for item in details_response['items']:
            duration_str = item['contentDetails']['duration']
            duration = isodate.parse_duration(duration_str)
            duration_minutes = duration.total_seconds() / 60
            results.append({
                "title": item['snippet']['title'],
                "description": item['snippet']['description'],
                "url": f"https://www.youtube.com/watch?v={item['id']}",
                "duration": round(duration_minutes, 2)
            })
    return results

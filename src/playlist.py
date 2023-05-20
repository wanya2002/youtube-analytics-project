import json
import datetime
import os
import isodate
from googleapiclient.discovery import build

class PlayList:
    api_key = os.getenv('YT_API_KEY')

    """Создание нового класса PlayList"""
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.playlists = self.youtube.playlists().list(id=self.playlist_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()
        self.title = self.playlists['items'][0]['snippet']['title']
        self.url = self.playlists['items'][0]['snippet']['thumbnails']['default']['url']



    def print_info(self) -> None:

        """Выводит в консоль информацию о канале."""
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.playlists = self.youtube.playlists().list(id=self.playlist_id,
                                                       part='contentDetails,snippet',
                                                       maxResults=50,
                                                       ).execute()
        print(json.dumps(self.playlists, indent=2, ensure_ascii=False))

    def total_duration(self):
        api_key = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,
                                                                 part='contentDetails',
                                                                 maxResults=50,
                                                                 ).execute()
        video_ids = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                              id=','.join(video_ids)
                                               ).execute()

        total_video_duration = datetime.timedelta(hours=0, minutes=0, seconds=0)

        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)

            duration_split = str(duration).split(':')
            duration = datetime.timedelta(hours=int(duration_split[0]), minutes=int(duration_split[1]),
                                         seconds=int(duration_split[2]))

            total_video_duration += duration

        return total_video_duration

    def show_best_video(self):
        api_key = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        video_ids = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        best_video_like_count = 0
        best_video_url = ''

        for video in video_response['items']:
            like_count = int(video['statistics']['likeCount'])
            if like_count > best_video_like_count:
                best_video_like_count = like_count
                best_video_url = f"https://youtu.be/{video['id']}"
        return best_video_url










import os
from googleapiclient.discovery import build
import json

class Video:
   """Создаем новый класс Video"""
   api_key = os.getenv('YT_API_KEY')

   def __init__(self, video_id: str) -> None:
       self.video_id = video_id
       self.youtube = build('youtube', 'v3', developerKey=self.api_key)
       self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                              id=self.video_id
                                              ).execute()
       self.video_title = self.video_response['items'][0]['snippet']['title']
       self.video_id = self.video_response['items'][0]['snippet']['thumbnails']['default']['url']
       self.view_count = self.video_response['items'][0]['statistics']['viewCount']
       self.like_count = self.video_response['items'][0]['statistics']['likeCount']

   def __str__(self):
       return self.video_title

class PLVideo:
    """Создаем новый класс PLVideo"""
    api_key = os.getenv('YT_API_KEY')

    def __init__(self, video_id, playlist_id):
        self.video_id = video_id
        self.playlist_id = playlist_id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=self.video_id
                                                         ).execute()
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        self.video_title = self.video_response['items'][0]['snippet']['title']
        self.video_id = self.video_response['items'][0]['snippet']['thumbnails']['default']['url']
        self.view_count = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count = self.video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.video_title



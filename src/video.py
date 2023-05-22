import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



class Video:

   """Создаем новый класс Video"""

   api_key = os.getenv('YT_API_KEY')
   youtube = build('youtube', 'v3', developerKey=api_key)

   def __init__(self, video_id):
       self.video_id = video_id
       self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                              id=self.video_id
                                              ).execute()
       try:
          self.video_title = self.video_response['items'][0]['snippet']['title']
          self.video_url = self.video_response['items'][0]['snippet']['thumbnails']['default']['url']
          self.view_count = self.video_response['items'][0]['statistics']['viewCount']
          self.like_count = self.video_response['items'][0]['statistics']['likeCount']
       except IndexError:
           self.video_title = None
           self.video_url = None
           self.view_count = None
           self.like_count = None
       except HttpError:
           self.video_title = None
           self.video_url = None
           self.view_count = None
           self.like_count = None

   def __str__(self):
       return self.video_title

class PLVideo(Video):
    """Создаем новый класс PLVideo"""
    api_key = os.getenv('YT_API_KEY')

    def __init__(self, video_id: str, playlist_id: str):
        super(PLVideo, self).__init__(video_id)
        self.playList_id = playlist_id
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=self.playList_id,
                                                                 part='contentDetails',
                                                                 maxResults=50,
                                                                 ).execute()


    def __str__(self):
        return self.video_title



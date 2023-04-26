import json
import os
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriber = self.channel['items'][0]['statistics']['subscriberCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']



    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        cls.youtube = build('youtube', 'v3', developerKey=cls.api_key)
        return cls.youtube

    def to_json (self, name):
        data = [self.__channel_id, self.title, self.description, self.url, self.subscriber, self.view_count, self.video_count]
        with open(name, 'w') as f:
            json.dump(data, f)

    @property
    def channel_id(self):
        return self.__channel_id






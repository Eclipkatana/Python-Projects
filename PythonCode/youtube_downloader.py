from pytube import YouTube 
from threading import Thread    
import requests
from PySide6.QtCore import QObject, Signal

class Youtube_Downloadeṛ(QObject):
    progress_callback = Signal(int)
    def __init__(self, url, path, extension):
        super().__init__()
        self.url=url
        self.path=path
        self.extension=extension
        self.download_thread=None
        
    def start_download(self):
        self.download_thread=Thread(target=self.download_audio)
        self.download_thread.start()
        
    def download_audio(self):
        yt = YouTube(self.url)
        stream=yt.streams.filter(only_audio=True, file_extension=self.extension).order_by("abr").desc().first()
        
        total_bytes = stream.filesize
        bytes_downloaded = 0
        response = requests.get(stream.url, stream=True)
        with open(self.path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=10000):
                if chunk:
                    f.write(chunk)
                    bytes_downloaded += len(chunk)
                    progress = (bytes_downloaded / total_bytes) * 100
                    self.progress_callback.emit(int(progress))
        
    def download_youtube_audio_NO_PROGRESS_BAR(self):
        try:
            yt = YouTube(self.url)
            stream=yt.streams.filter(only_audio=True, file_extension=self.extension).order_by("abr").desc().first()
            
            stream.download(self.path)
            
            return stream.abr, stream.title , stream.filesize
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=U44j_OHK50M"
    path= r"C:\Users\bibon\OneDrive\Desktop\Git\Python\Python-Projects\PythonCode"
    extention= "mp4"
    callback=1
    ydownloader=Youtube_Downloader(url, path, extention, callback)
    
    ydownloader.download_youtube_audio_NO_PROGRESS_BAR()
    
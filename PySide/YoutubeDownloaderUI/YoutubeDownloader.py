from YoutubeDownload_ui import Ui_YouTube_Downloader_UI

from PySide6.QtWidgets import QApplication, QFileDialog, QWidget

import sys

sys.path.append(
    r"C:\Users\bibon\OneDrive\Desktop\Git\Python\Python-Projects\PythonCode"
)
from youtube_downloader import Youtube_Downloadeṛ

import os

class Youtube_Downloader_UI(QWidget, Ui_YouTube_Downloader_UI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Youtube Downloader")

        self.browse_button.clicked.connect(self.browse_path)
        self.download_button.clicked.connect(self.download_video_NO_PROGRESS_BAR)

        self.download_progress_bar.setValue(0)
        #self.save_path_text.setText(r"C:\Users\bibon\OneDrive\Desktop\Git\Python\Python-Projects\PythonCode\YoutubeDownloaderUI\video.mp4")   
        #self.url_link_text.setText("https://www.youtube.com/watch?v=U44j_OHK50M")
        
    def browse_path(self):
        file_path = QFileDialog.getExistingDirectory()
        self.save_path_text.setText(file_path)

    def download_video_WITH_PROGRESS_BAR(self):
        url = self.url_link_text.text()
        path_input = self.save_path_text.text()
        path = os.path.abspath(path_input)
        extension = self.comboBox.currentText()

        if not url:
            self.output_text.setText("URL can not be empty")
            return

        if not path:
            self.output_text.setText("Path can not be empty")
            return

         # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(path), exist_ok=True)
        
        self.ydownloader = Youtube_Downloadeṛ(url, path, extension)
        self.ydownloader.progress_callback.connect(self.progress_callback)
        self.ydownloader.start_download()

    def progress_callback(self,progress):
        self.download_progress_bar.setValue(progress)
    
    def download_video_NO_PROGRESS_BAR(self):
        url = self.url_link_text.text()
        path = self.save_path_text.text()
        extension = self.comboBox.currentText()

        if not url:
            self.output_text.setText("URL can not be empty")
            return

        if not path:
            self.output_text.setText("Path can not be empty")
            return
        
        self.ydownloader = Youtube_Downloadeṛ(url, path, extension)
        
        quality, title, file_size =self.ydownloader.download_youtube_audio_NO_PROGRESS_BAR()

        self.output_text.setText(f"Downloaded {title} successfully in highest quality {quality}. File size: {file_size/1024:.0f} KB or {file_size/1024/1024:.0f} MB")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Youtube_Downloader_UI()
    window.show()

    app.exec()
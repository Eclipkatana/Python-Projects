from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGraphicsScene,
)
from Main_Window_ui import Ui_MainWindow

import sys

# sys.path.append('../CurrencyConverterUI')
sys.path.append(
    r"C:\Users\bibon\OneDrive\Desktop\Git\Python\Python-Projects\PySide\CurrencyConverterUI"
)
from CurrencyUI import Currency_Converter_UI

sys.path.append(
    r"C:\Users\bibon\OneDrive\Desktop\Git\Python\Python-Projects\PySide\YoutubeDownloaderUI"
)
from YoutubeDownloader import Youtube_Downloader_UI

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import numpy as np


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("MainApplication")

        self.icon_name_widget.setHidden(True)

        self.dashboard_1.clicked.connect(self.switch_to_dashboardPage)
        self.graph_1.clicked.connect(self.switch_to_graphPage)
        self.message_1.clicked.connect(self.switch_to_messagePage)
        self.noti_1.clicked.connect(self.switch_to_notificationPage)
        self.settings_1.clicked.connect(self.switch_to_settingPage)

        self.dashboard_2.clicked.connect(self.switch_to_dashboardPage)
        self.graph_1.clicked.connect(self.switch_to_graphPage)
        self.message_2.clicked.connect(self.switch_to_messagePage)
        self.noti_2.clicked.connect(self.switch_to_notificationPage)
        self.settings_2.clicked.connect(self.switch_to_settingPage)
        self.exit_button.clicked.connect(self.close)

        self.scene = QGraphicsScene()
        self.graph_test.setScene(self.scene)

        # Currency Converter UI
        self.push_button_graph.clicked.connect(self.plot_data_test)
        self.currency_button.clicked.connect(self.currency_exchange)
        self.ydownloader_button.clicked.connect(self.youtube_downloader)
        
    def youtube_downloader(self):
        self.ydownloader_UI = Youtube_Downloader_UI()
        self.ydownloader_UI.show()

        # Optionally center the currency UI on the screen
        self.ydownloader_UI.move(
            self.geometry().center() - self.ydownloader_UI.rect().center()
        )
    
    def currency_exchange(self):
        self.currency_UI = Currency_Converter_UI()
        self.currency_UI.show()

        # Optionally center the currency UI on the screen
        self.currency_UI.move(
            self.geometry().center() - self.currency_UI.rect().center()
        )

    def plot_data_test(self):
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        self.plot(x, y)

    def plot(self, x, y):
        fig, ax = plt.subplots()
        ax.plot(x, y)

        canvas = FigureCanvas(fig)
        canvas.setGeometry(0, 0, self.graph_test.width(), self.graph_test.height())

        self.scene.clear()
        self.scene.addWidget(canvas)

    def switch_to_dashboardPage(self):  # Dashboard Page is index 0
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_graphPage(self):  # Graph Page is index 4
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_messagePage(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_notificationPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_settingPage(self):
        self.stackedWidget.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    app.exec()

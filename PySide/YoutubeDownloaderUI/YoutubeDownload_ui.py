# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YoutubeDownload.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)
import resourses_rc
import resourses_rc

class Ui_YouTube_Downloader_UI(object):
    def setupUi(self, YouTube_Downloader_UI):
        if not YouTube_Downloader_UI.objectName():
            YouTube_Downloader_UI.setObjectName(u"YouTube_Downloader_UI")
        YouTube_Downloader_UI.resize(567, 474)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/youtube.jpg", QSize(), QIcon.Normal, QIcon.Off)
        YouTube_Downloader_UI.setWindowIcon(icon)
        YouTube_Downloader_UI.setStyleSheet(u"#YouTube_Downloader_UI {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.954545, y2:0.954545, stop:0 rgba(49, 87, 250, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"	text-align:center;\n"
"	padding: 4px 8px;\n"
"	border: 1px solid rgb(127,127,127);\n"
"	border-radius:5px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(137, 208, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	padding-left:10px\n"
"}")
        self.gridLayout_3 = QGridLayout(YouTube_Downloader_UI)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(YouTube_Downloader_UI)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.comboBox = QComboBox(YouTube_Downloader_UI)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 2, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(YouTube_Downloader_UI)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(110, 0))
        self.label_2.setMaximumSize(QSize(100, 70))
        self.label_2.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.url_link_text = QLineEdit(YouTube_Downloader_UI)
        self.url_link_text.setObjectName(u"url_link_text")
        self.url_link_text.setMaximumSize(QSize(450, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.url_link_text)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.save_path_text = QLineEdit(YouTube_Downloader_UI)
        self.save_path_text.setObjectName(u"save_path_text")
        self.save_path_text.setMaximumSize(QSize(450, 16777215))

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.save_path_text)

        self.browse_button = QPushButton(YouTube_Downloader_UI)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setMinimumSize(QSize(110, 0))

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.browse_button)


        self.gridLayout_2.addLayout(self.formLayout_3, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 4, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(YouTube_Downloader_UI)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(60, 20))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_6.setFont(font1)

        self.verticalLayout.addWidget(self.label_6)

        self.download_progress_bar = QProgressBar(YouTube_Downloader_UI)
        self.download_progress_bar.setObjectName(u"download_progress_bar")
        self.download_progress_bar.setMaximumSize(QSize(16777215, 20))
        self.download_progress_bar.setValue(24)

        self.verticalLayout.addWidget(self.download_progress_bar)

        self.output_text = QTextEdit(YouTube_Downloader_UI)
        self.output_text.setObjectName(u"output_text")
        self.output_text.setMaximumSize(QSize(16777215, 100))
        self.output_text.setReadOnly(True)

        self.verticalLayout.addWidget(self.output_text)


        self.gridLayout_3.addLayout(self.verticalLayout, 5, 0, 1, 3)

        self.groupBox = QGroupBox(YouTube_Downloader_UI)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"border:none\n"
"")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(80, 80))
        self.label.setSizeIncrement(QSize(90, 90))
        self.label.setBaseSize(QSize(90, 90))
        self.label.setToolTipDuration(0)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"border-radius: 5px")
        self.label.setPixmap(QPixmap(u":/newPrefix/icons/youtube.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(20)
        self.label_3.setFont(font2)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(194, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 3)

        self.download_button = QPushButton(YouTube_Downloader_UI)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setMaximumSize(QSize(200, 30))
        self.download_button.setBaseSize(QSize(50, 50))
        font3 = QFont()
        font3.setPointSize(16)
        self.download_button.setFont(font3)

        self.gridLayout_3.addWidget(self.download_button, 4, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 4, 0, 1, 1)


        self.retranslateUi(YouTube_Downloader_UI)

        QMetaObject.connectSlotsByName(YouTube_Downloader_UI)
    # setupUi

    def retranslateUi(self, YouTube_Downloader_UI):
        YouTube_Downloader_UI.setWindowTitle(QCoreApplication.translate("YouTube_Downloader_UI", u"YouTube Downloader", None))
        self.label_5.setText(QCoreApplication.translate("YouTube_Downloader_UI", u"File Extension", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("YouTube_Downloader_UI", u"mp4", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("YouTube_Downloader_UI", u"mp3", None))

        self.label_2.setText(QCoreApplication.translate("YouTube_Downloader_UI", u"URL Link", None))
        self.browse_button.setText(QCoreApplication.translate("YouTube_Downloader_UI", u"Browse Save Path", None))
        self.label_6.setText(QCoreApplication.translate("YouTube_Downloader_UI", u"Progress", None))
        self.groupBox.setTitle("")
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("YouTube_Downloader_UI", u"YouTube Downloader", None))
        self.download_button.setText(QCoreApplication.translate("YouTube_Downloader_UI", u"Download", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resourses_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(217, 212, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31,149,239);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color:white;\n"
"	height:30px;\n"
"	border:none;\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(181, 255, 204);\n"
"	color: rgb(255, 118, 84);\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/newPrefix/icons/boy.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setIconSize(QSize(25, 25))
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_1)

        self.graph_1 = QPushButton(self.icon_only_widget)
        self.graph_1.setObjectName(u"graph_1")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.graph_1.setIcon(icon1)
        self.graph_1.setIconSize(QSize(25, 25))
        self.graph_1.setCheckable(True)
        self.graph_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.graph_1)

        self.message_1 = QPushButton(self.icon_only_widget)
        self.message_1.setObjectName(u"message_1")
        self.message_1.setIcon(icon1)
        self.message_1.setIconSize(QSize(25, 25))
        self.message_1.setCheckable(True)
        self.message_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.message_1)

        self.noti_1 = QPushButton(self.icon_only_widget)
        self.noti_1.setObjectName(u"noti_1")
        self.noti_1.setIcon(icon1)
        self.noti_1.setIconSize(QSize(25, 25))
        self.noti_1.setCheckable(True)
        self.noti_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.noti_1)

        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        self.settings_1.setIcon(icon1)
        self.settings_1.setIconSize(QSize(25, 25))
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settings_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 310, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exit_button = QPushButton(self.icon_only_widget)
        self.exit_button.setObjectName(u"exit_button")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon2)
        self.exit_button.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.exit_button)


        self.gridLayout.addWidget(self.icon_only_widget, 1, 1, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31,149,239);\n"
"	color:white\n"
"}\n"
"\n"
"QPushButton {\n"
"	color:white;\n"
"	text-align:left;\n"
"	height:30px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
"\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(181, 255, 204);\n"
"	color: rgb(255, 118, 84);\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/icons/boy.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_name_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        icon3 = QIcon()
        icon3.addFile(u":/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_2.setIcon(icon3)
        self.dashboard_2.setIconSize(QSize(25, 25))
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_2)

        self.graph_2 = QPushButton(self.icon_name_widget)
        self.graph_2.setObjectName(u"graph_2")
        icon4 = QIcon()
        icon4.addFile(u":/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.graph_2.setIcon(icon4)
        self.graph_2.setIconSize(QSize(25, 25))
        self.graph_2.setCheckable(True)
        self.graph_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.graph_2)

        self.message_2 = QPushButton(self.icon_name_widget)
        self.message_2.setObjectName(u"message_2")
        self.message_2.setIcon(icon4)
        self.message_2.setIconSize(QSize(25, 25))
        self.message_2.setCheckable(True)
        self.message_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.message_2)

        self.noti_2 = QPushButton(self.icon_name_widget)
        self.noti_2.setObjectName(u"noti_2")
        self.noti_2.setIcon(icon4)
        self.noti_2.setIconSize(QSize(25, 25))
        self.noti_2.setCheckable(True)
        self.noti_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.noti_2)

        self.settings_2 = QPushButton(self.icon_name_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setIcon(icon4)
        self.settings_2.setIconSize(QSize(25, 25))
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settings_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 238, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_8 = QPushButton(self.icon_name_widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon5 = QIcon()
        icon5.addFile(u":/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.pushButton_8)


        self.gridLayout.addWidget(self.icon_name_widget, 1, 2, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_6 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_13 = QPushButton(self.header_widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"border:none")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons/order-food.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon6)
        self.pushButton_13.setIconSize(QSize(40, 40))
        self.pushButton_13.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.pushButton_13)

        self.horizontalSpacer_2 = QSpacerItem(95, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_14 = QPushButton(self.header_widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon7)

        self.horizontalLayout.addWidget(self.pushButton_14)


        self.horizontalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(95, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.pushButton_15 = QPushButton(self.header_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"border:none")
        icon8 = QIcon()
        icon8.addFile(u":/icons/boy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon8)

        self.horizontalLayout_6.addWidget(self.pushButton_15)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"#stackedWidget {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(82, 209, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left:10px\n"
"}")
        self.dashboar_page = QWidget()
        self.dashboar_page.setObjectName(u"dashboar_page")
        self.currency_button = QPushButton(self.dashboar_page)
        self.currency_button.setObjectName(u"currency_button")
        self.currency_button.setGeometry(QRect(20, 20, 75, 61))
        self.currency_button.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"padding-bottom:5px\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(181, 255, 204);\n"
"	color: rgb(255, 118, 84);\n"
"	font-weight:bold;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/icons/currency_exchange.png", QSize(), QIcon.Normal, QIcon.Off)
        self.currency_button.setIcon(icon9)
        self.currency_button.setIconSize(QSize(70, 70))
        self.currency_button.setCheckable(True)
        self.ydownloader_button = QPushButton(self.dashboar_page)
        self.ydownloader_button.setObjectName(u"ydownloader_button")
        self.ydownloader_button.setGeometry(QRect(130, 20, 75, 61))
        self.ydownloader_button.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(181, 255, 204);\n"
"	color: rgb(255, 118, 84);\n"
"	font-weight:bold;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/icons/youtube.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.ydownloader_button.setIcon(icon10)
        self.ydownloader_button.setIconSize(QSize(70, 70))
        self.stackedWidget.addWidget(self.dashboar_page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.graph_page = QWidget()
        self.graph_page.setObjectName(u"graph_page")
        self.graph_test = QGraphicsView(self.graph_page)
        self.graph_test.setObjectName(u"graph_test")
        self.graph_test.setGeometry(QRect(10, 70, 571, 411))
        self.push_button_graph = QPushButton(self.graph_page)
        self.push_button_graph.setObjectName(u"push_button_graph")
        self.push_button_graph.setGeometry(QRect(220, 20, 131, 24))
        self.stackedWidget.addWidget(self.graph_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 1, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.pushButton_13.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_13.toggled.connect(self.icon_name_widget.setVisible)
        self.settings_1.toggled.connect(self.settings_2.setChecked)
        self.noti_1.toggled.connect(self.noti_2.setChecked)
        self.message_1.toggled.connect(self.message_2.setChecked)
        self.graph_1.toggled.connect(self.graph_2.setChecked)
        self.dashboard_1.toggled.connect(self.dashboard_2.setChecked)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.graph_2.toggled.connect(self.graph_1.setChecked)
        self.message_2.toggled.connect(self.message_1.setChecked)
        self.noti_2.toggled.connect(self.noti_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.dashboard_1.setText("")
        self.graph_1.setText("")
        self.message_1.setText("")
        self.noti_1.setText("")
        self.settings_1.setText("")
        self.exit_button.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.graph_2.setText(QCoreApplication.translate("MainWindow", u"Graph", None))
        self.message_2.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.noti_2.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.pushButton_13.setText("")
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_15.setText("")
        self.currency_button.setText("")
        self.ydownloader_button.setText("")
        self.push_button_graph.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi


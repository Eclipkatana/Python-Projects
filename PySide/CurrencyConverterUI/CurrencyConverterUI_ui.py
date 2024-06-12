# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CurrencyConverterUI.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(460, 358)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setFamilies([u"Yu Gothic Medium"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.currrency1_label = QLabel(self.groupBox)
        self.currrency1_label.setObjectName(u"currrency1_label")
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic Medium"])
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.currrency1_label.setFont(font1)

        self.gridLayout_2.addWidget(self.currrency1_label, 0, 0, 1, 1)

        self.amount_label = QLabel(self.groupBox)
        self.amount_label.setObjectName(u"amount_label")
        self.amount_label.setFont(font1)

        self.gridLayout_2.addWidget(self.amount_label, 2, 0, 1, 1)

        self.currency1_input_text = QLineEdit(self.groupBox)
        self.currency1_input_text.setObjectName(u"currency1_input_text")

        self.gridLayout_2.addWidget(self.currency1_input_text, 0, 1, 1, 1)

        self.amount_input_text = QLineEdit(self.groupBox)
        self.amount_input_text.setObjectName(u"amount_input_text")

        self.gridLayout_2.addWidget(self.amount_input_text, 2, 1, 1, 1)

        self.currency2_input_text = QLineEdit(self.groupBox)
        self.currency2_input_text.setObjectName(u"currency2_input_text")

        self.gridLayout_2.addWidget(self.currency2_input_text, 1, 1, 1, 1)

        self.currrency2_label = QLabel(self.groupBox)
        self.currrency2_label.setObjectName(u"currrency2_label")
        self.currrency2_label.setFont(font1)

        self.gridLayout_2.addWidget(self.currrency2_label, 1, 0, 1, 1)

        self.output_label = QLabel(self.groupBox)
        self.output_label.setObjectName(u"output_label")
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic Medium"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.output_label.setFont(font2)

        self.gridLayout_2.addWidget(self.output_label, 5, 0, 1, 2)

        self.convert_button = QPushButton(self.groupBox)
        self.convert_button.setObjectName(u"convert_button")
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic Medium"])
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.convert_button.setFont(font3)

        self.gridLayout_2.addWidget(self.convert_button, 4, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Currency Converter", None))
        self.currrency1_label.setText(QCoreApplication.translate("Form", u"Currency 1", None))
        self.amount_label.setText(QCoreApplication.translate("Form", u"Amount", None))
        self.currrency2_label.setText(QCoreApplication.translate("Form", u"Currency 2", None))
        self.output_label.setText(QCoreApplication.translate("Form", u"Output", None))
        self.convert_button.setText(QCoreApplication.translate("Form", u"Convert", None))
    # retranslateUi


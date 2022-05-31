# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiFdgWcQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LeftFrame = QFrame(self.centralwidget)
        self.LeftFrame.setObjectName(u"LeftFrame")
        self.LeftFrame.setFrameShape(QFrame.StyledPanel)
        self.LeftFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.LeftFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.LeftFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.FileNameLabel = QLabel(self.frame_3)
        self.FileNameLabel.setObjectName(u"FileNameLabel")

        self.horizontalLayout_4.addWidget(self.FileNameLabel)

        self.FileBrowseButton = QPushButton(self.frame_3)
        self.FileBrowseButton.setObjectName(u"FileBrowseButton")

        self.horizontalLayout_4.addWidget(self.FileBrowseButton)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.LeftFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SimpulAsalLabel = QLabel(self.frame_4)
        self.SimpulAsalLabel.setObjectName(u"SimpulAsalLabel")

        self.horizontalLayout_2.addWidget(self.SimpulAsalLabel)

        self.SimpulAsalComboBox = QComboBox(self.frame_4)
        self.SimpulAsalComboBox.setObjectName(u"SimpulAsalComboBox")

        self.horizontalLayout_2.addWidget(self.SimpulAsalComboBox)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.LeftFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.SimpulTujuanLabel = QLabel(self.frame_5)
        self.SimpulTujuanLabel.setObjectName(u"SimpulTujuanLabel")

        self.horizontalLayout_3.addWidget(self.SimpulTujuanLabel)

        self.SimpulTujuanComboBox = QComboBox(self.frame_5)
        self.SimpulTujuanComboBox.setObjectName(u"SimpulTujuanComboBox")

        self.horizontalLayout_3.addWidget(self.SimpulTujuanComboBox)


        self.verticalLayout.addWidget(self.frame_5)

        self.StartButton = QPushButton(self.LeftFrame)
        self.StartButton.setObjectName(u"StartButton")

        self.verticalLayout.addWidget(self.StartButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.LeftFrame)

        self.FrameFigure = QFrame(self.centralwidget)
        self.FrameFigure.setObjectName(u"FrameFigure")
        self.FrameFigure.setFrameShape(QFrame.StyledPanel)
        self.FrameFigure.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.FrameFigure)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.FileNameLabel.setText(QCoreApplication.translate("MainWindow", u"Masukkan File Konfigurasi", None))
        self.FileBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.SimpulAsalLabel.setText(QCoreApplication.translate("MainWindow", u"Simpul Asal", None))
        self.SimpulTujuanLabel.setText(QCoreApplication.translate("MainWindow", u"Simpul Tujuan", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi


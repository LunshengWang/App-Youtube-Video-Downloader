# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'App - Youtube Video Downloader.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from pytube import YouTube
from urllib import request
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon("resources/ytdl.png"))
        MainWindow.resize(640, 480)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setWindowOpacity(4.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ytUrlLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ytUrlLabel.setFont(font)
        self.ytUrlLabel.setObjectName("ytUrlLabel")
        self.horizontalLayout.addWidget(self.ytUrlLabel)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.loadUrlButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.loadUrlButton.setFont(font)
        self.loadUrlButton.setObjectName("loadUrlButton")
        self.loadUrlButton.clicked.connect(self.clickLoadUrlButton)
        self.horizontalLayout.addWidget(self.loadUrlButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.saveDirLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.saveDirLabel.setFont(font)
        self.saveDirLabel.setObjectName("saveDirLabel")
        self.horizontalLayout_2.addWidget(self.saveDirLabel)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.browseButton.setFont(font)
        self.browseButton.setObjectName("browseButton")
        self.browseButton.clicked.connect(self.clickBrowseButton)
        self.horizontalLayout_2.addWidget(self.browseButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.videoListLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.videoListLabel.setFont(font)
        self.videoListLabel.setObjectName("videoListLabel")
        self.horizontalLayout_3.addWidget(self.videoListLabel)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.activated.connect(self.itemSelect)
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.dloadButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.dloadButton.setFont(font)
        self.dloadButton.setObjectName("dloadButton")
        self.dloadButton.clicked.connect(self.clickDloadButton)
        self.horizontalLayout_3.addWidget(self.dloadButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.progressLabel.setFont(font)
        self.progressLabel.setObjectName("progressLabel")
        self.verticalLayout.addWidget(self.progressLabel)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.aboutLabel = QtWidgets.QLabel(self.centralwidget)
        self.aboutLabel.setText("")
        self.aboutLabel.setObjectName("aboutLabel")
        self.verticalLayout.addWidget(self.aboutLabel)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.clickExit)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.clickAbout)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.dstream = '' # Initialized it as string first to avoid crash when clicking Download button without any stream

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "App - Youtube Video Downloader"))
        self.ytUrlLabel.setText(_translate("MainWindow", "Youtube URL: "))
        self.lineEdit.setText(_translate("MainWindow", "Please paste your youtbue url here"))
        self.loadUrlButton.setText(_translate("MainWindow", "Load URL"))
        self.saveDirLabel.setText(_translate("MainWindow", "Save Directory: "))
        home = os.path.expanduser('~') # os.getcwd() # current dir
        self.lineEdit_2.setText(home)
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.videoListLabel.setText(_translate("MainWindow", "Video List: "))
        self.dloadButton.setText(_translate("MainWindow", "Download"))
        self.progressLabel.setText(_translate("MainWindow", "Progress: "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit app"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About app"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+B"))

    def downloadProgress(self, stream, chunk, bytes_remaining):
        downloadPercent = int((stream.filesize - bytes_remaining) / stream.filesize * 100)
        self.progressBar.setProperty("value", downloadPercent)

    def clickLoadUrlButton(self):
        url = self.lineEdit.text()
        # Make sure that it is a valid url
        try:
            request.urlopen(url)
            self.aboutLabel.clear()
        except Exception as e:
            self.aboutLabel.setText(url + " is not a valid url, please make sure to paste a valid one")
            return

        yt = YouTube(url, on_progress_callback=self.downloadProgress) # How to know it is successful?
        self.videoList = yt.streams.filter(progressive=True).order_by('resolution').all()
        initialized = False
        for vl in self.videoList:
            if not initialized:
                self.dstream = vl # Set to 1st stream as the default
                initialized = True
            item = vl.mime_type + "\t" + vl.resolution
            self.comboBox.addItem(item)

    def itemSelect(self, i): # Select which stream to download
        item = self.comboBox.currentText()
        for vl in self.videoList:
            if vl.mime_type + "\t" + vl.resolution == item:
                self.dstream = vl
                self.aboutLabel.clear()

    def clickBrowseButton(self):
        oldPath = self.lineEdit_2.text() # Currently directory
        newPath = QFileDialog.getExistingDirectory(self.centralwidget, "Browse a directory", oldPath)
        if os.path.isdir(newPath): # Only if it is a valid directory
            self.lineEdit_2.setText(newPath)

    def clickDloadButton(self):
        # Check if it is valid stream:
        if type(self.dstream).__name__ != 'Stream':
            self.aboutLabel.setText("Not a valid stream, please select a valid one")
            return
        savePath = self.lineEdit_2.text()
        self.dstream.download(savePath)

    def clickExit(self):
        QCoreApplication.instance().quit()

    def clickAbout(self):
        self.aboutLabel.setText("Copyright (C) 2021 Alan Wang <lunsheng.wang@protonmail.com>")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

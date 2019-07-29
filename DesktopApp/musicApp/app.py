from PyQt5 import QtCore, QtGui, QtWidgets
import os, time
import pygame
import mutagen
import threading
pygame.mixer.init()

songs = os.listdir('songs/')
# print(songs)

class Ui_MainWindow(object):
    labelX = 661
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1226, 781)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 290, 561, 411))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 411, 391))
        self.listWidget.setObjectName("listWidget")

        for i in range(len(songs)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
            item.setText(songs[i])

        self.listWidget_2 = QtWidgets.QListWidget(self.frame)
        self.listWidget_2.setGeometry(QtCore.QRect(430, 10, 121, 391))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 220, 381, 61))
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(770, 220, 381, 61))
        self.label_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(650, 290, 561, 411))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 541, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(450, 140, 701, 61))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 140, 71, 61))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-image: url('next_icon.png');")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 140, 71, 61))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-image: url('prev_icon.png');")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 140, 71, 61))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("background-image: url('stop_icon.png');")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 140, 71, 61))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4.setStyleSheet("background-image: url('play_icon.png');")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 160, 61, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1170, 160, 61, 19))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 90, self.labelX, 41))
        self.label_5.setStyleSheet("font: 55 16pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 10, 621, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(790, 10, 251, 61))
        self.pushButton_5.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1221, 741))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 1221, 721))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(300, 50, 711, 91))
        self.label_7.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";color:#fff;background"
                                   "-color:transparent;")
        self.label_7.setObjectName("label_7")

        self.img = QtGui.QPixmap('bg_1.jpg')
        self.label_6.setPixmap(self.img)

        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setGeometry(QtCore.QRect(420, 550, 311, 91))
        self.pushButton_6.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1226, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_Playlist = QtWidgets.QAction(MainWindow)
        self.actionSave_Playlist.setObjectName("actionSave_Playlist")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_Playlist)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Featured Songs"))
        self.label_2.setText(_translate("MainWindow", "My Playlist"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "SongName"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Action"))
        self.label_3.setText(_translate("MainWindow", "00:00"))
        self.label_4.setText(_translate("MainWindow", "00:00"))
        self.label_5.setText(_translate("MainWindow", "Currently Playing : "))
        self.pushButton_5.setText(_translate("MainWindow", "Search"))
        self.label_7.setText(_translate("MainWindow", "Welcome to My JukeBox"))
        self.pushButton_6.setText(_translate("MainWindow", "Go Inside"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_Playlist.setText(_translate("MainWindow", "Save Playlist"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

        self.pushButton_6.clicked.connect(self.frame_3.hide)
        self.listWidget.itemClicked.connect(self.selectSong)
        self.pushButton_4.clicked.connect(self.playSong)
        self.pushButton.clicked.connect(self.nextSong)
        self.pushButton_2.clicked.connect(self.prevSong)
        self.pushButton_3.clicked.connect(self.stopSong)

        # self.horizontalSlider.sliderPressed.connect(self.changeValue)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setDisabled(True)

    def selectSong(self,item):
        self.currentSong = item.text()

    def playSong(self):
        try:
            self.label_5.setText("Currently Playing : {}".format(self.currentSong))
            self.horizontalSlider.setDisabled(False)

            path = 'songs/' + self.currentSong
            self.horizontalSlider.setValue(0)
            songFile = mutagen.File(path)
            songLength = songFile.info.length
            self.horizontalSlider.setMaximum(songLength)
            # print(self.label_5.x())
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            t = threading.Thread(target=self.changeSongPosition)
            t.start()

        except BaseException as ex:
            print(ex)

    def nextSong(self):
        print("Next")
        index = songs.index(self.currentSong)
        self.currentSong = songs[index + 1]
        self.playSong()

    def prevSong(self):
        print("Prev")
        index = songs.index(self.currentSong)
        self.currentSong = songs[index - 1]
        self.playSong()

    def stopSong(self):
        print("stop")

    def changeValue(self):
        print("Position Changed...")
        currentValue = self.horizontalSlider.value()
        pygame.mixer.music.set_pos(currentValue)

    def changeSongPosition(self):
        while True:
            print("Changing Position")
            time.sleep(1)
            songPos = pygame.mixer.music.get_pos()
            seconds = songPos/1000
            # print(seconds)
            self.horizontalSlider.setValue(seconds)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

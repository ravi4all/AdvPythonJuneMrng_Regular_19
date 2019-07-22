from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1190, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 10, 321, 71))
        self.label.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 28, 8);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 200, 511, 71))
        self.label_2.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 28, 8);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 340, 511, 71))
        self.label_3.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 28, 8);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(640, 200, 421, 81))
        self.lineEdit.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(640, 330, 421, 81))
        self.lineEdit_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(640, 460, 421, 81))
        self.lineEdit_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 470, 511, 71))
        self.label_4.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 28, 8);")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 590, 161, 101))
        self.pushButton.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 590, 161, 101))
        self.pushButton_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 590, 161, 101))
        self.pushButton_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(890, 590, 161, 101))
        self.pushButton_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1190, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Basic Calculator"))
        self.label_2.setText(_translate("MainWindow", "Enter First Number"))
        self.label_3.setText(_translate("MainWindow", "Enter Second Number"))
        self.label_4.setText(_translate("MainWindow", "Result"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.pushButton_3.setText(_translate("MainWindow", "*"))
        self.pushButton_4.setText(_translate("MainWindow", "/"))

        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.sub)
        self.pushButton_3.clicked.connect(self.mul)
        self.pushButton_4.clicked.connect(self.div)
        self.lineEdit_3.setReadOnly(True)

    def add(self):
        f_num = int(self.lineEdit.text())
        s_num = int(self.lineEdit_2.text())
        result = f_num + s_num
        self.lineEdit_3.setText(str(result))

    def sub(self):
        f_num = int(self.lineEdit.text())
        s_num = int(self.lineEdit_2.text())
        result = f_num - s_num
        self.lineEdit_3.setText(str(result))

    def mul(self):
        f_num = int(self.lineEdit.text())
        s_num = int(self.lineEdit_2.text())
        result = f_num * s_num
        self.lineEdit_3.setText(str(result))

    def div(self):
        f_num = int(self.lineEdit.text())
        s_num = int(self.lineEdit_2.text())
        result = f_num / s_num
        self.lineEdit_3.setText(str(result))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

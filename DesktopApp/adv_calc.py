from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 10, 761, 81))
        self.lineEdit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 220, 111, 81))
        self.pushButton.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 220, 111, 81))
        self.pushButton_2.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 220, 111, 81))
        self.pushButton_3.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 330, 111, 81))
        self.pushButton_4.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 330, 111, 81))
        self.pushButton_5.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(240, 330, 111, 81))
        self.pushButton_6.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 450, 111, 81))
        self.pushButton_7.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(430, 450, 111, 81))
        self.pushButton_8.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(240, 450, 111, 81))
        self.pushButton_9.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(60, 560, 111, 81))
        self.pushButton_10.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(430, 560, 111, 81))
        self.pushButton_11.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(240, 560, 111, 81))
        self.pushButton_12.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(710, 560, 111, 81))
        self.pushButton_13.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(710, 220, 111, 81))
        self.pushButton_14.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(710, 450, 111, 81))
        self.pushButton_15.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(710, 330, 111, 81))
        self.pushButton_16.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(710, 120, 111, 81))
        self.pushButton_17.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(430, 120, 111, 81))
        self.pushButton_18.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 10px 10px black;")
        self.pushButton_18.setObjectName("pushButton_18")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 31))
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
        self.pushButton.setText(_translate("MainWindow", "7"))
        self.pushButton_2.setText(_translate("MainWindow", "8"))
        self.pushButton_3.setText(_translate("MainWindow", "9"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "6"))
        self.pushButton_6.setText(_translate("MainWindow", "5"))
        self.pushButton_7.setText(_translate("MainWindow", "1"))
        self.pushButton_8.setText(_translate("MainWindow", "3"))
        self.pushButton_9.setText(_translate("MainWindow", "2"))
        self.pushButton_10.setText(_translate("MainWindow", "."))
        self.pushButton_11.setText(_translate("MainWindow", "^"))
        self.pushButton_12.setText(_translate("MainWindow", "0"))
        self.pushButton_13.setText(_translate("MainWindow", "/"))
        self.pushButton_14.setText(_translate("MainWindow", "+"))
        self.pushButton_15.setText(_translate("MainWindow", "*"))
        self.pushButton_16.setText(_translate("MainWindow", "-"))
        self.pushButton_17.setText(_translate("MainWindow", "="))
        self.pushButton_18.setText(_translate("MainWindow", "C"))

        self.lineEdit.setReadOnly(True)

        self.btns = [self.pushButton,self.pushButton_2,self.pushButton_3,
                     self.pushButton_4, self.pushButton_5, self.pushButton_6,
                     self.pushButton_7, self.pushButton_8, self.pushButton_9,
                     self.pushButton_12]
        self.oprs = [self.pushButton_13,self.pushButton_14,
                     self.pushButton_15,self.pushButton_16]
        self.pushButton_17.clicked.connect(self.evaluate)
        for i in range(len(self.btns)):
            self.btns[i].clicked.connect(self.appendValues)

        for i in range(len(self.oprs)):
            self.oprs[i].clicked.connect(self.appendOperators)

    def appendValues(self):
        self.expression = ''
        try:
            btn = self.sender()
            x = btn.text()
            text = self.lineEdit.text()
            text += x
            self.lineEdit.setText(text)
            self.expression = self.lineEdit.text()
        except BaseException as ex:
            print(ex)

    def appendOperators(self):
        try:
            btn = self.sender()
            x = btn.text()
            oprs = ['+','-','/','*']
            text = self.lineEdit.text()
            text += x
            # print(text[-1])

            for i in range(len(oprs)):
                if oprs[i] == text[-1] and x in oprs:
                    text = self.expression + x
                    break

            self.lineEdit.setText(text)

        except BaseException as ex:
            print(ex)

    def evaluate(self):
        result = eval(self.expression)
        self.lineEdit.setText(str(result))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

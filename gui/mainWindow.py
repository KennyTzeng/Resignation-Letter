# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 350)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.poseImage = QtWidgets.QGraphicsView(self.centralwidget)
        self.poseImage.setGeometry(QtCore.QRect(250, 70, 200, 200))
        self.poseImage.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.poseImage.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.poseImage.setObjectName("poseImage")
        self.seeyouTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.seeyouTextLabel.setGeometry(QtCore.QRect(350, 35, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.seeyouTextLabel.setFont(font)
        self.seeyouTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.seeyouTextLabel.setObjectName("seeyouTextLabel")
        self.approveButton = QtWidgets.QPushButton(self.centralwidget)
        self.approveButton.setGeometry(QtCore.QRect(230, 290, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.approveButton.setFont(font)
        self.approveButton.setObjectName("approveButton")
        self.denyButton = QtWidgets.QPushButton(self.centralwidget)
        self.denyButton.setGeometry(QtCore.QRect(370, 290, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.denyButton.setFont(font)
        self.denyButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.denyButton.setCheckable(False)
        self.denyButton.setChecked(False)
        self.denyButton.setAutoDefault(False)
        self.denyButton.setDefault(False)
        self.denyButton.setFlat(False)
        self.denyButton.setObjectName("denyButton")
        self.greetingTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.greetingTextLabel.setGeometry(QtCore.QRect(60, 30, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.greetingTextLabel.setFont(font)
        self.greetingTextLabel.setObjectName("greetingTextLabel")
        self.resignerTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.resignerTextLabel.setGeometry(QtCore.QRect(550, 230, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resignerTextLabel.setFont(font)
        self.resignerTextLabel.setObjectName("resignerTextLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resignation Confirmation Letter"))
        self.seeyouTextLabel.setText(_translate("MainWindow", "See ya!"))
        self.approveButton.setText(_translate("MainWindow", "Approve"))
        self.denyButton.setText(_translate("MainWindow", "Deny"))
        self.greetingTextLabel.setText(_translate("MainWindow", "Dear Supervisors,"))
        self.resignerTextLabel.setText(_translate("MainWindow", "Resigner: me"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

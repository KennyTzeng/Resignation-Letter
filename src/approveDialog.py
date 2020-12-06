import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import gui.approveDialog as ui

class ApproveDialog(QtWidgets.QDialog, ui.Ui_approveDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # set dialog icon
        self.setWindowIcon(QtGui.QIcon('images/green-ok-24.png'))

        # set fixed dialog size
        self.setFixedSize(self.width(), self.height())

        # register exitButton handler
        self.exitPushButton.clicked.connect(self.exitButtonHandler)

    def closeEvent(self, event):
        # ignore exit event of this dialog
        event.ignore()

    def exitButtonHandler(self):
        sys.exit(0)


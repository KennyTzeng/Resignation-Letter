from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import gui.nowayDialog as ui

class NowayDialog(QtWidgets.QDialog, ui.Ui_nowayDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # set dialog icon
        self.setWindowIcon(QtGui.QIcon('images/warning.png'))

        # set fixed dialog size
        self.setFixedSize(self.width(), self.height())

        # load X-mark image
        pixmap = QtGui.QPixmap("images/x-mark-3-40.png")
        pixmap = pixmap.scaled(self.xmarkGraphicsView.width(), self.xmarkGraphicsView.height(), QtCore.Qt.IgnoreAspectRatio)
        pixmapItem = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene = QtWidgets.QGraphicsScene(self)
        scene.addItem(pixmapItem)
        self.xmarkGraphicsView.setScene(scene)

        # register okButton handler
        self.okPushButton.clicked.connect(self.okButtonHandler)

    def okButtonHandler(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    nowayDialog = NowayDialog()
    nowayDialog.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-
import sys, random
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import gui.mainWindow as ui

class Application(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # set window icon
        self.setWindowIcon(QtGui.QIcon('images/letter.png'))

        # load image
        pixmap = QtGui.QPixmap(self.getPoseImageFilepath())
        pixmap = pixmap.scaled(self.poseImage.width(), self.poseImage.height(), QtCore.Qt.IgnoreAspectRatio)
        pixmapItem = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene = QtWidgets.QGraphicsScene(self)
        scene.addItem(pixmapItem)
        self.poseImage.setScene(scene)

    def getPoseImageFilepath(self):
        path = "images/"
        images = ["pose1.jpg", "pose2.jpg"]

        return "%s%s"%(path, images[random.randint(0, len(images) - 1)])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())

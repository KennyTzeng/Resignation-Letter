# -*- coding: utf-8 -*-
import sys, random
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import gui.mainWindow as ui
from src.denyButton import DenyButton
import src.global_def as g

class MainWindow(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # set window icon
        self.setWindowIcon(QtGui.QIcon('images/letter.png'))

        # set fixed window size
        self.setFixedSize(g.WINDOW_WIDTH, g.WINDOW_HEIGHT)

        # load image
        pixmap = QtGui.QPixmap(self.getPoseImageFilepath())
        pixmap = pixmap.scaled(self.poseImage.width(), self.poseImage.height(), QtCore.Qt.IgnoreAspectRatio)
        pixmapItem = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene = QtWidgets.QGraphicsScene(self)
        scene.addItem(pixmapItem)
        self.poseImage.setScene(scene)

        # replace denyButton to customized one
        denyBtn = DenyButton(self.centralwidget)
        placeholderBtn = self.denyButton
        denyBtn.setGeometry(QtCore.QRect(placeholderBtn.x(), placeholderBtn.y(), placeholderBtn.width(), placeholderBtn.height()))
        denyBtn.setFont(placeholderBtn.font())
        denyBtn.setObjectName(placeholderBtn.objectName())
        denyBtn.setText(placeholderBtn.text())
        denyBtn.setStyleSheet(placeholderBtn.styleSheet())
        self.denyButton = denyBtn
        placeholderBtn.deleteLater()

    def getPoseImageFilepath(self):
        path = "images/"
        images = ["pose1.jpg", "pose2.jpg"]

        return "%s%s"%(path, images[random.randint(0, len(images) - 1)])


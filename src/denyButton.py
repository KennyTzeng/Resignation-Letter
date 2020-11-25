import random
from PyQt5 import QtWidgets, QtCore, QtGui
import src.global_def as g

class DenyButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEnabled(False)

    def enterEvent(self, event):
        self.moveRandomly()

    def moveRandomly(self):
        new_x = random.randint(g.PADDING, g.WINDOW_WIDTH - g.PADDING - self.width())
        new_y = random.randint(g.PADDING, g.WINDOW_HEIGHT - g.PADDING - self.height())
        self.setGeometry(QtCore.QRect(new_x, new_y, self.width(), self.height()))
    

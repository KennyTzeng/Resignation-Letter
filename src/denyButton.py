import random, threading
from PyQt5 import QtWidgets, QtCore, QtGui
import lib.global_def as g
from lib.logger import DEBUG_PRINT

class DenyButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEnabled(False)
        self.lock = False

    def enterEvent(self, event):
        self.moveRandomly()

        # narrow
        if random.random() < 0.20 and not self.lock:
            self.lock = True
            DEBUG_PRINT("%s locked" % self.objectName())
            current_width, current_height = self.width(), self.height()
            current_font_size = self.font().pointSize()
            self.setGeometry(self.x(), self.y(), current_width * 0.2, current_height * 0.2)
            font = self.font()
            font.setPointSize(current_font_size * 0.2)
            self.setFont(font)
            threading.Timer(1, self.cb_narrow, [current_width, current_height, current_font_size]).start()

#        elif random.random() < 0.20 and not self.lock:
#           self.lock = True

    def moveRandomly(self):
        new_x = random.randint(g.PADDING, g.WINDOW_WIDTH - g.PADDING - self.width())
        new_y = random.randint(g.PADDING, g.WINDOW_HEIGHT - g.PADDING - self.height())
        self.setGeometry(QtCore.QRect(new_x, new_y, self.width(), self.height()))

    def cb_narrow(self, origin_width, origin_height, origin_font_size):
        self.setGeometry(self.x(), self.y(), origin_width, origin_height)
        font = self.font()
        font.setPointSize(origin_font_size)
        self.setFont(font)
        self.lock = False
        DEBUG_PRINT("%s unlocked" % self.objectName())
    
#    def cb_disappear(self):


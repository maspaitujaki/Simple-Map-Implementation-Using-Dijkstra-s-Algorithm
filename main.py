import sys
import os
import datetime
import hashlib
from PySide2 import QtGui
from matplotlib import pyplot as plt
from qt_material import *
from ui_ui import QTableWidgetItem, QAbstractItemView, QMainWindow, Ui_MainWindow, QGraphicsDropShadowEffect, QIntValidator, QApplication


class MainWindow(QMainWindow):
    """
    Kelas MainWindow untuk menjalankan program
    """

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Change title
        self.setWindowTitle("Dikjstra")

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import PyQt5
from PyQt5 import QtWidgets, QtGui, QtCore
from MainWindow import Ui_MainWindow
import sys
import random
from TreeBin import Node, BinaryTree



class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tree = BinaryTree()

        self.scene = QtWidgets.QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.scale = 0.8
        self.ui.graphicsView.scale(self.scale, self.scale)
        self.ui.pushButton.clicked.connect(self.AddEl)
        self.ui.pushButton_2.clicked.connect(self.DelEl)
        self.ui.pushButton_4.clicked.connect(self.Clear)
        self.ui.pushButton_5.clicked.connect(self.Generate)

    def AddEl(self):
        self.tree.AddNode(int(self.ui.spinBox.text()))
        self.scene.clear()
        self.PaintT()

    def DelEl(self):
        self.tree.DeleteNode(int(self.ui.spinBox_2.text()))
        self.scene.clear()
        self.PaintT()

    def Clear(self):
        self.scene.clear()
        self.tree.Clear()
        self.PaintT()

    def Generate(self):
        self.scene.clear()
        self.tree.GenerateTree()
        self.PaintT()

    def PaintT(self):
        self.ui.label_5.setText(str(self.tree.count))
        self.ui.label_7.setText(str(self.tree.lvlCount))
        self.tree.paint(self.scene, self.scale, self.tree.root)



app = QtWidgets.QApplication([])
application = myWindow()
application.show()

sys.exit(app.exec())


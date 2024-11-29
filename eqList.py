from PyQt5.QtWidgets import (
    QListWidget,
)

class eqList(QListWidget):
    def __init__(self, parent=None):
        super(QListWidget, self).__init__(parent)

    def removeSelectedItem(self):
        self.currentSelectedItem = self.currentRow()
        self.takeItem(self.currentSelectedItem)
        
from PyQt5.QtWidgets import QPushButton

class IconButton(QPushButton):
    def __init__(self, icon):
        super().__init__()

        self.icon = icon

        self.initUI()
    
    def initUI(self):
        self.setIcon(self.style().standardIcon(self.icon))
        
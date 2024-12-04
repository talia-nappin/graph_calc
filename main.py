import sys
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
from vtkmodules.vtkCommonColor import vtkNamedColors
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonCore import vtkMinimalStandardRandomSequence
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.qt.QVTKRenderWindowInteractor import  QVTKRenderWindowInteractor

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
    QFrame,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QMainWindow,
    QGridLayout,
    QSpinBox,
    QStyle,
    QPushButton
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import Qt

from eqList import EqList
from iconButton import IconButton

colors = vtkNamedColors()

cone = vtkConeSource()
cone.SetHeight(3.0)
cone.SetRadius(1.0)
cone.SetResolution(100)

coneMapper = vtkPolyDataMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())

coneActor = vtkActor()
coneActor.SetMapper(coneMapper)
coneActor.GetProperty().SetColor(colors.GetColor3d('MistyRose'))

dockIcons = [
    QStyle.SP_MessageBoxInformation,
    QStyle.SP_MessageBoxQuestion
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'graph_calc'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        self.infoButton, self.helpButton = [IconButton  (icon) for icon in dockIcons]

        self.eqList = EqList()
        self.eqList.itemDoubleClicked.connect(self.editListItem)

        self.digitBox = QSpinBox()

        self.frame = QFrame()
        self.vl = QVBoxLayout()
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.vl.addWidget(self.vtkWidget)

        self.renderer = vtkRenderer()
        self.renwin = self.vtkWidget.GetRenderWindow()
        self.renwin.AddRenderer(self.renderer)
        self.iren = self.renwin.GetInteractor()

        self.renderer.SetBackground(.3, .4, .5 )
        self.renderer.AddActor(coneActor)

        self.renderer.ResetCamera()

        self.frame.setLayout(self.vl)

        self.layout = QGridLayout()
        self.layout.addWidget(self.eqList, 0, 0, 2, 1)
        self.layout.addWidget(self.frame, 1, 1, 2, 2)
        self.layout.addWidget(self.digitBox, 2, 0)
        self.layout.addWidget(self.infoButton, 0, 1)
        self.layout.addWidget(self.helpButton, 0, 2)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.iren.Initialize()



    def keyPressEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            if event.key() == Qt.Key_N:
                dlg = NewGraphDialog()
                if dlg.exec():
                    self.eqList.addItem(dlg.textbox.text())
                    if self.eqList.count() == 1:
                        self.eqList.setCurrentRow(0)
            elif event.key() == Qt.Key_W:
                self.eqList.removeSelectedItem()
            elif event.key() == Qt.Key_E:
                if self.eqList.count() > 0:
                 self.editListItem(self.eqList.currentItem())

    @pyqtSlot()
    def openHelp():
        print('HELP!!!')

    def editListItem(self, selectedItem):
        dlg = NewGraphDialog()
        dlg.textbox.setText(selectedItem.text().strip())
        if dlg.exec():
            selectedItem.setText(dlg.textbox.text().strip())

class NewGraphDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "New graph"
        self.left = 100
        self.top = 100
        self.width = 340
        self.height = 60
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QLineEdit(self)
        self.textbox.move(10, 10)
        self.textbox.resize(320,40)
        self.textbox.returnPressed.connect(lambda:self.accept())

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
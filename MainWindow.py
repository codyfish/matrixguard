import threading
from time import sleep

from PyQt5 import QtWidgets, uic
from MatrixWidget import MatrixWidget
from PyQt5.QtCore import pyqtSlot
from sympy import Matrix
import sys
from sympy.parsing.sympy_parser import parse_expr

from CalculationRow import CalculationRow
from Operations import Id, Scalar, ScalarRow, SwitchRow, AddRow
import dialogs.Dialogs as Dialogs


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  # Call the inherited classes __init__ method

        uic.loadUi('main-window.ui', self)  # Load the .ui file

        self._scroll_lock = threading.Lock()

        self._scroll_area = self.findChild(QtWidgets.QScrollArea, 'scroll_area')
        self._scroll_area_content = self.findChild(QtWidgets.QWidget, 'scroll_area_content')
        self._calculation_layout = QtWidgets.QVBoxLayout()
        self._scroll_area_content.setLayout(self._calculation_layout)

        button_switch_row = self.findChild(QtWidgets.QPushButton, 'button_switch_row')
        button_scalar_row = self.findChild(QtWidgets.QPushButton, 'button_scalar_row')
        button_scalar_all = self.findChild(QtWidgets.QPushButton, "button_scalar_all")
        button_add_row = self.findChild(QtWidgets.QPushButton, "button_add_row")
        button_add_matrix_d = self.findChild(QtWidgets.QPushButton, "button_add_matrix_d")

        button_switch_row.clicked.connect(self.c_switch_row)
        button_scalar_row.clicked.connect(self.c_scalar_row)
        button_scalar_all.clicked.connect(self.c_scalar_all)
        button_add_row.clicked.connect(self.c_add_row)
        button_add_matrix_d.clicked.connect(self.c_add_matrix)

        # matrix = Matrix([[1 for x in range(5)] for y in range(4)])
        # self._current_crow = CalculationRow(matrix)
        # self._calculation_layout.addWidget(self._current_crow)

        self.show()  # Show the GUI

    def scroll_down(self):
        scroller = ScrollThread(self._scroll_lock, self._scroll_area.verticalScrollBar())
        scroller.start()

    def add_operation(self, operation):
        self._current_crow.add_operation(operation)
        matrix = self._current_crow.get_matrix_result()
        self._current_crow = CalculationRow(matrix)
        self._calculation_layout.addWidget(self._current_crow)
        self.scroll_down()

    @pyqtSlot()
    def c_switch_row(self):
        print("switch rows")
        dialog = Dialogs.SwitchRowsDialog()
        if dialog.exec():
            print(dialog.row1)
            operation = SwitchRow(dialog.row1, dialog.row2)
            self.add_operation(operation)

    @pyqtSlot()
    def c_scalar_row(self):
        print("scalar row")
        dialog = Dialogs.ScalarRowDialog()
        if dialog.exec():
            print(dialog.expr)
            operation = ScalarRow(dialog.row, dialog.expr)
            self.add_operation(operation)

    @pyqtSlot()
    def c_scalar_all(self):
        print("scalar all")
        dialog = Dialogs.ScalarAllDialog()
        if dialog.exec():
            print(dialog.expr)
            operation = Scalar(dialog.expr)
            self.add_operation(operation)

    @pyqtSlot()
    def c_add_row(self):
        print("add row")
        dialog = Dialogs.AddRowDialog()
        if dialog.exec():
            print(dialog.expr)
            operation = AddRow(dialog.source, dialog.target, dialog.expr)
            self.add_operation(operation)

    @pyqtSlot()
    def c_add_matrix(self):
        dialog = Dialogs.AddMatrixDialog()
        if dialog.exec():
            self._current_crow = CalculationRow(dialog.matrix)
            self._calculation_layout.addWidget(self._current_crow)
            self.scroll_down()


class ScrollThread(threading.Thread):
    def __init__(self, lock, scrollbar):
        super().__init__()
        self._lock = lock
        self._scrollbar = scrollbar

    def run(self) -> None:
        sleep(0.1)
        self._lock.acquire()
        self._scrollbar.triggerAction(QtWidgets.QAbstractSlider.SliderToMaximum)
        self._lock.release()

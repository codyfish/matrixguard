from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from sympy.parsing.sympy_parser import parse_expr
from sympy import Matrix


class ScalarAllDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("dialogs/dialog_scalar_all.ui", self)
        self.expr = 0

        self.ui.buttonBox.accepted.connect(self.on_ok)
        self.ui.buttonBox.rejected.connect(self.on_cancel)

    @pyqtSlot()
    def on_ok(self):
        text = self.ui.scalar_edit.text()
        self.expr = parse_expr(text)
        self.accept()

    @pyqtSlot()
    def on_cancel(self):
        self.reject()


class ScalarRowDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("dialogs/dialog_scalar_row.ui", self)
        self.expr = 0
        self.row = 0

        self.ui.buttonBox.accepted.connect(self.on_ok)
        self.ui.buttonBox.rejected.connect(self.on_cancel)

    @pyqtSlot()
    def on_ok(self):
        text = self.ui.scalar_edit.text()
        self.row = int(self.ui.row_edit.text())
        self.expr = parse_expr(text)
        self.accept()

    @pyqtSlot()
    def on_cancel(self):
        self.reject()


class SwitchRowsDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("dialogs/dialog_switch_rows.ui", self)
        self.row1 = 0
        self.row2 = 0

        self.ui.buttonBox.accepted.connect(self.on_ok)
        self.ui.buttonBox.rejected.connect(self.on_cancel)

    @pyqtSlot()
    def on_ok(self):
        self.row1 = int(self.ui.row1_edit.text())
        self.row2 = int(self.ui.row2_edit.text())

        self.accept()

    @pyqtSlot()
    def on_cancel(self):
        self.reject()


class AddRowDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("dialogs/dialog_add_row.ui", self)
        self.expr = 0
        self.source = 0
        self.target = 0

        self.ui.buttonBox.accepted.connect(self.on_ok)
        self.ui.buttonBox.rejected.connect(self.on_cancel)

    @pyqtSlot()
    def on_ok(self):
        text = self.ui.scalar_edit.text()
        self.source = int(self.ui.source_edit.text())
        self.target = int(self.ui.target_edit.text())
        self.expr = parse_expr(text)
        self.accept()

    @pyqtSlot()
    def on_cancel(self):
        self.reject()


class AddMatrixDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("dialogs/dialog_add_matrix.ui",self)
        self.rows = 1
        self.cols = 1

        self.ui.buttonBox.accepted.connect(self.on_ok)
        self.ui.buttonBox.rejected.connect(self.on_cancel)

    @pyqtSlot()
    def on_ok(self):
        self.rows = int(self.ui.row_edit.text())
        self.cols = int(self.ui.col_edit.text())
        self. matrix = Matrix([[0 for c in range(self.cols)] for r in range(self.rows)])
        self.accept()

    @pyqtSlot()
    def on_cancel(self):
        self.reject()

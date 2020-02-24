from PyQt5 import QtWidgets
from sympy.parsing.sympy_parser import parse_expr
from sympy import Matrix
from MatrixWidget import MatrixWidget

from Operations import Id


class CalculationRow(QtWidgets.QWidget):

    def __init__(self, matrix, *args, **kwargs):
        super(QtWidgets.QWidget, self).__init__(*args, **kwargs)

        self._layout = QtWidgets.QHBoxLayout()
        self._matrix_widget = MatrixWidget(matrix)
        self._layout.addWidget(self._matrix_widget)
        self.setLayout(self._layout)

        self._operation = Id()

    def add_operation(self, operation):
        self._operation = operation
        self._layout.addWidget(operation.to_widget())

    def get_matrix_result(self):
        return self._operation.apply(self._matrix_widget.to_matrix())

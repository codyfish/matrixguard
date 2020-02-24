from PyQt5 import QtWidgets
from sympy.parsing.sympy_parser import parse_expr
from sympy import Matrix


class MatrixWidget(QtWidgets.QWidget):

    def __init__(self, init_matrix, *args, **kwargs):
        super(QtWidgets.QWidget, self).__init__(*args, **kwargs)
        self._matrix_grid = QtWidgets.QGridLayout()

        for r in range(init_matrix.rows):
            for c in range(init_matrix.cols):
                self._matrix_grid.addWidget(QtWidgets.QLineEdit(str(init_matrix[r, c])), r, c)

        self.setLayout(self._matrix_grid)

    def to_matrix(self):
        entries = [[]]
        for r in range(self._matrix_grid.rowCount()):
            column = []
            for c in range(self._matrix_grid.columnCount()):
                field = self._matrix_grid.itemAtPosition(r, c).widget()
                value = parse_expr(field.text())
                column.append(value)

            entries.append(column)

        return Matrix(entries)

    def rows(self):
        return self._matrix_grid.rowCount()

    def columns(self):
        return self._matrix_grid.columnCount()

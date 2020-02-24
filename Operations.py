from PyQt5 import QtWidgets
from sympy import eye


class Operation:
    def apply(self, matrix):
        pass

    def to_widget(self):
        pass


class Id(Operation):
    def __init__(self):
        pass

    def apply(self, matrix):
        if len(matrix) == 0:
            return matrix

        return eye(matrix.rows) * matrix

    def to_widget(self):
        return QtWidgets.QLabel("id")


class Scalar(Operation):
    def __init__(self, scalar=1):
        self._scalar = scalar

    def apply(self, matrix):
        if len(matrix) == 0:
            return matrix

        return (eye(matrix.rows) * self._scalar) * matrix

    def to_widget(self):
        return QtWidgets.QLabel(str(self._scalar))


class ScalarRow(Operation):
    def __init__(self, row, scalar=1):
        self._scalar = scalar
        self._row = row

    def apply(self, matrix):
        if len(matrix) == 0:
            return matrix

        trans = eye(matrix.rows)
        trans[self._row, self._row] = self._scalar

        return trans * matrix

    def to_widget(self):
        return QtWidgets.QLabel(str(self._scalar))


class SwitchRow(Operation):
    def __init__(self, row1, row2):
        self._row1 = row1
        self._row2 = row2

    def apply(self, matrix):
        if len(matrix) == 0:
            return matrix

        trans = eye(matrix.rows)
        trans[self._row1, self._row1] = 0
        trans[self._row2, self._row2] = 0
        trans[self._row1, self._row2] = 1
        trans[self._row2, self._row1] = 1

        return trans * matrix

    def to_widget(self):
        return QtWidgets.QLabel(str(self._row1))


class AddRow(Operation):
    def __init__(self, source, target, scalar=1):
        self._source = source
        self._target = target
        self._scalar = scalar

    def apply(self, matrix):
        if len(matrix) == 0:
            return matrix

        trans = eye(matrix.rows)
        trans[self._target, self._source] = self._scalar

        return trans * matrix

    def to_widget(self):
        return QtWidgets.QLabel(str(self._target))

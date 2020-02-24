from sympy import symbols
from sympy import Matrix
import sympy
from PyQt5 import QtWidgets
import sys
import MainWindow
import MatrixWidget

# print(sympy.sqrt(2))

# x, y = symbols('x y')
# expr = x + x + y
# print(expr)

# A = Matrix([[x, 2], [2, 3]])
# print(A.eigenvals())
app = QtWidgets.QApplication(sys.argv)
window = MainWindow.MainWindow()
window.show()

app.exec_()

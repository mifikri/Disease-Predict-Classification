import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QLineEdit, QCompleter
from PyQt5.QtCore import QStringListModel
from PyQt5 import QtCore, QtWidgets, QtGui
import fielddata

def get_data(model):
    model.setStringList(fielddata.l1)

#if __name__ == "__main__":
def auto(edit):
#    app = QApplication(sys.argv)
#    edit = QLineEdit()
    completer = QCompleter()
    completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
    edit.setCompleter(completer)

    model = QStringListModel()
    completer.setModel(model)
    get_data(model)
    return edit
#    edit.show()
#    sys.exit(app.exec_())


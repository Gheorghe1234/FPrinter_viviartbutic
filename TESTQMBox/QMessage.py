from PySide2.QtWidgets import QMessageBox


def dialog_box(self, s):
    dlg = QMessageBox(self)
    # dlg.setIcon(QtWidgets.QMessageBox.Information)
    dlg.setWindowTitle("MessageBox")
    dlg.setText(s)
    dlg.exec_()

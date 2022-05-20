from PyQt5 import QtWidgets
class Alert:
    def __init__(self,msg):
        self.show(msg)

    def show(self,msg):
        dlg = QtWidgets.QMessageBox()
        dlg.setWindowTitle("Thông báo")
        dlg.setText(msg)
        dlg.exec()
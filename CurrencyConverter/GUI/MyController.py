import json
import sys
import requests

from GUI import MyModel
from GUI import Currency
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyController(QMainWindow):

    def __init__(self, parent=None):
        """
        mittels MyForm greife auf meine Buttons zu.
        PushButton_3: Buttonname, Wenn ich aufs Button geklickt habe, erstelle ich eine Verbindung zur Methode .
        :param parent:
        """
        super().__init__(parent)
        self.myForm = Currency.Ui_Form()
        self.myForm.setupUi(self)
        self.myModel=MyModel.MyModel()
        self.myForm.pushButton_3.clicked.connect(self.getCur)
        self.myForm.pushButton.clicked.connect(self.clear)


    def getCur(self):
        """
        Die Methode getCur greift auf die zwei lineEdits und doubleSpinBox zu
        :return:
        """
        from_c = self.myForm.lineEdit.text()
        to_c = self.myForm.lineEdit_2.text()
        input = self.myForm.doubleSpinBox.value()

        if(self.myForm.checkBox.isChecked()):
            g=self.myModel.get_cur(from_c,to_c,input)
        else:
            g=self.myModel.get_cur_offline(from_c,to_c,input)
        self.myForm.textEdit.setText(g)


    def clear(self):
        """
        Die Methode clear() greift auf die zwei lineEdits zu und setzt die beiden auf 0, wenn ich das Button tätige.
        :return:
        """
        self.myForm.lineEdit.setText(" ")
        self.myForm.lineEdit_2.setText(" ")
        self.myForm.doubleSpinBox.setValue(0.00)

# Main-Methode
if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())

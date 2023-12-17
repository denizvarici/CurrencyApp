from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow
import API


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnCalculate.clicked.connect(self.Calculate)

    def Calculate(self):
        try:
            amount = int(self.ui.tbxAmount.text())
            exchangeCurrency = self.ui.cbxExchange.currentText()
            buyCurrency = self.ui.cbxBuy.currentText()
            
            


            rate = API.bringCurrentRates(exchangeCurrency,buyCurrency)
            
            self.ui.lblResult.setText(f"{amount} {exchangeCurrency} = {amount*rate} {buyCurrency}")

        except:
            self.ui.lblResult.setText("Lütfen tüm alanları doldurun!")


def App():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())


App()
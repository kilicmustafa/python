import sys

from PyQt5 import QtWİdgets

def pencere():

    app = QtWidgets.QApplication(sys.argv)
    
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Pencere Baslığı")
    pencere.setGeometry(100 , 100 ,500 ,500)

    etiket = QtWidgets.Label(pencere)
    etiket.setText("Merhaba Dünya")
    etiket.move(200 ,30)

    buton = QtWidgets.QPushButton(pencere)
    buton.setText("Burası bir butondur")
    button.move(180 ,80)
    
    pencere.show()

    sys_exit(app.exec_())



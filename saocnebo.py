from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton, QCheckBox, QRadioButton, QMessageBox, QCheckBox

import sys
class MyWindow(QWidget):

    def dzebna(self):
        if not self.tanxmoba.isChecked():
            QMessageBox.warning(self, 'ყურადღება!', "ჯერ დაეთანხმე წესებს")
            return
        qveyana = self.qveyana.currentText()
        biujeti = self.biujeti.currentText()
        cilindrebi = self.cilindrebi.currentText()

        if self.transformeri.isChecked():
            QMessageBox.warning(self, "შორს ლიბერასტები", "ეგეც შენი ამერიკა და ევროპა! ან კაცი აირჩიე ან ქალი, ნუ გარყვენით ჩემი PyQt5-ის პროგრამა, დატოვეთ რამე წმინდა! ")
            return
        if qveyana == 'იტალია' and cilindrebi == '6' and biujeti == '50k-100K$':
            manqana = 'Alfa Romeo Giulia Quadrifoglio'
        elif qveyana == 'იტალია' and cilindrebi == '6' and biujeti == '100K-500k$':
            manqana = 'Lancia Stratos'
        elif qveyana == 'იტალია' and cilindrebi == '6' and biujeti == '500K-2M$':
            manqana = 'Ferrari Dino 246 GT'
        elif qveyana == 'იტალია' and cilindrebi == '8' and biujeti == '50k-100K$':
            manqana = 'Maserati GranSport'
        elif qveyana == 'იტალია' and cilindrebi == '8' and biujeti == '100K-500k$':
            manqana = 'Ferrari F430'
        elif qveyana == 'იტალია' and cilindrebi == '8' and biujeti == '500K-2M$':
            manqana = 'Ferrari 458 Speciale'
        elif qveyana == 'იტალია' and cilindrebi == '10' and biujeti == '50k-100K$':
            manqana = 'Lamborghini Gallardo'
        elif qveyana == 'იტალია' and cilindrebi == '10' and biujeti == '100K-500k$':
            manqana = 'Lamborghini Huracán'
        elif qveyana == 'იტალია' and cilindrebi == '10' and biujeti == '500K-2M$':
            manqana = 'Lamborghini Huracán STO'

        elif qveyana == 'გერმანია' and cilindrebi == '6' and biujeti == '50k-100K$':
            manqana = 'BMW M2 Competition'
        elif qveyana == 'გერმანია' and cilindrebi == '6' and biujeti == '100K-500k$':
            manqana = 'Porsche 911 Carrera S'
        elif qveyana == 'გერმანია' and cilindrebi == '6' and biujeti == '500K-2M$':
            manqana = 'Porsche 959'
        elif qveyana == 'გერმანია' and cilindrebi == '8' and biujeti == '50k-100K$':
            manqana = 'Mercedes-AMG C63'
        elif qveyana == 'გერმანია' and cilindrebi == '8' and biujeti == '100K-500k$':
            manqana = 'Audi R8 V8'
        elif qveyana == 'გერმანია' and cilindrebi == '8' and biujeti == '500K-2M$':
            manqana = 'Mercedes-AMG GT Black Series'
        elif qveyana == 'გერმანია' and cilindrebi == '10' and biujeti == '50k-100K$':
            manqana = 'BMW M5 E60'
        elif qveyana == 'გერმანია' and cilindrebi == '10' and biujeti == '100K-500k$':
            manqana = 'Audi R8 V10'
        elif qveyana == 'გერმანია' and cilindrebi == '10' and biujeti == '500K-2M$':
            manqana = 'Porsche Carrera GT'

        elif qveyana == 'იაპონია' and cilindrebi == '6' and biujeti == '50k-100K$':
            manqana = 'Nissan 370Z NISMO'
        elif qveyana == 'იაპონია' and cilindrebi == '6' and biujeti == '100K-500k$':
            manqana = 'Toyota Supra TRD 3000GT'
        elif qveyana == 'იაპონია' and cilindrebi == '6' and biujeti == '500K-2M$':
            manqana = 'Nissan GT-R R34 Z-Tune'
        elif qveyana == 'იაპონია' and cilindrebi == '8' and biujeti == '50k-100K$':
            manqana = 'Lexus IS F'
        elif qveyana == 'იაპონია' and cilindrebi == '8' and biujeti == '100K-500k$':
            manqana = 'Lexus LFA'
        elif qveyana == 'იაპონია' and cilindrebi == '8' and biujeti == '500K-2M$':
            manqana = 'Lexus LFA Nürburgring Edition'
        elif qveyana == 'იაპონია' and cilindrebi == '10' and biujeti == '50k-100K$':
            manqana = 'Honda/Acura NSX Gen 1'
        elif qveyana == 'იაპონია' and cilindrebi == '10' and biujeti == '100K-500k$':
            manqana = 'Honda/Acura NSX Gen 2 (2016+)'
        elif qveyana == 'იაპონია' and cilindrebi == '10' and biujeti == '500K-2M$':
            manqana = 'Honda NSX GT3'
        else:
            pass
        self.shedegi.setText(f"თქვენთვის იდეალური მანქანა არის: {manqana}")



    def __init__(self):
        super().__init__()
        self.setWindowTitle('იპოვე საშენო მანქანა')
        self.setGeometry(400, 200, 400, 700)

        self.gacnoba = QLabel('ეროვნების, ცილინდრების რაოდენობის და ბიუჯეტის არჩევის შემდეგ, \nჩვენ გეტყვით თუ რომელია შენთვის საუკეთესო მანქანა')
        self.tanxmoba = QCheckBox("მე ვეთანხმები წესებს")
        self.sqesi = QLabel ("აირჩიე სქესი:")
        self.kaci = QRadioButton ("კაცი")
        self.qali = QRadioButton ("ქალი")
        self.transformeri = QRadioButton ("ტრანსფორმერი")



        self.qveyana = QComboBox()
        self.qveyana.addItems(['გერმანია', 'იტალია', 'იაპონია'])

        self.biujeti = QComboBox()
        self.biujeti.addItems(['50k-100K$', '100K-500k$', '500K-2M$'])

        self.cilindrebi = QComboBox()
        self.cilindrebi.addItems(['6', '8', '10'])

        self.shedegi = QLabel ("თქვენთვის იდეალური მანქანა არის:")
        self.dzieba_btn = QPushButton('მოძებნე შესაბამისი მანქანა')


        layout = QVBoxLayout()
        layout.addWidget(self.gacnoba)
        layout.addWidget(self.tanxmoba)
        layout.addWidget(self.sqesi)
        layout.addWidget(self.kaci)
        layout.addWidget(self.qali)
        layout.addWidget(self.transformeri)
        layout.addWidget(QLabel("აირჩიე ქვეყანა:"))
        layout.addWidget(self.qveyana)
        layout.addWidget(QLabel("აირჩიე ბიუჯეტი:"))
        layout.addWidget(self.biujeti)
        layout.addWidget(QLabel("აირჩიე ცილინდრების რაოდენობა:"))
        layout.addWidget(self.cilindrebi)
        layout.addWidget(self.dzieba_btn)
        self.dzieba_btn.clicked.connect(self.dzebna)
        layout.addWidget(self.shedegi)

        self.setLayout(layout)



app = QApplication(sys.argv)
window = MyWindow()

window.show()
sys.exit(app.exec_())

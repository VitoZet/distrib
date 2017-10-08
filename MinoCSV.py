import xlrd, csv, sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from datetime import datetime
from UIminoCSV import Ui_FP_Minotavr


class FPMinoCSV(QMainWindow, Ui_FP_Minotavr):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.initSignal()


    def initSignal(self):
        self.minoCSV.clicked.connect(self.miniCSV)

    def miniCSV(self):
        wb = xlrd.open_workbook('mino.xlsx')

        sheet1 = wb.sheet_by_index(0)
        csv_price = []
        csv_balance = []
        for row in range(sheet1.nrows):
            try:
                row_num = float(str(sheet1.cell_value(row, 0)).strip())
            except:
                row_num = 0
            if row_num > 0:
                artik = str(sheet1.cell_value(row, 1)).strip()
                balanc = int(float(str(sheet1.cell_value(row, 3)).strip().replace('есть', '777')))
                price_col = float(str(sheet1.cell_value(row, 7)).replace('Цена клиента', ''))

                if price_col < 70:
                    price_col *= 2.00
                elif 70 <= price_col < 200:
                    price_col *= 1.6
                elif 200 <= price_col < 400:
                    price_col *= 1.43
                elif 400 <= price_col < 1500:
                    price_col *= 1.35
                elif 1500 <= price_col < 2200:
                    price_col *= 1.30
                else:
                    price_col *= 1.25

                price_col_round = int(round(price_col,-1))


                csv_price.append([artik, price_col_round])
                csv_balance.append([artik,balanc])

        with open('Остатки от ' + str(datetime.date(datetime.now())) +'.csv', 'w', newline='') as csv_f:
            csv_w = csv.writer(csv_f, delimiter = ';')
            csv_w.writerows(csv_balance)

        with open('Розн цены от ' +str(datetime.date(datetime.now())) + '.csv', 'w', newline='') as csv_p:
            csv_wp = csv.writer(csv_p, delimiter = ';')
            csv_wp.writerows(csv_price)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    MinoCSV = FPMinoCSV()
    MinoCSV.show()
    sys.exit(app.exec_())
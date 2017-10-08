# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIminoCSV.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FP_Minotavr(object):
    def setupUi(self, FP_Minotavr):
        FP_Minotavr.setObjectName("FP_Minotavr")
        FP_Minotavr.resize(275, 303)
        self.centralwidget = QtWidgets.QWidget(FP_Minotavr)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 20, 221, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.minoCSV = QtWidgets.QPushButton(self.centralwidget)
        self.minoCSV.setGeometry(QtCore.QRect(30, 230, 221, 23))
        self.minoCSV.setObjectName("minoCSV")
        FP_Minotavr.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FP_Minotavr)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 275, 21))
        self.menubar.setObjectName("menubar")
        FP_Minotavr.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FP_Minotavr)
        self.statusbar.setObjectName("statusbar")
        FP_Minotavr.setStatusBar(self.statusbar)

        self.retranslateUi(FP_Minotavr)
        QtCore.QMetaObject.connectSlotsByName(FP_Minotavr)

    def retranslateUi(self, FP_Minotavr):
        _translate = QtCore.QCoreApplication.translate
        FP_Minotavr.setWindowTitle(_translate("FP_Minotavr", "FP - MinotavrPrice"))
        self.textBrowser.setHtml(_translate("FP_Minotavr", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Обработка прайса минотавр.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">После обработки на выходе будет два файла <span style=\" font-weight:600;\">CSV</span>.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Один с <span style=\" font-weight:600;\">остатками</span>, второй с <span style=\" font-weight:600;\">Розничными ценами.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Обробатываемый файл нужно переименовать на:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">mino</span></p></body></html>"))
        self.minoCSV.setText(_translate("FP_Minotavr", "Обработать МИНОТАВР"))


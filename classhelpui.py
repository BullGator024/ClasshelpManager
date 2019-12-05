# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python_stuff\MENUDEF_ClassHelp\classhelpgui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(532, 620)
        MainWindow.setMinimumSize(QtCore.QSize(532, 620))
        MainWindow.setMaximumSize(QtCore.QSize(532, 620))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labFile = QtWidgets.QLabel(self.centralwidget)
        self.labFile.setGeometry(QtCore.QRect(10, 10, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labFile.setFont(font)
        self.labFile.setObjectName("labFile")
        self.txtFilePath = QtWidgets.QLineEdit(self.centralwidget)
        self.txtFilePath.setGeometry(QtCore.QRect(90, 10, 331, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtFilePath.setFont(font)
        self.txtFilePath.setObjectName("txtFilePath")
        self.btnOpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenFile.setGeometry(QtCore.QRect(440, 10, 75, 21))
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.grpbStats = QtWidgets.QGroupBox(self.centralwidget)
        self.grpbStats.setGeometry(QtCore.QRect(10, 80, 191, 141))
        self.grpbStats.setObjectName("grpbStats")
        self.lab_S_HP = QtWidgets.QLabel(self.grpbStats)
        self.lab_S_HP.setGeometry(QtCore.QRect(10, 50, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_S_HP.setFont(font)
        self.lab_S_HP.setObjectName("lab_S_HP")
        self.lab_S_SPD = QtWidgets.QLabel(self.grpbStats)
        self.lab_S_SPD.setGeometry(QtCore.QRect(10, 80, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_S_SPD.setFont(font)
        self.lab_S_SPD.setObjectName("lab_S_SPD")
        self.lab_S_JMP = QtWidgets.QLabel(self.grpbStats)
        self.lab_S_JMP.setGeometry(QtCore.QRect(10, 110, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_S_JMP.setFont(font)
        self.lab_S_JMP.setObjectName("lab_S_JMP")
        self.lab_S_NAM = QtWidgets.QLabel(self.grpbStats)
        self.lab_S_NAM.setGeometry(QtCore.QRect(10, 20, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_S_NAM.setFont(font)
        self.lab_S_NAM.setObjectName("lab_S_NAM")
        self.grpbNStats = QtWidgets.QGroupBox(self.centralwidget)
        self.grpbNStats.setGeometry(QtCore.QRect(220, 80, 221, 141))
        self.grpbNStats.setObjectName("grpbNStats")
        self.lab_S_JMP_2 = QtWidgets.QLabel(self.grpbNStats)
        self.lab_S_JMP_2.setGeometry(QtCore.QRect(10, 110, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_S_JMP_2.setFont(font)
        self.lab_S_JMP_2.setObjectName("lab_S_JMP_2")
        self.lab_S_SPD_2 = QtWidgets.QLabel(self.grpbNStats)
        self.lab_S_SPD_2.setGeometry(QtCore.QRect(10, 80, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_S_SPD_2.setFont(font)
        self.lab_S_SPD_2.setObjectName("lab_S_SPD_2")
        self.lab_S_NAM_2 = QtWidgets.QLabel(self.grpbNStats)
        self.lab_S_NAM_2.setGeometry(QtCore.QRect(10, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_S_NAM_2.setFont(font)
        self.lab_S_NAM_2.setObjectName("lab_S_NAM_2")
        self.lab_S_HP_2 = QtWidgets.QLabel(self.grpbNStats)
        self.lab_S_HP_2.setGeometry(QtCore.QRect(10, 50, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_S_HP_2.setFont(font)
        self.lab_S_HP_2.setObjectName("lab_S_HP_2")
        self.txtCName = QtWidgets.QLineEdit(self.grpbNStats)
        self.txtCName.setGeometry(QtCore.QRect(70, 20, 141, 20))
        self.txtCName.setObjectName("txtCName")
        self.spnbHealth = QtWidgets.QSpinBox(self.grpbNStats)
        self.spnbHealth.setGeometry(QtCore.QRect(70, 50, 141, 22))
        self.spnbHealth.setMaximum(30000)
        self.spnbHealth.setObjectName("spnbHealth")
        self.spnbJump = QtWidgets.QSpinBox(self.grpbNStats)
        self.spnbJump.setGeometry(QtCore.QRect(70, 110, 141, 22))
        self.spnbJump.setObjectName("spnbJump")
        self.txtStrafeSPD = QtWidgets.QLineEdit(self.grpbNStats)
        self.txtStrafeSPD.setGeometry(QtCore.QRect(70, 80, 141, 20))
        self.txtStrafeSPD.setObjectName("txtStrafeSPD")
        self.btnChange = QtWidgets.QPushButton(self.centralwidget)
        self.btnChange.setGeometry(QtCore.QRect(450, 110, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnChange.setFont(font)
        self.btnChange.setObjectName("btnChange")
        self.labMain = QtWidgets.QLabel(self.centralwidget)
        self.labMain.setGeometry(QtCore.QRect(20, 230, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labMain.setFont(font)
        self.labMain.setObjectName("labMain")
        self.txtMainfire = QtWidgets.QTextEdit(self.centralwidget)
        self.txtMainfire.setGeometry(QtCore.QRect(20, 260, 231, 121))
        self.txtMainfire.setReadOnly(False)
        self.txtMainfire.setTabStopWidth(24)
        self.txtMainfire.setObjectName("txtMainfire")
        self.labAltfire = QtWidgets.QLabel(self.centralwidget)
        self.labAltfire.setGeometry(QtCore.QRect(280, 230, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labAltfire.setFont(font)
        self.labAltfire.setObjectName("labAltfire")
        self.txtAltfire = QtWidgets.QTextEdit(self.centralwidget)
        self.txtAltfire.setGeometry(QtCore.QRect(280, 260, 231, 121))
        self.txtAltfire.setReadOnly(False)
        self.txtAltfire.setTabStopWidth(24)
        self.txtAltfire.setObjectName("txtAltfire")
        self.labITem = QtWidgets.QLabel(self.centralwidget)
        self.labITem.setGeometry(QtCore.QRect(280, 390, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labITem.setFont(font)
        self.labITem.setObjectName("labITem")
        self.txtItem = QtWidgets.QTextEdit(self.centralwidget)
        self.txtItem.setGeometry(QtCore.QRect(280, 420, 231, 121))
        self.txtItem.setReadOnly(False)
        self.txtItem.setTabStopWidth(24)
        self.txtItem.setObjectName("txtItem")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(450, 160, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cmbClassList = QtWidgets.QComboBox(self.centralwidget)
        self.cmbClassList.setGeometry(QtCore.QRect(90, 40, 151, 22))
        self.cmbClassList.setObjectName("cmbClassList")
        self.labReload = QtWidgets.QLabel(self.centralwidget)
        self.labReload.setGeometry(QtCore.QRect(20, 390, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labReload.setFont(font)
        self.labReload.setObjectName("labReload")
        self.txtReload = QtWidgets.QTextEdit(self.centralwidget)
        self.txtReload.setGeometry(QtCore.QRect(20, 420, 231, 121))
        self.txtReload.setReadOnly(False)
        self.txtReload.setTabStopWidth(24)
        self.txtReload.setObjectName("txtReload")
        self.btnExport = QtWidgets.QPushButton(self.centralwidget)
        self.btnExport.setGeometry(QtCore.QRect(440, 50, 75, 23))
        self.btnExport.setObjectName("btnExport")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 532, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Class Help manager"))
        self.labFile.setText(_translate("MainWindow", "File path:"))
        self.btnOpenFile.setText(_translate("MainWindow", "Open"))
        self.grpbStats.setTitle(_translate("MainWindow", "Class Stats (Current)"))
        self.lab_S_HP.setText(_translate("MainWindow", "Health: "))
        self.lab_S_SPD.setText(_translate("MainWindow", "Speed:"))
        self.lab_S_JMP.setText(_translate("MainWindow", "Jump: "))
        self.lab_S_NAM.setText(_translate("MainWindow", "Name: "))
        self.grpbNStats.setTitle(_translate("MainWindow", "Class Stats (New)"))
        self.lab_S_JMP_2.setText(_translate("MainWindow", "Jump: "))
        self.lab_S_SPD_2.setText(_translate("MainWindow", "Speed:"))
        self.lab_S_NAM_2.setText(_translate("MainWindow", "Name: "))
        self.lab_S_HP_2.setText(_translate("MainWindow", "Health: "))
        self.btnChange.setText(_translate("MainWindow", "Change"))
        self.labMain.setText(_translate("MainWindow", "Mainfire:"))
        self.txtMainfire.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.labAltfire.setText(_translate("MainWindow", "Altfire:"))
        self.txtAltfire.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.labITem.setText(_translate("MainWindow", "Item:"))
        self.txtItem.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", " Class:"))
        self.labReload.setText(_translate("MainWindow", "Reload:"))
        self.txtReload.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnExport.setText(_translate("MainWindow", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


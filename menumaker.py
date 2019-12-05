from classhelpui import *
from datetime import datetime
import sys, os


class ClassHelpW(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # !--- Actions ---! #
        self.btnChange.clicked.connect(self.btnChangeClick)
        self.btnOpenFile.clicked.connect(self.openFile)
        self.btnExport.clicked.connect(self.exportData)
        self.cmbClassList.currentIndexChanged.connect(self.on_comboBoxChange)
        self.btnClear.clicked.connect(self.clearAllFields)

        # !--- Stores ---! #
        self.classes = []
        self.class_hpp = []
        self.class_jmp = []
        self.class_spd = []
        self.class_mai = []
        self.class_alt = []
        self.class_rel = []
        self.class_itm = []

        self.new_classes = []
        self.new_class_hpp = []
        self.new_class_jmp = []
        self.new_class_spd = []
        self.new_class_mai = []
        self.new_class_alt = []
        self.new_class_rel = []
        self.new_class_itm = []

    def clearAllFields(self):
        self.txtAltfire.setText('')
        self.txtCName.setText('')
        self.txtItem.setText('')
        self.txtMainfire.setText('')
        self.txtStrafeSPD.setText('')
        self.spnbHealth.setValue(0)
        self.spnbJump.setValue(0)

    def exportData(self):
        filepath = self.txtFilePath.text()[::-1]
        newpath = ''
        try:
            for char in filepath:
                if char == '\\' or char == '/':
                    break
                else:
                    newpath = filepath[filepath.index(char) + 1:]
            newpath = newpath[::-1]
            data = []
            with open(newpath + 'ExportedData.txt', 'w+') as f:
                timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                data.append(f'// Data generated in {timestamp}\n\n')
                # [+] ===== Class names ===== [+] #
                data.append('OptionValue Classname \n')
                data.append('{ \n')
                for c in self.new_classes:
                    idx = self.new_classes.index(c)
                    string = self.new_classes[idx]
                    if string[0] == ' ':
                        string = string[1:]
                    data.append(f'{idx}, "{string}"\n')
                data.append('} \n\n\n')

                # [+] ===== Class Health values ===== [+] #
                data.append('OptionValue ClassHealth \n')
                data.append('{ \n')
                for c in self.new_classes:
                    idx = self.new_classes.index(c)
                    string = str(self.new_class_hpp[idx])
                    if string[0] == ' ':
                        string = string[1:]
                    data.append(f'{idx}, "{string}"\n')
                data.append('} \n\n\n')

                # [+] ===== Class Jump values ===== [+] #
                data.append('OptionValue ClassJump \n')
                data.append('{ \n')
                for c in self.new_classes:
                    idx = self.new_classes.index(c)
                    string = str(self.new_class_jmp[idx])
                    if string[0] == ' ':
                        string = string[1:]
                    data.append(f'{idx}, "{string}"\n')
                data.append('} \n\n\n')

                # [+] ===== Class Speed values ===== [+] #
                data.append('OptionValue ClassSpeed \n')
                data.append('{ \n')
                for c in self.new_classes:
                    idx = self.new_classes.index(c)
                    string = str(self.new_class_spd[idx])
                    if string[0] == ' ':
                        string = string[1:]
                    data.append(f'{idx}, "{string}"\n')
                data.append('} \n\n\n')

                # [+] ===== Class Mainfire values ===== [+] #
                data.append('OptionValue ClassMainfire \n')
                data.append('{ \n')
                for c in self.new_classes:
                    idx = self.new_classes.index(c)
                    string = str(self.new_class_mai[idx])
                    if string[0] == ' ':
                        string = string[1:]
                    data.append(f'{idx}, "{string}"\n')
                data.append('} \n\n\n')

                # [+] ===== Class Altfire values ===== [+] #
                data.append('OptionValue ClassAltfire \n')
                data.append('{ \n')
                for c in self.new_classes:
                    idx = self.new_classes.index(c)
                    string = str(self.new_class_alt[idx])
                    if string[0] == ' ':
                        string = string[1:]
                    data.append(f'{idx}, "{string}"\n')
                data.append('} \n\n\n')

                # [+] ===== Class Item values ===== [+] #
                data.append('OptionValue ClassItem \n')
                data.append('{ \n')
                for c in self.new_classes:
                    idx = self.new_classes.index(c)
                    string = str(self.new_class_itm[idx])
                    if string[0] == ' ':
                        string = string[1:]
                    data.append(f'{idx}, "{string}"\n')
                data.append('} \n\n\n')

                # [+] ===== Class Reload values ===== [+] #
                data.append('OptionValue ClassReload \n')
                data.append('{ \n')
                for c in self.new_classes:
                    idx = self.new_classes.index(c)
                    string = str(self.new_class_rel[idx])
                    if string[0] == ' ':
                        string = string[1:]
                    data.append(f'{idx}, "{string}"\n')
                data.append('} \n\n\n')

                f.writelines(data)

        except Exception as e:
            exc_tb = sys.exc_info()[2]
            print(f'Error ocurred in <exportData> at line {exc_tb.tb_lineno}: {e}')

    def btnChangeClick(self):
        index = self.cmbClassList.currentIndex()

        name = self.txtCName.text() if self.txtCName.text() != '' else self.classes[index]
        hp = self.spnbHealth.value() if self.spnbHealth.value() > 0 else self.class_hpp[index]
        spd = self.txtStrafeSPD.text() if self.txtStrafeSPD.text() != '' else self.class_spd[index]
        jmp = self.spnbJump.value() if self.spnbJump.value() > 0 else self.class_jmp[index]

        main = self.txtMainfire.toPlainText() if self.txtMainfire.toPlainText() != '' else self.class_mai[index]
        alt = self.txtAltfire.toPlainText() if self.txtAltfire.toPlainText() != '' else self.class_alt[index]
        itm = self.txtItem.toPlainText() if self.txtItem.toPlainText() != '' else self.class_itm[index]
        rel = self.txtReload.toPlainText() if self.txtReload.toPlainText() != '' else 'No reload attack'

        self.new_classes[index] = name
        self.new_class_hpp[index] = hp
        self.new_class_jmp[index] = jmp
        self.new_class_spd[index] = spd
        self.new_class_mai[index] = main
        self.new_class_alt[index] = alt
        self.new_class_rel[index] = rel
        self.new_class_itm[index] = itm

    def on_comboBoxChange(self):
        index = self.cmbClassList.currentIndex()
        name = 'Name: ' + self.classes[index]
        hp = 'Health: ' + self.class_hpp[index]
        spd = 'Speed: ' + self.class_spd[index]
        jmp = 'Jump: ' + self.class_jmp[index]

        self.lab_S_NAM.setText(name)
        self.lab_S_HP.setText(hp)
        self.lab_S_SPD.setText(spd)
        self.lab_S_JMP.setText(jmp)

        main = self.class_mai[index]
        alt = self.class_alt[index]
        itm = self.class_itm[index]

        self.txtMainfire.setText(main)
        self.txtAltfire.setText(alt)
        self.txtItem.setText(itm)

    def openFile(self):
        try:
            dir = self.txtFilePath.text()
            self.file = open(dir, 'r')

            self.text = self.file.readlines()
            self.file.close()

            templines = []
            for line in self.text:
                if line[0] in '1234567890':
                    templines.append(line.replace('\n', ''))
            

            index = ''
            oldindex = '0'
            array = 1
            for d in templines:
                for char in d:
                    if char in '1234567890' and char != ',':
                        index += char
                    else:
                        if int(index) < int(oldindex):
                            array += 1
                        i = d.index(char) + 1
                        i = d[i:]
                        i = i.replace('"', '')
                        self.manageItems(i, array)
                        oldindex = index
                        index = ''
                        break
            
            # !--- Add classes to combo box ---! #
            for clas in self.classes:
                self.cmbClassList.addItem(clas)
            self.cmbClassList.setCurrentIndex(0)

            self.new_classes = self.classes
            self.new_class_hpp = self.class_hpp
            self.new_class_jmp = self.class_jmp
            self.new_class_spd = self.class_spd
            self.new_class_mai = self.class_mai
            self.new_class_alt = self.class_alt
            self.new_class_rel = self.class_rel
            self.new_class_itm = self.class_itm

        except Exception as e:
            print(f'Error in < openFile >: {e}')
        
    def manageItems(self, i, array):
        temp = ''
        for j in i:
            if j != '/':
                temp += j
            else:
                break
        i = temp

        if array == 1:
            self.classes.append(i)
        elif array == 2:
            self.class_hpp.append(i)
        elif array == 3:
            self.class_jmp.append(i)
        elif array == 4:
            self.class_spd.append(i)
        elif array == 5:
            self.class_mai.append(i)
        elif array == 6:
            self.class_alt.append(i)
        elif array == 7:
            self.class_itm.append(i)
        elif array == 8:
            self.class_rel.append(i)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ClassHelpW()
    window.show()
    app.exec_()
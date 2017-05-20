import Main
import time

from PyQt4 import QtGui

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def sd(ser, ser_sent, ex):
    cycles = int(ex.lineEdit_sd.text())
    num = 1

    if (ex.comboBox_application.currentText() == 'Alteon'):
        while (cycles > 0):
            serial_line = ser.readline()
            print(serial_line)
            ex.label_sd_cycle.setText(_translate("Form", str(num), None))
            num += 1
            cycles -= 1
            if Main.Waitfor("assword:", 200, ser):
                print 'Entered sentry'
                for i in range(4):
                    print i
                    ser_sent.write("admn\n")
                    time.sleep(1)
                ser_sent.write("admn\n")
                time.sleep(1)
                ser_sent.write("admn\n")
                time.sleep(1)
                ser_sent.write("off .a2\n")
                time.sleep(1)
                ser_sent.write("on .a2\n")
                time.sleep(3)
                print 'finish'



            else:
                return 0;
        return 1;
    else:  ### rest of applications
        while (cycles > 0):
            serial_line = ser.readline()
            print(serial_line)
            ex.label_sd_cycle.setText(_translate("Form", str(num), None))
            num += 1
            cycles -= 1
            application = str(ex.comboBox_application.currentText() + '>')
            if Main.Waitfor(application, 200, ser):
                pass
            else:
                return 0;
        return 1;

import time, Main
from PyQt4 import QtGui
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


def sd(ser, ser_sent, ser_sent2, ser_TC, ex):
    cycles = int(ex.lineEdit_sd.text())
    num = 1
    power_up_time = Main.power_up_time(ex)
    global card_result
    card_result = 'PASS'
    application = str(ex.comboBox_application.currentText() + '>')
    cycles_ = cycles
    if (ex.comboBox_platform.currentText() == 'ODSVL2'):
        quant = '1'
    else:
        quant = '3'

    def control_thermal():
        if ex.checkBox_control_TC.isChecked():
            if (power_up_time * cycles_) > 3600:  # contronl TC only if the test is long than 1 hours
                if (num == 1):
                    ser_TC.write("SETP1,0\n")
                    print "Temp going down"
                elif num == int((cycles_ * ex.horizontalSlider_TC.value() / 100)):
                    ser_TC.write("SETP1,45\n")
                    print "Temp going up"

    while (cycles > 0):
        num_ = (num - 1) % 30  # creating dinamic delay for power off timing.
        serial_line = ser.readline()
        print(serial_line)
        ex.label_sd_cycle.setText(_translate("Form", str(num), None))
        control_thermal()
        num += 1
        cycles -= 1
        if (ex.comboBox_ps_acdc.currentText() == 'AC'):
            if (int(ex.comboBox_ps_num.currentText()) == 2):
                if (num % 2):
                    Main.off_on(ser_sent, ser_sent2, ex, num_, 1)
                else:
                    Main.off_on(ser_sent, ser_sent2, ex, num_, 2)
            else:
                Main.off_on(ser_sent, ser_sent2, ex, num_, 1)

            """if (num == int(ex.lineEdit_sd.text())): #to finish the tests with both PS are on
                ser_sent.write("on .a1\n")
                time.sleep(1)
                ser_sent.write("on .a2\n")"""
        elif (ex.comboBox_ps_acdc.currentText() == 'DC'):
            if (int(ex.comboBox_ps_num.currentText()) == 2):
                if (num % 2):
                    Main.off_on(ser_sent, ser_sent2, ex, num_, 1)
                else:
                    Main.off_on(ser_sent, ser_sent2, ex, num_, 2)
            else:
                Main.off_on(ser_sent, ser_sent2, ex, num_, 1)

        time.sleep(5)
        if (ex.comboBox_application.currentText() == 'Alteon'):
            if Main.Waitfor("assword:", power_up_time, ser):
                time.sleep(30)  ## use to debug
                ser.write("admin\n")
                time.sleep(2)
                if ex.checkBox_ssl_check.isChecked() and (card_result == 'PASS'):
                    time.sleep(2)
                    ser.write("/info/sys/ssl\n")
                    if Main.Waitfor(str(ex.comboBox_ssl_type.currentText()), 5, ser):
                        time.sleep(2)
                        ser.write("/info/sys/ssl\n")
                        if (ex.comboBox_ssl_type.currentText() == 'Cavium'):
                            if Main.Waitfor(('Count: ' + str(ex.comboBox_ssl_quant.currentText())), 3, ser):
                                pass
                            else:
                                card_result = 'Quant FAIL'
                        else:
                            if Main.Waitfor(('Count: ' + quant), 3, ser):
                                pass
                            else:
                                card_result = 'Quant FAIL'
                    else:
                        card_result = 'Recognize FAIL'



            else:
                return 0;
        else:  # rest of application
            if Main.Waitfor(application, power_up_time, ser):
                pass
            else:
                return 0;
    return 1;

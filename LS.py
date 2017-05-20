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


########off and on sentry######
def off_on(ser_sent, ex, off_time, ps_on):
    ser_sent.write("\n")
    if Main.Waitfor('Username:', 1, ser_sent):
        ser_sent.write("admn\n")
        Main.Waitfor(':', 2, ser_sent)
        ser_sent.write("admn\n")
    ser_sent.write("off .a1\n")
    Main.Waitfor(':', 2, ser_sent)
    ser_sent.write("off .a2\n")
    Main.Waitfor(':', 2, ser_sent)
    time.sleep(off_time)
    ser_sent.write("on .a" + str(ps_on) + "\n")
    return 1;


def ls(ser, ser_sent, ser_ls, ex):
    # cycles = int(ex.lineEdit_ls.text()) ###???
    num = 1
    power_up_time = Main.power_up_time(ex)
    global ls_card_result
    ####define LS  result
    test1 = ['Test1', 'PASS', 0]
    test2 = ['Test2', 'PASS', 0]
    test3 = ['Test3', 'PASS', 0]
    test4 = ['Test4', 'PASS', 0]
    test5 = ['Test5', 'PASS', 0]
    test6 = ['Test6', 'PASS', 0]

    ls_card_result = [test1, test2, test3, test4, test5, test6]
    if ex.comboBox_application.currentText() == 'Alteon':
        application = 'assword:'
        up_string = 'kernel'
    else:
        application = str(ex.comboBox_application.currentText() + '>')
        up_string = 'Starting up'
    ser.write("\n")
    # if (ex.comboBox_application.currentText() == 'Alteon'):
    for cyc in range(int(ex.lineEdit_ls.text())):
        ex.label_ls_cycle.setText(_translate("Form", str(cyc + 1), None))
        for n in range(1):  ## Test1 sd device thru sw command"
            ex.label_ls_result.setText(_translate("Form", '1', None))
            ps_on = (n % 2) + 1
            off_time = n

            if (n % 3):
                num += 1
            else:
                pass
            if Main.Waitfor(application, power_up_time, ser):
                pass
            else:
                print "last state not get application on loop num %d" % num
                ls_card_result[0][1] = "FAIL-application"
                ls_card_result[0][2] = n
                break
            if ex.comboBox_application.currentText() == 'Alteon':
                ser.write("admin\n")
                time.sleep(2)
                ser.write("boot/shutdown\n")
                time.sleep(2)
                ser.write("y\n")
                time.sleep(2)
            else:
                ser.write("login\n")
                time.sleep(2)
                ser.write("radware\n")
                time.sleep(2)
                ser.write("radware1\n")
                time.sleep(2)
                ser.write("shutdown\n")
                time.sleep(2)
                ser.write("y\n")
                time.sleep(2)
            print ls_card_result
            print application
            Main.Waitfor('Power down', 70, ser)  ##  ??
            off_on(ser_sent, ex, off_time, ps_on)
            if Main.Waitfor(up_string, 60, ser):
                print "last state failed on loop num %d" % num
                ls_card_result[0][1] = "FAIL"
                ls_card_result[0][2] = n
                break
            ser_ls.send_break(2)

        for n in range(0):  ## Test2 sd device thru button, graceful SD
            ex.label_ls_result.setText(_translate("Form", '2', None))
            ps_on = (n % 2) + 1
            off_time = n
            if (n % 3):
                num += 1
            else:
                pass
            # ex.progressBar_ls.setValue(num)
            if Main.Waitfor(application, power_up_time, ser):
                pass
            else:
                print "last state not get application on loop num %d" % num
                ls_card_result[1][1] = "FAIL-application"
                ls_card_result[1][2] = n
                break
            if ex.comboBox_application.currentText() == 'Alteon':
                ser.write("admin\n")
                time.sleep(2)
                ser.write("boot/shutdown\n")
                time.sleep(2)
                ser.write("y\n")
                time.sleep(2)
            else:
                ser.write("login\n")
                time.sleep(2)
                ser.write("radware\n")
                time.sleep(2)
                ser.write("radware1\n")
                time.sleep(2)
                ser.write("shutdown\n")
                time.sleep(2)
                ser.write("y\n")
                time.sleep(2)
            time.sleep(2)
            ser_ls.send_break(2)  ## sd device thru button grecefull
            time.sleep(2)
            Main.Waitfor('Power down', 70, ser)  ##  ??
            off_on(ser_sent, ex, off_time, ps_on)
            if Main.Waitfor(up_string, 60, ser):
                print "last state failed on loop num %d" % num
                ls_card_result[1][1] = "FAIL"
                ls_card_result[1][2] = n
                break
            ser_ls.send_break(2)

        for n in range(0):  ## Test3 sd device thru button, non-graceful SD
            ex.label_ls_result.setText(_translate("Form", '3', None))
            ps_on = (n % 2) + 1
            off_time = n
            if (n % 3):
                num += 1
            else:
                pass
                # ex.progressBar_ls.setValue(num)
            if Main.Waitfor(up_string, power_up_time, ser):
                pass
            else:
                print "last state not get application on loop num %d" % num
                ls_card_result[2][1] = "FAIL-application"
                ls_card_result[2][2] = n
                break
            if ex.comboBox_application.currentText() == 'Alteon':
                ser.write("admin\n")
                time.sleep(2)
                ser.write("boot/shutdown\n")
                time.sleep(2)
                ser.write("y\n")
                time.sleep(2)
            else:
                ser.write("login\n")
                time.sleep(2)
                ser.write("radware\n")
                time.sleep(2)
                ser.write("radware1\n")
                time.sleep(2)
                ser.write("shutdown\n")
                time.sleep(2)
                ser.write("y\n")
                time.sleep(2)
            ser_ls.send_break(5)  ## sd device thru button non grecefull
            print 'sd from PWR button'
            time.sleep(10)
            off_on(ser_sent, ex, off_time, ps_on)
            if Main.Waitfor(application, 60, ser):
                print "last state failed on loop num %d" % num
                ls_card_result[2][1] = "FAIL"
                ls_card_result[2][2] = n
                break
            ser_ls.send_break(2)
        for n in range(0):  ## Test4 EPI_test: simulation of electrical power interaption after power resume
            ex.label_ls_result.setText(_translate("Form", '4', None))
            ps_on = (n % 2) + 1
            off_time = n
            if (n % 3):
                num += 1
            else:
                pass
                # ex.progressBar_ls.setValue(num)

            time.sleep(5)

            off_on(ser_sent, ex, 10, ps_on)  ## first EPI
            print '----------first EPI ended----------'
            time.sleep(n)
            off_on(ser_sent, ex, off_time, ps_on)
            print '----------second EPI ended----------'
            if Main.Waitfor(up_string, 60, ser):
                pass
            else:
                print "EPI test failed on loop num %d" % num
                ls_card_result[3][1] = "FAIL"
                ls_card_result[3][2] = n
                break
            print ls_card_result
        num = 85
        # ex.progressBar_ls.setValue(num)
        for n in range(100):  ## Test5 0.1 resolution
            ex.label_ls_result.setText(_translate("Form", '5', None))
            ps_on = (n % 2) + 1
            if (n == 0):
                off_time = 0
            else:
                off_time += 0.1
            off_on(ser_sent, ex, off_time, ps_on)  ## first EPI
            print '---------- EPI ended----------'
            time.sleep(1)
        if Main.Waitfor(up_string, 60, ser):
            pass
        else:
            print " test5 failed on loop num %d" % num
            ls_card_result[4][1] = "FAIL"
        num = 95
        # ex.progressBar_ls.setValue(num)
        for n in range(100):  ## Test6 0.1 resolution power ON
            ex.label_ls_result.setText(_translate("Form", '5', None))
            ps_on = (n % 2) + 1
            if (n == 0):
                on_time = 0
            else:
                on_time += 0.1
            num += 1
            off_on(ser_sent, ex, 3, ps_on)  ## first EPI
            print '---------- EPI ended----------'
            time.sleep(on_time)
        num = 100
        # ex.progressBar_ls.setValue(num)
        if Main.Waitfor(up_string, 60, ser):
            pass
        else:
            print " test5 failed on loop num %d" % num
            ls_card_result[5][1] = "FAIL"

    for i in range(6):
        if ('FAIL' in ls_card_result[i]) or ('FAIL-application' in ls_card_result[i]):
            return 0;
        else:
            return 1;

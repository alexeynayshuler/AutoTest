import time, Main, os
from PyQt4 import QtGui
import Main
import os
import time

from PyQt4 import QtGui

filePath = "C:\\Python_projects\\auto_test_py\\tools"
filePath1 = "C:\\Python_projects\\auto_test_py\\tools\\pkp_test"
savePath = "C:\\Python_projects\\auto_test_py\\capture\\compression.txt"
port = 6188
username = 'radware'
password = 'radware'
nbytes = 4096
try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def reboot(ser, ser_TC, ex):
    cycles = int(ex.lineEdit_reboot.text())
    num = 1
    power_up_time = Main.power_up_time(ex)
    cycles_ = cycles

    def control_thermal():
        if ex.checkBox_control_TC.isChecked():
            if (power_up_time * cycles_) > 3600:  # contronl TC only if the test is long than 1 hours
                if (num == 1):
                    ser_TC.write("SETP1,0\n")
                    print "Temp going down"
                elif num == int((cycles_ * ex.horizontalSlider_TC.value() / 100)):
                    ser_TC.write("SETP1,45\n")
                    print "Temp going up"

    if (ex.comboBox_application.currentText() == 'Alteon'):
        while (cycles > 0):
            control_thermal()
            serial_line = ser.readline()
            print(serial_line)
            ex.label_reboot_cycle.setText(_translate("Form", str(num), None))
            num += 1
            cycles -= 1
            # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;for LSpci ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

            if ex.checkBox_lspci.isChecked() and (num > 2):
                if Main.Waitfor("Application...", 200, ser):
                    ser.write("ulp\n")
                    Main.Waitfor("#", 5, ser)
                    if num == 3:
                        ser.write("chmod 777 /disk/tools/*\n")
                        Main.Waitfor("#", 5, ser)
                    if (ex.comboBox_platform.currentText() == 'ODSHTQ'):
                        ser.write("/disk/tools/lspci -vv -s 87: | grep LnkSta:\n")
                        if Main.Waitfor("Speed 5GT/s, Width x8", 5, ser):
                            print 'got it ;;;;;;;;;;;;;;;;;;;;;;;;;;;'
                            ser.write("reboot\n")
                        else:
                            return 0;
                    elif (ex.comboBox_platform.currentText() == 'ODSHTQE'):
                        ser.write("/disk/tools/lspci -vv -s 87: | grep LnkSta:\n")
                        if Main.Waitfor("Speed 8GT/s, Width x8", 5, ser):
                            print 'got it ;;;;;;;;;;;;;;;;;;;;;;;;;;;'
                            ser.write("reboot\n")
                        else:
                            return 0;
                    elif (ex.comboBox_platform.currentText() == 'ODSMR'):
                        ser.write("/disk/tools/lspci -vv -s 13: | grep LnkSta:\n")
                        if Main.Waitfor("Speed 8GT/s, Width x8", 5, ser):
                            print 'got it ;;;;;;;;;;;;;;;;;;;;;;;;;;;'
                            ser.write("reboot\n")
                        else:
                            return 0;
                    elif (ex.comboBox_platform.currentText() == 'ODSVL2'):
                        ser.write("/disk/tools/lspci -vv -s 02: | grep LnkSta:\n")
                        if Main.Waitfor("Speed 8GT/s, Width x8", 5, ser):
                            print 'got it ;;;;;;;;;;;;;;;;;;;;;;;;;;;'
                            ser.write("reboot\n")
                        else:
                            return 0;

                else:
                    return 0;
            # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

            else:
                if Main.Waitfor("assword:", power_up_time, ser):
                    if ex.checkBox_lspci.isChecked() and (num == 2):
                        ##########3 config ip and load LSPCI file##################
                        ip = Main.get_PCip('1.1.1.1')
                        s1 = ip.split('.')
                        gw = s1[0] + '.' + s1[1] + '.1.1'
                        print ip
                        ser.write("exit\n")
                        if Main.Waitfor('[y/n]:', 2, ser):
                            ser.write("y\n")
                            time.sleep(2)
                        ser.write("\n")
                        if Main.Waitfor('password:', 300, ser):
                            pass
                        else:
                            ser.write("y\n")
                            Main.Waitfor(':', 3, ser)
                        ser.write("1Gb||bust!:admin\n")
                        if Main.Waitfor('$', 3, ser):
                            pass
                        else:
                            ser.write("y\n")
                            Main.Waitfor('$', 3, ser)
                        ser.write("/maint/sys/devacces\n")
                        if Main.Waitfor('deactivate?', 3, ser):
                            time.sleep(2)
                            ser.write("n\n")
                        else:
                            ser.write("radware\n")
                            Main.Waitfor('$', 3, ser)
                            ser.write("y\n")
                        Main.Waitfor('$', 3, ser)
                        ser.write("/cfg/sys/mmgmt/net 1/addr ")
                        ser.write(ip)
                        ser.write("\n")
                        Main.Waitfor('$', 3, ser)
                        ser.write("/cfg/sys/mmgmt/net 1/mask 255.255.0.0\n")
                        Main.Waitfor('$', 3, ser)
                        ser.write("/cfg/sys/mmgmt/net 1/gw ")
                        ser.write(gw)
                        ser.write("\n")
                        Main.Waitfor('$', 3, ser)
                        ser.write("/cfg/sys/mmgmt/net 1/ena\n")
                        Main.Waitfor('$', 3, ser)
                        ser.write("apply\n")
                        Main.Waitfor('$', 3, ser)
                        serverPath = "/disk/"
                        print(
                        "pscp -batch -unsafe -P 6188 -pw radware -r " + filePath + " radware@" + ip + ":" + serverPath)
                        os.system(
                            "pscp -batch -unsafe -P 6188 -pw radware -r " + filePath + " radware@" + ip + ":" + serverPath)
                        time.sleep(5)
                        ser.write("/revert\n")
                        time.sleep(2)
                        ser.write("y\n")
                        time.sleep(2)
                        ser.write("save\n")
                        time.sleep(2)
                        ser.write("y\n")
                        time.sleep(2)
                        ser.write("y\n")
                        time.sleep(2)
                        ser.write("exit\n")
                        time.sleep(2)


                        #########################################################

                    ser.write("admin\n")
                    time.sleep(2)
                    ser.write("/boot/reset\n")
                    time.sleep(2)
                    ser.write("y\n")
                else:
                    return 0;

        return 1;
    else:  ### rest of applications
        while (cycles > 0):
            control_thermal()
            serial_line = ser.readline()
            print(serial_line)
            ex.label_reboot_cycle.setText(_translate("Form", str(num), None))
            num += 1
            cycles -= 1
            application = str(ex.comboBox_application.currentText() + '>')
            if Main.Waitfor(application, power_up_time, ser):
                ser.write("login\n")
                time.sleep(2)
                ser.write("radware\n")
                time.sleep(2)
                ser.write("radware1\n")
                time.sleep(2)
                ser.write("reboot\n")
                time.sleep(2)
                ser.write("y\n")
            else:
                return 0;
        return 1;

import pyping
import re
import telnetlib
import time

import os
import serial
import socket
from PyQt4 import QtGui

result_path = 'C:\\Python_projects\\auto_test_py\\results\\'
cap1_path = 'C:\\Python_projects\\auto_test_py\\capture\\capture1.txt'
cap2_path = 'C:\\Python_projects\\auto_test_py\\capture\\capture2.txt'
# cap = open(capture_path+'capture.txt','w+')
global cap1
global cap2
try:
    cap1 = open(cap1_path, 'w+')
    print cap1
    cap2 = open(cap2_path, 'w+')
except:
    print 'cant open capture file'

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


# device list [MAC,Sw version]
######### Open serial interface for Radware Device
def openSerial(ex):  # com_info = [COM3,9600]
    ser = serial.Serial()
    if ex.comboBox_application.currentText() == 'Alteon':
        ser.baudrate = '9600'
    else:
        ser.baudrate = '19200'

    ser.port = str('COM' + ex.lineEdit_COM.text())
    ser.timeout = 1
    # ser.port = str(com_info[0])
    ser.open()
    print ser.portstr + ' Opened'
    return ser;

    """try:
        ser.open()
        print ser.portstr + ' Opened'
        return ser;
    except: 
        print 'cant open  %s'   %ser.port    """


def openSerial_sent(ex):  # com_info = [COM3,9600]
    if (ex.comboBox_pwr_sw.currentText() == 'Sentry'):
        ser_sent = serial.Serial()
        ser_sent.baudrate = '9600'
        ser_sent.port = str('COM' + ex.lineEdit_sd_sentry.text())
        ser_sent.timeout = 1
        # ser.port = str(com_info[0])
        ser_sent.open()
        print ser_sent.portstr + ' Opened'
    else:
        # ser_sent = telnetlib.Telnet("10.201.100.180")
        ser_sent = 'PASS'
    return ser_sent;


def openSerial_sent2(ex):
    ser_sent2 = serial.Serial()
    ser_sent2.baudrate = '9600'
    ser_sent2.port = str('COM' + ex.lineEdit_sd_sentry_2.text())
    ser_sent2.timeout = 1
    # ser.port = str(com_info[0])
    ser_sent2.open()
    print ser_sent2.portstr + ' Opened'
    return ser_sent2;


def openSerial_ls(ex):  # com_info = [COM3,9600]
    ser_ls = serial.Serial()
    ser_ls.baudrate = '9600'
    ser_ls.port = str('COM' + ex.lineEdit_ls_com.text())
    ser_ls.timeout = 1
    # ser.port = str(com_info[0])
    ser_ls.open()
    print ser_ls.portstr + ' Opened'
    return ser_ls;


def openSerial_TC(ex):  # com_info = [COM3,9600]
    ser_TC = serial.Serial()
    ser_TC.baudrate = '19200'
    ser_TC.port = 'COM1'
    ser_TC.timeout = 1
    # ser.port = str(com_info[0])
    ser_TC.open()
    print ser_TC.portstr + ' Opened'
    return ser_TC;


def need_reboot(ex, ser):
    power_up = power_up_time(ex)
    ser.write("exit\n")
    if (ex.comboBox_application.currentText() == 'Alteon'):
        if Waitfor("assword:", power_up, ser):
            ser.write("admin\n")
            time.sleep(2)
            ser.write("/boot/reset\n")
            time.sleep(2)
            ser.write("y\n")
            return 1;
        else:
            print 'not rebooted'
            return 0;
    else:
        application = str(ex.comboBox_application.currentText() + '>')
        if Waitfor(application, power_up, ser):
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
            print 'not rebooted'
            return 0;


########Power OFF/ON function######
def off_on(ser_sent, ser_sent2, ex, off_time, ps_on):
    if (ex.comboBox_pwr_sw.currentText() == 'Sentry'):
        ser_sent.write("\n")
        if Waitfor('Username:', 1, ser_sent):
            ser_sent.write("admn\n")
            Waitfor(':', 2, ser_sent)
            ser_sent.write("admn\n")
        ser_sent.write("off .a1\n")
        Waitfor(':', 2, ser_sent)
        ser_sent.write("off .a2\n")
        Waitfor(':', 2, ser_sent)
        time.sleep(off_time)
        ser_sent.write("on .a" + str(ps_on) + "\n")
    else:  # Tower Power
        ser_sent = telnetlib.Telnet("10.201.100.180")
        print ser_sent.read_until("Username :", 2)
        ser_sent.write("admn\r\n")
        print ser_sent.read_until("Password :", 2)
        ser_sent.write("admn\r\n")
        print ser_sent.read_until("LX:", 2)
        ser_sent.write("off ." + ex.comboBox_tp1.currentText() + "\r\n")
        print ser_sent.read_until("LX:", 2)
        ser_sent.write("off ." + ex.comboBox_tp2.currentText() + "\r\n")
        print ser_sent.read_until("LX:", 2)
        time.sleep(off_time)

        if ps_on == 1:
            ser_sent.write("on ." + ex.comboBox_tp1.currentText() + "\r\n")
        else:
            ser_sent.write("on ." + ex.comboBox_tp2.currentText() + "\r\n")
        time.sleep(2)
        ser_sent.close()
        print 'finish SD cycle thru Tower Power'

    return 1;


########wait for function######
def Waitfor(str_search, timer, ser):
    # from Gui_combo import cap1
    # from Gui_combo import cap2
    t1 = time.time()
    t3 = 0
    global serial_line, cap1
    while (t3 < timer):
        t2 = time.time()
        t3 = t2 - t1
        serial_line = ser.readline()
        print(serial_line)
        cap1.write(serial_line + "\n")
        if (str_search in serial_line):
            if os.path.getsize(cap1_path) > 5000:
                print cap1
                print os.path.getsize(cap1_path)
                cap1.close()
                cap2.close()
                os.system('copy ' + cap1_path + ' ' + cap2_path)
                try:
                    cap1 = open(cap1_path, 'w+')
                    print 'after open'
                    print cap1
                    time.sleep(3)
                except:
                    print 'cant open capture file'
            return serial_line;
    cap1.close()
    cap2.close()
    os.system('copy ' + cap2_path + ' + ' + cap1_path + ' ' + cap2_path)
    try:
        cap1 = open(cap1_path, 'w+')
        print 'after open'
        print cap1
        time.sleep(3)
    except:
        print 'cant open capture file'
    return 0;


########get the Device info from power up######
def device_info(ex, ser):
    Device = ['mac', 'sw']
    if (ex.comboBox_application.currentText() == 'Alteon'):

        if Waitfor('kernel /', 100, ser):
            print 'reconize alteon'
            Device[1] = (serial_line.split('kernel /')[1]).split('/')[0]
        else:
            Device[1] = 'no ver'

        ####found Mac####################
        if Waitfor('Base MAC Address', 100, ser):
            Device[0] = (serial_line.split('= ')[1]).rstrip()
        else:
            Device[0] = 'no mac'
        return Device;
    ### DP applications
    elif (ex.comboBox_application.currentText() == 'DefensePro') and (
                ex.comboBox_platform.currentText() == 'ODSMR' or 'ODSHTQ' or 'ODSHTQE'):
        if Waitfor('mnt/cf/', 100, ser):
            Device[1] = (serial_line.split('mnt/cf/')[1]).split('-64bit')[0]
        else:
            Device[1] = 'no ver'

        ####found Mac####################
        if Waitfor('Base MAC address', 100, ser):
            Device[0] = (serial_line.split(': ')[1]).rstrip()
        else:
            Device[0] = 'no mac'
        return Device;
    else:  ### rest of DP and other applications#
        if Waitfor('MAC address: ', 100, ser):
            Device[0] = (serial_line.split(': ')[1]).rstrip()
        else:
            Device[0] = 'no mac'
        return Device;
        ### get SW
        if Waitfor('cm:/', 100, ser):
            Device[1] = (serial_line.split('/')[1]).split('/')[0]
        else:
            Device[1] = 'no ver'


####save results####################
def save(ex, Device, ls_card_result):
    maci = re.sub('[^0-9a-zA-Z]+', '', Device[0])
    try:
        fo = open(result_path + maci + ".txt", "w+")
        print (result_path + maci + ".txt")
    except:
        print 'cant save the file'
    fo.write("Device info :  Platform- %s Application- %s \n" % (
    ex.comboBox_platform.currentText(), ex.comboBox_application.currentText()))
    fo.write("MAC: %s  \n" % Device[0])
    fo.write("Version: %s  \n" % Device[1])
    fo.write("Reboot Test: %s  Result: %s %s Cycles \n" % (
    str(ex.checkBox_reboot.isChecked()), ex.label_reboot_result.text(), ex.lineEdit_reboot.text()))
    fo.write("ShutDown Test: %s  Result: %s %s Cycles \n" % (
    str(ex.checkBox_sd.isChecked()), ex.label_sd_result.text(), ex.lineEdit_sd.text()))
    fo.write("SSL Test: %s  Result: %s %s Cycles \n" % (
    str(ex.checkBox_ssl.isChecked()), ex.label_ssl_result.text(), ex.lineEdit_ssl.text()))
    fo.write("Last State Test: %s  Result: %s %s Cycles  \nReason: %s \n" % (
    str(ex.checkBox_ls.isChecked()), ex.label_ls_result.text(), ex.lineEdit_ls.text(), ls_card_result))
    fo.close()


###get PC ip#######################
def get_PCip(target):
    ipaddr = ''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((target, 8000))
        ipaddr = s.getsockname()[0]
        s.close()
    except:
        pass
    s1 = ipaddr.split('.')
    for i in range(200, 220):
        ip = s1[0] + '.' + s1[1] + '.' + s1[2] + '.' + str(i)
        r = pyping.ping(ip)
        if r.ret_code == 1:
            break
    return ip;


####power up time value##############    
def power_up_time(ex):
    if (ex.comboBox_platform.currentText() == 'ODSHTQE'):
        if (ex.comboBox_application.currentText() == 'Alteon'):
            return 500;
        elif (ex.comboBox_application.currentText() == 'DefensePro'):
            return 300;
        else:
            return 300;
    elif (ex.comboBox_platform.currentText() == 'ODSHTQ'):
        if (ex.comboBox_application.currentText() == 'Alteon'):
            return 300;
        elif (ex.comboBox_application.currentText() == 'DefensePro'):
            return 300;
        else:
            return 300;
    elif (ex.comboBox_platform.currentText() == 'ODSMR'):
        if (ex.comboBox_application.currentText() == 'Alteon'):
            return 300;
        elif (ex.comboBox_application.currentText() == 'DefensePro'):
            return 200;
        else:
            return 300;
    elif (ex.comboBox_platform.currentText() == 'ODSVL2'):
        if (ex.comboBox_application.currentText() == 'Alteon'):
            return 300;
        elif (ex.comboBox_application.currentText() == 'DefensePro'):
            return 300;
        else:
            return 300;
    elif (ex.comboBox_platform.currentText() == 'ODSLS'):
        if (ex.comboBox_application.currentText() == 'Alteon'):
            return 300;
        elif (ex.comboBox_application.currentText() == 'DefensePro'):
            return 300;
        else:
            return 300;
    elif (ex.comboBox_platform.currentText() == 'ODSVL'):
        if (ex.comboBox_application.currentText() == 'Alteon'):
            return 300;
        elif (ex.comboBox_application.currentText() == 'DefensePro'):
            return 300;
        else:
            return 300;
    elif (ex.comboBox_platform.currentText() == 'ODS2/3'):
        if (ex.comboBox_application.currentText() == 'Alteon'):
            return 300;
        elif (ex.comboBox_application.currentText() == 'DefensePro'):
            return 300;
        else:
            return 300;
    else:
        return 300;


####initialize the GUI##############    
def guiInit(ex, act):
    if (act):
        ex.label_MAC.setText(_translate("Form", '---', None))
        ex.label_SW.setText(_translate("Form", '---', None))
        ex.label_reboot_cycle.setText(_translate("Form", '---', None))
        ex.label_reboot_result.setText(_translate("Form", '---', None))
        ex.label_sd_cycle.setText(_translate("Form", '---', None))
        ex.label_sd_result.setText(_translate("Form", '---', None))
        ex.label_card_result.setText(_translate("Form", '---', None))
        ex.label_ssl_result.setText(_translate("Form", '---', None))
        ex.label_ls_result.setText(_translate("Form", '---', None))
        ex.progressBar_ssl.setValue(0)
        ex.progressBar_ls.setValue(0)
    ex.checkBox_reboot.setDisabled(act)
    ex.checkBox_need_reboot.setDisabled(act)
    ex.checkBox_control_TC.setDisabled(act)
    ex.checkBox_ls.setDisabled(act)
    ex.checkBox_ssl_check.setDisabled(act)
    ex.checkBox_sd.setDisabled(act)
    ex.comboBox_platform.setDisabled(act)
    ex.comboBox_ssl_quant.setDisabled(act)
    ex.comboBox_application.setDisabled(act)
    ex.comboBox_ps_num.setDisabled(act)
    ex.comboBox_ps_acdc.setDisabled(act)
    ex.checkBox_ssl_dis_info.setDisabled(act)
    ex.checkBox_ssl.setDisabled(act)
    ex.lineEdit_ssl.setDisabled(act)
    ex.checkBox_lspci.setDisabled(act)
    ex.checkBox_Traffic.setDisabled(act)

    ex.horizontalSlider_TC.setDisabled(act)

    ex.lineEdit_reboot.setDisabled(act)
    ex.lineEdit_ls.setDisabled(act)
    ex.lineEdit_ls_com.setDisabled(act)
    ex.lineEdit_sd.setDisabled(act)
    ex.lineEdit_sd_sentry.setDisabled(act)
    ex.comboBox_ps_num.setDisabled(act)
    ex.comboBox_ps_acdc.setDisabled(act)
    ex.lineEdit_COM.setDisabled(act)
    ex.pushButton_run.setDisabled(act)
    ex.pushButton_save.setDisabled(act)
    ex.comboBox_ssl_type.setDisabled(act)
    ex.comboBox_pwr_sw.setDisabled(act)
    ex.comboBox_tp1.setDisabled(act)
    ex.comboBox_tp2.setDisabled(act)

    # return ex;

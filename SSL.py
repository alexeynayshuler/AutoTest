import Main
import os
import time

import paramiko

filePath = "C:\\Python_projects\\auto_test_py\\tools"
filePath1 = "C:\\Python_projects\\auto_test_py\\tools\\pkp_test"
savePath = "C:\\Python_projects\\auto_test_py\\capture\\compression.txt"
port = 6188
username = 'radware'
password = 'radware'
nbytes = 4096


def ssl(ser, ex):
    if (ex.comboBox_platform.currentText() == 'ODSHTQE') or (ex.comboBox_platform.currentText() == 'ODSHTQ') or (
        ex.comboBox_platform.currentText() == 'ODSLS'):
        t_cycle = 20
    elif (ex.comboBox_platform.currentText() == 'ODSVL') or (ex.comboBox_platform.currentText() == 'ODS2/3'):
        t_cycle = 20
    elif (ex.comboBox_platform.currentText() == 'ODSVL2'):
        t_cycle = 6
    elif (ex.comboBox_platform.currentText() == 'ODSMR'):
        t_cycle = 11

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
    ser.write("/cfg/sys/mmgmt/net 1/ena\n")
    Main.Waitfor('$', 3, ser)
    ser.write("apply\n")
    Main.Waitfor('$', 3, ser)
    serverPath = "/disk/"
    print("pscp -P 6188 -pw radware -r " + filePath + " radware@" + ip + ":" + serverPath)
    os.system("pscp -P 6188 -batch -pw radware -r " + filePath + " radware@" + ip + ":" + serverPath)
    time.sleep(5)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port, username, password)
    except paramiko.SSHException:
        print "Connection Failed"
        quit()
    stdin, stdout, stderr = ssh.exec_command('chmod 777 /disk/tools/*')
    # outlines=stdout.readlines(30)
    # resp=''.join(outlines)
    # print(resp)
    t = int(ex.lineEdit_ssl.text())
    cycles = t / t_cycle
    # stdin,stdout,stderr = ssh.exec_command('/disk/tools/pkp_stress_htq '+str(cycles)+' all',get_pty=True)
    stdin, stdout, stderr = ssh.exec_command('/disk/tools/pkp_stress_htq ' + str(cycles) + ' all')
    print('/disk/tools/pkp_stress_htq ' + str(cycles) + ' all')
    stdin.close()
    runssl = 1
    run_compression = 0
    t1 = time.time()
    t3 = 0
    if t < t_cycle:
        runssl = 0
        print "SSL test time duration is to low need to be more than: %d" % t_cycle
    while (runssl):
        for line in stdout.readlines(50):  # 50
            print line

            if ('successfully!!!' in line):
                ex.progressBar_ssl.setValue(95)
                run_compression = 1
                # stdin,stdout,stderr=ssh.exec_command('/disk/tools/radware_test_hw')
                # stdin,stdout,stderr=ssh.exec_command('cd /disk/tools')
                # stdin,stdout,stderr=ssh.exec_command('radware_test_hw')
                print('/disk/tools/radware_test_hw')
                try:
                    comp_cap = open(savePath, "w+")
                except:
                    print 'cant open compression file'

            if (run_compression):

                comp_cap.write(line + "\n")
                if ('Finished 7/8' in line):
                    time.sleep(5)
                    ex.progressBar_ssl.setValue(100)
                    comp_cap.close()
                    ssh.close()
                    return 1;
            else:
                t2 = time.time()
                t3 = int((t2 - t1) / 60)
                if (t3 < t):
                    prog = (t3 * 100) / t
                else:
                    prog = 100

                ex.progressBar_ssl.setValue(prog)

    return 0;

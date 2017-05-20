from subprocess import Popen, PIPE

import Main

WINSCP = r'c:\<path to>\winscp.com'


class UploadFailed(Exception):
    pass


def upload_files(host, user, passwd, files):
    cmds = ['option batch abort', 'option confirm off']
    cmds.append('open sftp://{user}:{passwd}@{host}/'.format(host=host, user=user, passwd=passwd)
    cmds.append('put {} ./'.format(' '.join(files))
    cmds.append('exit\n')
    with Popen(WINSCP, stdin=PIPE, stdout=PIPE, stderr=PIPE,
               universal_newlines=True) as winscp:
        stdout, stderr = winscp.communicate('\n'.join(cmds))
    if winscp.returncode:
    # WinSCP returns 0 for success, so upload failed
        raise UploadFailed


PCip = Main.get_PCip(1.1
.1
.1)
serial_line = ser.readline()
print(serial_line)
ser.write("exit\n")
time.sleep(2)
ser.write("1Gb||bust!:admin\n")
time.sleep(2)
ser.write("/maint/sys/devacces\n")
time.sleep(2)
ser.write("radware\n")
time.sleep(2)
ser.write("y\n")
time.sleep(2)
upload_files(ip, )

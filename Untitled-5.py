import os

matrix = {}
matrix[(0, 1)] = 0
matrix[(0, 1)] = 0
# matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
savePath = "C:\\Python_projects\\auto_test_py\\capture\\compression.txt"
cap1_path = 'C:\\Python_projects\\auto_test_py\\capture\\capture1.txt'
cap2_path = 'C:\\Python_projects\\auto_test_py\\capture\\capture2.txt'
line = 'koby'

try:
    comp_cap = open(cap1_path, "w+")
except:
    print 'cant open compression file'

for i in range(5):
    comp_cap.write('2' + "\n")
comp_cap.close()
os.system('copy ' + cap2_path + ' + ' + cap1_path + ' ' + cap2_path)
comp_cap.close()
print 'finish'

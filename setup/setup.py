import sys
from subprocess import check_call

if sys.platform == "linux" or sys.platform == "linux2":
    print("[*] Installation on Linux")
    print("[*] Start installation all requirements from the list:")
    check_call(['pip', 'install', '-r', 'requirements.txt'])
    print("[*] All requirements installed.")


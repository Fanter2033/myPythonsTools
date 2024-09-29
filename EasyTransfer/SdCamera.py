import os
import sys
import subprocess
import xml.etree.ElementTree as ET
from util import *

class SdCamera:
    def __init__(self, os, vendor) -> None:
        self.osType = os
        self.vendor = vendor
        self.install_packages()
    
    def install_packages(self):
        if self.osType == "Windows":
            print("Installing Windows-specific packages...")
            for package in WINDOWS_PACKAGES:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        elif self.osType == "Linux":
            print("Installing Linux-specific packages...")
        else:
            print("OS not recognized!")
            return -1


    def find_in_fs(self):
        dd = ("","")
        if self.osType == "Windows":
            try:
                import win32com.client                              # After pywin32 is installed
                wmi = win32com.client.GetObject("winmgmts:")
                for disk in wmi.ExecQuery("SELECT * FROM Win32_LogicalDisk WHERE DriveType = 2"):  # DriveType = 2 is Removable
                    print(f"USB Drive: {disk.DeviceID} - {disk.VolumeName}")
                    dd = (disk.DeviceID, disk.VolumeName)

                    if(os.path.exists(dd[0]+"/PRIVATE/M4ROOT/MEDIAPRO.XML")):
                        tree = ET.parse(dd[0]+"/PRIVATE/M4ROOT/MEDIAPRO.XML")
                        root = tree.getroot()
                        
                        print(root.tag)
            except ImportError as e:
                print(f"Failed to import win32com: {e}")
        elif self.osType == "Linux":
            pass



if __name__ == "__main__":
    SD = SdCamera("Windows", "Sony")
    SD.find_in_fs()
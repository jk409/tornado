__author__ = 'Administrator'
import os
import win32api
import win32con
import wmi
import time
import sys
sys.path.append('./')
import sql

mysql=sql.Mysql('127.0.0.1','root','123456','kkk')
def getSysInfo(wmiService = None):
    result = {}
    if wmiService == None:
        wmiService = wmi.WMI()
    # cpu
    for cpu in wmiService.Win32_Processor():
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        result['cpuPercent'] = cpu.loadPercentage
    # memory
    cs = wmiService.Win32_ComputerSystem()
    os = wmiService.Win32_OperatingSystem()
    result['memTotal'] = int(int(cs[0].TotalPhysicalMemory)/1024/1024)
    result['memFree'] = int(int(os[0].FreePhysicalMemory)/1024)
    #disk
    result['diskTotal'] = 0
    result['diskFree'] = 0
    for disk in wmiService.Win32_LogicalDisk(DriveType=3):
        result['diskTotal'] += int(disk.Size)
        result['diskFree'] += int(disk.FreeSpace)
    result['diskTotal'] = int(result['diskTotal']/1024/1024)
    result['diskFree'] = int(result['diskFree']/1024/1024)
    return result

if __name__ == '__main__':
    wmiService = wmi.WMI()
    while 1:
        #timestamp = time.strftime('%Y-%m-%d %H:%M', time.localtime())
        timestamp = int(time.time())
        cpuPercent=getSysInfo(wmiService)['cpuPercent']
        memTotal=getSysInfo(wmiService)['memTotal']
        memFree =getSysInfo(wmiService)['memFree']
        memFree= memTotal  - memFree
        diskTotal=getSysInfo(wmiService)['diskTotal']
        diskFree =getSysInfo(wmiService)['diskFree']
        try:
            sqls="insert into  `hostinfo` (ip,time,cpuPercent,memTotal,memFree,diskTotal,diskFree) values('%s',%s,%s,%s,%s,%s,%s);"
            mysql.cmd(sqls%('127.0.0.1',timestamp,cpuPercent,memTotal,memFree,diskTotal,diskFree))
            mysql.commit()
            print('----------------------------------------------OK')
        except:
            print('----------------------------------------------Faile')
        time.sleep(10)
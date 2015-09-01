__author__ = 'Administrator'
import sys,time,socket
#E-mail:jk409@qq.com
#example: test.py   ip   80
def run(ip,port):
    #time.sleep(0.8)
    try:
        time.sleep(1)
        sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sc.settimeout(0.5)
        sc.connect((ip,port))
        return (ip,port,'success')
    except socket.timeout:
        return (ip,port,'danger')

    #except KeyboardInterrupt:
    #    break
if __name__ =="__main__":
    print(run('127.0.0.1',80))

import network
import socket
import time
import Stepper
from machine import Pin

SSID="XXXXXXXXXX"
PASSWORD="XXXXXXXXXXXX"
port=4533
wlan=None
listenSocket=None

def connectWifi(ssid,passwd):
  global wlan
  wlan=network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.disconnect()
  wlan.connect(ssid,passwd)
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  return True

try:
  connectWifi(SSID,PASSWORD)
  ip=wlan.ifconfig()[0]
  listenSocket = socket.socket()
  listenSocket.bind((ip,port))
  listenSocket.listen(1)
  listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  print ('tcp waitingw...')

  while True:
    print("accepting.....")
    conn,addr = listenSocket.accept()
    print(addr,"connected")

    while True:
      data = conn.recv(1024)
      if(len(data) == 0):
        print("close socket")
        conn.close()
        break
      print(data)
      ret = conn.send(data)
      #ret = conn.send("set_pos:")
except:
  if(listenSocket):
    listenSocket.close()
  wlan.disconnect()
  wlan.active(False)







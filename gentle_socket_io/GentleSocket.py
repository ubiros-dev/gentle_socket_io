import time
import socket
from gentle_socket_io import GentleProfile

# import math
# import serial, struct, 


class GentleSocket(object):
    def __init__(self, numFingers = 2):
        self.numFingers = numFingers
        self.fingerPos = [50] * numFingers
        self.offSet = [0] * numFingers
        self.defaultProfile = GentleProfile(name="Default")
        self.activeProfile = self.defaultProfile
        # self.finger1 = 50
        # self.finger2 = 50
        # self.finger3 = 50
        # self.finger4 = 50
        # self.finger5 = 50
        # self.finger6 = 50
        # self.finger7 = 50
        # self.finger8 = 50

        self.min = 0
        self.max = 120

        # self.offset1 = 0
        # self.offset2 = 0
        # self.offset3 = 0
        # self.offset4 = 0
        # self.offset5 = 0
        # self.offset6 = 0
        # self.offset7 = 0
        # self.offset8 = 0
        
        self.delayTime = 0.3

        self.closeVal = self.activeProfile.closeVal
        self.openVal = self.activeProfile.openVal

    def initialize(self, hostname, port = 88):
        self.socket = socket.socket()
        self.hostname = hostname
        self.socket.connect((hostname, port))
        time.sleep(self.delayTime)
        self.changeProfile(self.activeProfile)

    def end(self):
        self.socket.close()

    def sendCmd(self, cmd):
        self.socket.send(cmd.encode())

    def moveFinger(self, perc, finger = 0):
        if perc < self.min:
            perc = self.min

        if perc > self.max:
            perc = self.max
            
        if finger == 0:   #all fingers move together        "cmd = 'mN>': move all fingers to position N
            cmd = 'm'
        else:             #individual finger motion         "cmd = 'mF:N>": move finger F to position N
            cmd = '1' + str(finger) + ':'                   

        cmd = cmd + str(perc) + '>'
        self.sendCmd(cmd)
            
    def close(self):
        self.moveFinger(self.activeProfile.openVal)

    def open(self):
        self.moveFinger(self.activeProfile.closeVal)

    def changeProfile(self, profile: GentleProfile): #add all changes, force threshold, kp, ki, vmax
        cmd = 'k' + str(profile.Kp) + '>'
        self.sendCmd(cmd)
        cmd = 'i' + str(profile.Ki) + '>'
        self.sendCmd(cmd)
        cmd = 'v' + str(profile.Vmax) + '>'
        self.sendCmd(cmd)
        cmd = 'f' + str(profile.forceThreshold) + '>'
        self.sendCmd(cmd)
        self.activeProfile = profile

def example_function():
    return 1 + 1

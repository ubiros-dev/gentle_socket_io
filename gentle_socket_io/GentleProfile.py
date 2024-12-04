




class GentleProfile(object):
    def __init__(self, name, force = 2000, open = 30, close = 70, ki = 100, kp = 100, vmax = 100):
        self.name = name
        self.forceThreshold = force
        self.openVal = open
        self.closeVal = close
        self.Ki = ki
        self.Kp = kp
        self.Vmax = vmax
        
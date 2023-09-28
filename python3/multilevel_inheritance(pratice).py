class OppoA12:
    def __init__(self):
        self.deviceModel="OPPO A12"
        self.OppoA12_display="6.22 inche"
        self.OppoA12_ram="4 GB"
        self.OppoA12_rom="32GB"
        self.OppoA12_cpu="octa-core(4*2.35 GHZ)"
    def OppoA12_config(self):
        print("device model:-",self.deviceModel)
        print("display:-",self.OppoA12_display)
        print("ram:-",self.OppoA12_ram)
        print("rom:-",self.OppoA12_rom)
        print("cpu:-",self.OppoA12_cpu)

class OppoA15(OppoA12):
    def __init__(self):
        self.DeviceModel_1="OPPO A15"
        self.OppoA15_display="6.52 inches"
        self.OppoA15_ram="3 GB"
        self.OppoA15_rom="32 GB"
        #self.OppoA15_cpu = "octa-core(4*2.35 GHZ)"
        OppoA12.__init__(self)
    def OppoA15_config(self):
        print("device model:-",self.DeviceModel_1)
        print("display:-",self.OppoA15_display)
        print("ram:-",self.OppoA15_ram)
        print("rom:-",self.OppoA15_rom)
        print("cpu:-",self.OppoA12_cpu)

class OPPO_mobile(OppoA15 ):
    def __init__(self):
      self.mobile="OPPOA15"
      OppoA15.__init__(self)
    def mobile_config(self):
        print("special features mobile")
        print("device model:-",self.DeviceModel_1)
        print("ram:-",self.OppoA15_ram)
        #print("grate cpu:-",self.OppoA1_cpu)

a=OppoA12()
a.OppoA12_config()
print("------------------------------------------")
b=OppoA15()
b.OppoA15_config()
print("------------------------------------------")
c=OPPO_mobile()
c.mobile_config()

class redmi7:
    def __init__(self):
        self.deviceModel="Redmi 7A"
        self.vesion="MIUI version"
        self.RAM = "3 GB"
        self.ROM = "32 GB"
        self.CPU="Octa-core Max 2.01 GHZ"
    def redmi_configuration(self):
        print("device model :-",self.deviceModel)
        print("version :-",self.vesion)
        print("ROM:- ",self.ROM)
        print("RAM :-",self.RAM)
        print("CPU :-",self.CPU)

class samsung:
    def __init__(self):
        self.DeviceModel="samsung galaxy M20"
        self.processor="samsung Exynos 7904"
        self.frontCamera="8 MP"

    def samsung_configuration(self):
        print("device model :-",self.DeviceModel)
        print("processor :-",self.processor)
        print("front camera :-",self.frontCamera)


class IPhoneXR:
    def __init__(self):
        self.DeviceModel_1="Apple IphoneXR"
        self.IphoneXR_display="15.49 cm"
        self.IphoneXR_rom="64 GB"
        self.IphoneXR_ram="3 GB"
        self.IphoneXR_processor="apple A12 Bionic"
    def IPhoneXR_congifuration(self):
        print("device model:-", self.DeviceModel_1)
        print("display:-", self.IphoneXR_display)
        print("RAM:-", self.IphoneXR_ram)
        print("ROM:-", self.IphoneXR_rom)
        print("processor:-", self.IphoneXR_processor)

class IPhoneX:
    def __init__(self):
        self.DeviceModel=" Apple IPhoneX"
        self.IphoneX_display="5.8 inche"
        self.IphoneX_ram="3GB"
        self.IphoneX_rom="64 GB"
        self.IphoneX_processor="Apple A11 Bionic"
    def IPhoneX_congifuration(self):
        print("device model:-",self.DeviceModel)
        print("display:-",self.IphoneX_display)
        print("RAM:-",self.IphoneX_ram)
        print("ROM:-",self.IphoneX_rom)
        print("processor:-",self.IphoneX_processor)



class configuration(redmi7,IPhoneXR):
    def __init__(self):
        self.devicemodel1="redmi7"
        self.devicemodel2="iphonexr"
        redmi7.__init__(self)
        IPhoneXR.__init__(self)
    def config(self):
        print("mobile deatils")
        print("device model1",self.redmi_configuration())
        print("-------------------------------------------------------------------------")
        print("device model 2",self.IPhoneXR_congifuration())

a=configuration()
a.config()

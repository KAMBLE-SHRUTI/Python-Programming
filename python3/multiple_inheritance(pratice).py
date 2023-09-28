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

class Apple_Moile(IPhoneX,IPhoneXR):
    def __init__(self):
        self.DeviceModels="IPhoneX,IPoneXR"
        IPhoneX.__init__(self)
        IPhoneXR.__init__(self)
    def configuration(self):
        print("similar two apple mobiles")
        #print(self.DeviceModels)
        print("frist device:-",self.DeviceModel)
        print("IPhoneX:-",self.IphoneX_processor)
        print("second device :-",self.DeviceModel_1)
        print("IPhoneXR:-", self.IphoneXR_processor)





C=Apple_Moile()
C.configuration()
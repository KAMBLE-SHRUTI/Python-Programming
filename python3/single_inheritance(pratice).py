class redmi_mobile:
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

class samsung_mobile(redmi_mobile):
    def __init__(self):
        self.DeviceModel="samsung galaxy M20"
        self.processor="samsung Exynos 7904"
        self.frontCamera="8 MP"
        redmi_mobile.__init__(self)
    def samsung_configuration(self):
        print("device model :-",self.DeviceModel)
        print("processor :-",self.processor)
        print("front camera :-",self.frontCamera)
        print("----------new properties---------------")
        print("ROM:-",self.ROM)
        print("RAM:-",self.RAM)

a=redmi_mobile()
a.redmi_configuration()
print("--------------------------------------------------")
b=samsung_mobile()
b.samsung_configuration()

class home:
    def __init__(self):
        self.kt=500
        self.hl=800
        self.br=400
        self.bt=100

    def home_details(self):
        print("kitchen size:- ",self.kt)
        print("holl size:- ",self.hl)
        print("bedroom size:- ",self.br)
        print("bathroom size:- ",self.bt)

a=home()
a.home_details()
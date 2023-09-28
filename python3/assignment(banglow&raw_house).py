class banglow:
    def __init__(self):
        self.name="shukhi"
        self.kt=600
        self.bd=500
        self.hl=590
        self.gr=700
        self.br=300
        self.gy=1000
    def banglow_details(self):
        print("house:- ",self.name)
        print("kitchen:- ",self.kt)
        print("bedroom:- ",self.bd)
        print("holl:- ",self.hl)
        print("guest room:- ",self.gr)
        print("washroom:- ",self.br)
        print("gerlly:- ",self.gy)
class rew_house(banglow):
    def __init__(self):
        self.raw_house_name="samrudhi"
        self.kt=200
        self.br=400
        self.bt=200
        banglow.__init__(self)

    def raw_house_details(self):
        print("home:- ",self.raw_house_name)
        print("kitchen:- ",self.kt)
        print("bedroom:- ",self.br)
        print("bathroom:- ",self.bt)
        print("garlly:- ",self.gy)
        print("geust room:- ",self.gr)



b=rew_house()
b.banglow_details()
print("--------------------------------------------------------------")
b.raw_house_details()



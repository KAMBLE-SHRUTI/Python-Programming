class ENTC:
    def __init__(self):
        self._fy_entcCount=60
        self._entcHod="varene"

class CSE(ENTC):
    def __init__(self):
        self._fy_cseCount = 60
        self._cseHod = "supriya mali"
        ENTC.__init__(self)
        print("hod of entc dep.",self._entcHod)
        self._entcHod="sanjana patil"
        print("new hod of entc dep.",self._entcHod)

a=ENTC()
b=CSE()
print("----------------------------------")
print("hod from class entc",b._entcHod)
print("new hod from class entc",a._entcHod)

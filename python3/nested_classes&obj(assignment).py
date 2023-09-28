class company:
    def __init__(self):
        self.company_name="Amplifiers Electronics PVT LTD,Karad"
        self.company_founder="sagar shinde"
        self.company_domain="wed devlopment & embedeed system"
        self.company_city="Karad"

    def company_details(self):
        print("company:- ",self.company_name)
        print("founder:- ",self.company_founder)
        print("domain:- ",self.company_domain)
        print("city:- ",self.company_city)

    class founder:
        def __init__(self):
            self.founder_name="sagar shinde"
            self.founder_designation="wed devloper & embedeed system"
            self.founder_BOD="27-sep"
            self.founder_city="karad"
            self.founder_emailid="sagar@gmail.com"

        def founder_details(self):
            print("name:- ",self.founder_name)
            print("designation:- ",self.founder_designation)
            print("birth of date:- ",self.founder_BOD)
            print("city:- ",self.founder_city)
            print("email id:- ",self.founder_emailid)

a=company()
a.company_details()
print("-------------------------------------------------------")
b=a.founder()
b.founder_details()

class company:
    def __init__(self):
        self.company_name = "Amplifiers Electronics PVT LTD,Karad"
        self.company_founder = "sagar shinde"
        self.company_domain = "wed devlopment & embedeed system"
        self.company_city = "Karad"

    def company_details(self):
        print("company:- ",self.company_name)
        print("founder:- ",self.company_founder)
        print("domain:- ",self.company_domain)
        print("city:- ",self.company_city)

class founder:
    def __init__(self):
        self.founder_name = "sagar shinde"
        self.founder_designation = "wed devloper & embedeed system"
        self.founder_BOD = "27-sep"
        self.founder_city = "karad"
        self.founder_emailid = "sagar@gmail.com"


    def founder_details(self):
        print("name:- ", self.founder_name)
        print("designation:- ", self.founder_designation)
        print("birth of date:- ", self.founder_BOD)
        print("city:- ", self.founder_city)
        print("email id:- ", self.founder_emailid)


class employee(company,founder):
    def __init__(self):
        self.emplyee_name="bhagyashri bamane"
        self.emplyee_designation="python devloper"
        self.emplyee_BOD="15-july"
        self.emplyee_city="sangli"
        self.emplyee_emailid="bhagyashri@gmail.com"
        company.__init__(self)
        founder.__init__(self)

    def employee_deatils(self):
        print("name:- ",self.emplyee_name)
        print("desingnation:- ",self.emplyee_designation)
        print("birth of date:- ",self.emplyee_BOD)
        print("city:- ",self.emplyee_city)
        print("email id:- ",self.emplyee_emailid)
        print("comapny:- ",self.company_name)
        print("founter:- ",self.founder_name)


c=employee()
c.employee_deatils()


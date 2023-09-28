class author:
    def __init__(self,name,age,state,mobile):
        self.name=name
        self.age=age
        self.state=state
        self.mobile=mobile

    def author_details(self):
        print("author name:-",self.name)
        print("author age:- ",self.age)
        print("author state:- ",self.state)
        print("author mobile num:- ",self.mobile)


class book(author):
    def __init__(self,book,author,price,year,pages):
        self.book=book
        self.author=author
        self.price=price
        self.year=year
        self.pages=pages
        super().__init__(self.name,self.age,self.state,self.mobile)      #error

    def book_details(self):
        print("book name:- ",self.book)
        print("author:- ",self.author)
        print("price:- ",self.price)
        print("year:- ",self.year)
        print("pages:- ",self.pages)

a=author("chetan bhagat","28 age","gujrat","9876543201")
a.author_details()
print("--------------------------------------------------------------------")
b=book("2states","chetan bhagat","250/-","2019","986")
b.book_details()

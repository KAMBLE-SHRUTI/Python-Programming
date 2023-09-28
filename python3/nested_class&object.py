class book:
    def __init__(self):
        self.book = "chava"
        self.book_author = "shivaji sawant"

    def book_details(self):
        print("book name:- ", self.book)
        print("book author:- ", self.book_author)

    class author:
        def __init__(self):
            self.author_name = "shivaji sawant"
            self.BOD = "31-aug"

        def author_details(self):
            print("author name:- ", self.author_name)
            print("date of birth:- ", self.BOD)


a = book()
a.book_details()
print("-------------------------------------------------------")
b = a.author()
b.author_details()

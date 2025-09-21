class Book:
    def __init__(self, bid, baname, price=400, author=0):                   #####prameterised and parameterless constructor
        self.bid = bid
        self.bname = baname
        self.price = price
        self.author = author

    def showbook(self):
        print('Book details')
        return f'BOOK ID:{self.bid}\nBOOK NANME:{self.bname}\nPRICE:{self.price}\nAUTHOR:{self.author}\n'
    
    def __del__(self):                                              ####destructor call
        print('Destructor call')

b1 = Book(101, 'Python', 500, 'S.B.Kishor')

print(b1.showbook())

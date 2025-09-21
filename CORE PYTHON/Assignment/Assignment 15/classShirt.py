class Shirt:
    def __init__(self, sid, sname, type, price, size= 'large'):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def showShirt(self):
        print('shirt detail')
        return f'SHIRT ID:{self.sid}\nSHIRT NAME:{self.type}\nTYPE:{self.type}\nPRICE:{self.price}\nSIZE:{self.size}\n'
    
    def __del__(self):
        print('destructor call')


s1 = Shirt(101, 'abc', 'formal', 80000)
print(s1.showShirt())
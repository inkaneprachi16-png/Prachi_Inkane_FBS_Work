class Shirt:
    size_prize={'small':1.0, 'medium':1.1,'large':1.2,'xlarge':1.3}
    discount =0
    def __init__(self, sid, sname, type, price, size= 'medium'):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.base_price = price
        self.size = size
        self.finalprice=self.adjust_price()


    def showShirt(self):
        print('shirt detail')
        return f'SHIRT ID:{self.sid}\nSHIRT NAME:{self.type}\nTYPE:{self.type}\nBASE PRICE:{self.base_price}\nSIZE:{self.size}\nFINAL PRICE:{self.finalprice}\n'
    
    def __del__(self):
        print('destructor call')

    def adjust_price(self):
        multiplier=Shirt.size_prize.get(self.size,1.0)
        return self.base_price*multiplier



s1 = Shirt(101, 't-shirt', 'formal', 1000)
print(s1.showShirt())


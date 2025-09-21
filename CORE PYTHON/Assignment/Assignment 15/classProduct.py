class Product:
    def __init__(self, pid, pname, price, quantity=3):          ###prameterised and parameterless constructor
        self.pid = pid
        self.pname =pname
        self.price = price
        self.quantity = quantity

    def showProducts(self):
        print('Product Details')
        return f'PRODUCT ID:{self.pid}\nPRODUCT NAME:{self.pname}\nPRICE:{self.price}\nQUANTITY:{self.quantity}\n'
    
    def __del__(self):                              ##destructor call
        print('destructor call')

p1 = Product(1001, 'Python', 700)
print(p1.showProducts())
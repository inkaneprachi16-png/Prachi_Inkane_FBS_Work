class Product:
    discount = 0                                                ##Static variable
    def __init__(self, pid, pname, price=0, quantity=0):          ###prameterised and parameterless constructor
        self.pid = pid
        self.pname =pname
        self.price = price
        self.quantity = quantity
        Product.discount = 10

    def showProducts(self):
        print('Product Details')
        print(f'PRODUCT ID:{self.pid}')
        print(f'PRODUCT NAME:{self.pname}')
        print(f'PRICE(befor discount):{self.price}')
        print(f'QUANTITY:{self.quantity}')
        print(f'Price(after {Product.discount} % discount):{self.discountPrice()}')
    
    def __del__(self):                              ##destructor call
        print('destructor call')

    def discountPrice(self):                            ###Static method
        return self.price * (1-Product.discount/100)


p1 = Product(1001, 'laptop', 50000, 2)
p1.showProducts()



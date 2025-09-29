class ComplexNumber:
    def __init__(self, real = 0, image=0):
        self.real = real
        self.image= image
        print(f"Object created: {self.real} + {self.image}i")

    def __add__(self, other):
        new_real= self.real + other.real
        new_image = self.image +  other.image
        return(f"Addition of complex number is : {new_real} + {new_image}i")

    def __sub__(self, other):
        new_real= self.real - other.real
        new_image = self.image -  other.image
        return(f"Substraction of complex number: {new_real} - {new_image}i")
    
    def __del__(self):
        print('destructor call')


c1 = ComplexNumber(3,4)
c2 = ComplexNumber(1,2)

print(c1+c2)
print(c1-c2)
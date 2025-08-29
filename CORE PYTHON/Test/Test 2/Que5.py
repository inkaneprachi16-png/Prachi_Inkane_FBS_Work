p1 = int(input('enter the price of first product:'))
p2 = int(input('enter the price of second product:'))
p3 = int(input('enter the price of tirrd product:'))
p4 = int(input('enter the price of fourth product:'))
p5 = int(input('enter the price of fifth product:'))

sum_product = p1+p2+p3+p4+p5

total_bill = sum_product + 18/100

print(f'Total bill after adding 18% GST is {total_bill}')
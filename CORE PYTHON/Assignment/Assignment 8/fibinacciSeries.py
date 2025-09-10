
def fibbo(num):
   c=0
   a=1
   b=0
   for i in range(num):
      c=a+b
      print(c, end=' ')
      a=b
      b=c

num= int(input('enter number:'))
fibbo(num)

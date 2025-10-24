def fibbonaciSeries(range):
    a=0
    b=1
    while (a<=range):
        yield a
        a, b =b, a+b

for num in fibbonaciSeries(100):
    print(num)
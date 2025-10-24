def pallindromNum(range):
    num =0
    while num <=range:
        if str(num)==str(num)[: : -1]:
            yield num

        num +=1


# gen = pallindromNum()
for p in pallindromNum(20):
    print(p)
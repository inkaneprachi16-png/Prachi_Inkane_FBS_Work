class calculator():
    try:
        num1= float(input('enter  number1:'))
        num2 = float(input('enter  number2:'))

        operator = input('enter operator to perform the operation(+,-,*,/):')

        if operator == '+':
            result = num1+num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 *num2
        elif operator == '/':
            try:
                result = num1/num2
            except ZeroDivisionError as e :
                print('division error:', e)      
        else:
            print('invalid operator')
    
        print(f'result: {num1} {operator} {num2} = {result}')

    except ValueError as e:
        print('value error:', e)

    except Exception as e:
        print('error:', e)

calculator()

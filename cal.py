#the basic arithmetics

addition = '+'
subtraction = '-'
division = '/'
multiplication = '*'



# this is a condition for getting more than one input depending on the users inputs.

expression_length = int( input('Enter to length of expression '))


if expression_length == 2:

    first_number = int(input('Enter you first number'))
    operator = input('Enter the operator')
    second_number = int(input('Enter you second number'))

    if operator  == addition:
        answer = first_number + second_number
    elif operator == subtraction:
        answer = first_number - second_number
    elif operator == division:
        answer = first_number / second_number
    elif operator == multiplication:
        answer = first_number * second_number
    else:
        print('You have entered a wrong operator')

    print(f'Your answer is {answer}')

elif expression_length == 3:

    user = []
    num_list = []
    addition = '+'
    subtraction = '-'
    division = '/'
    multiplication = '*'


    numbers_amount = 3

    if numbers_amount == 3:
        count = 1
        while count <= 3:
            i = input('Enter a number')
            user.append(i)
            count += 1
    elif numbers_amount >= 0:
        print("error")
    else:
        print('Can not handle expression with more the 3 number')


    #storing the user input in a list in for of a string

    for i, x in enumerate(user):
        if i == 0:
            u =int(x)
            num_list.append(u)
        elif i == 1:
            v =int(x)
            num_list.append(v)
        elif i == 2:
            w =int(x)
            num_list.append(w)
        
    num1, num2, num3 = num_list

    #converting the earlier stored string numbers to integers

    for i, x in enumerate(num_list):
        if i == 0:
            a = int(x)
            num_list.append(u)
        elif i == 1:
            b = int(x)
            num_list.append(v)
        elif i == 2:
            c =int(x)
            num_list.append(w)

    print(f'This are the numbers you entered {num1}, {num2}, {num3}')
    #you have to join the operators you want to use e.g "++" which is same as num1 + num2 + num3

    print('')

    operators = input('What operator do you want to use')

    if operators == '++':
        answer = num1 + num2 + num3
    elif operators == '+-':
        answer = num1 + num2 - num3
    elif operators == '+/':
        answer = num1 + num2 / num3
    elif operators == '+*':
        answer = num1 + num2 * num3
    elif operators == '--':
        answer = num1 - num2 - num3
    elif operators == '-+':
        answer = num1 - num2 + num3
    elif operators == '-/':
        answer = num1 - num2 / num3
    elif operators == '-*':
        answer = num1 - num2 * num3
    elif operators == '//-':
        answer = num1 / num2 / num3
    elif operators == '/+':
        answer = num1 / num2 + num3
    elif operators == '/-':
        answer = num1 / num2 - num3
    elif operators == '/*':
        answer = num1 / num2 * num3
    elif operators == '**':
        answer = num1 * num2 * num3
    elif operators == '*+':
        answer = num1 * num2 + num3
    elif operators == '*-':
        answer = num1 * num2 - num3
    elif operators == '*/':
        answer = num1 * num2 / num3

    print(f'You used the {operators} operators.\n Your answer is {answer} ')
else:
    print(f"This calculator doesn't support expression length of {expression_length} ")


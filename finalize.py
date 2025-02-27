import random as rd
chosen_option_1 = 0
chosen_option_2 = 0
chosen_option_3 = 0

a = input('please may you insert your name: ')

print(f'hello {a}, welcome to the money game')

money = 1
computer_money = 100
passwords = ['greenpanda123','pinkdinosaur567','redacted','unknown','!@#$%^&*()','sup\'Deven']
computer_password = rd.choice(passwords)
print(computer_password)
while True:
    list_of_options = ['hack','double','+20','+10','+10','double','+20','+10','+10','+30','triple','nothing']
    chosen_option_1 =  rd.choice(list_of_options)
    chosen_option_2 =  rd.choice(list_of_options)
    chosen_option_3 =  rd.choice(list_of_options)
    computer_money = computer_money+rd.randrange(1,1000)
    # print(chosen_option + chosen_option_2+chosen_option_3)



    b = input('pick one 1/2/3: ')
    if b=='1':
        print(chosen_option_1)
        if chosen_option_1 == 'double':
                money = money*2
        elif chosen_option_1 == '+20':
                money = money+20
        elif chosen_option_1 == '+10':
                money = money+10
        elif chosen_option_1 == '+30':
                money = money+30
        elif chosen_option_1 == 'triple':
                money = money*3
        elif chosen_option_1 == 'hack':
                d = input('guess the computers password: greenpanda123/pinkdinosaur567/redacted/unknown/!@#$%^&*()/sup\'deven: ')
                if d == computer_password:
                       print(f'you just won {computer_money//2} money!!!!')
                       money += computer_money//2
                else:
                    print('RIP you guessed the wrong password better luck next time!')
        print(f'your money is ${money}')
    elif b=='2':
        print(chosen_option_2)
        if chosen_option_2 == 'double':
                money = money*2
        elif chosen_option_2 == '+20':
                money = money+20
        elif chosen_option_2 == '+10':
                money = money+10
        elif chosen_option_2 == '+30':
                money = money+30
        elif chosen_option_2 == 'triple':
                money = money*3
        elif chosen_option_2 == 'hack':
                d = input('guess the computers password: greenpanda123/pinkdinosaur567/redacted/unknown/!@#$%^&*()/sup\'deven: ')
                if d == computer_password:
                       print(f'you just won {computer_money//2} money!!!!')
                       money += computer_money//2

                else:
                    print('RIP you guessed the wrong password better luck next time!')
        print(f'your money is ${money}')
    elif b=='3':
        print(chosen_option_3)
        if chosen_option_3 == 'double':
                money = money*2
        elif chosen_option_3 == '+20':
                money = money+20
        elif chosen_option_3 == '+10':
                money = money+10
        elif chosen_option_3 == '+30':
                money = money+30
        elif chosen_option_3 == 'triple':
                money = money*3
        elif chosen_option_3 == 'hack':
                d = input('guess the computers password: greenpanda123/pinkdinosaur567/redacted/unknown/!@#$%^&*()/sup\'deven: ')
                if d == computer_password:
                       print(f'you just won {computer_money//2} money!!!!')
                       money += computer_money//2

                else:
                    print('RIP you guessed the wrong password better luck next time!')
        print(f'your money is ${money}')
    else:
        print('next time please enter a valid answer')
        print('the game is going to end')
        print(f'your money was ${money}')
        break
    c = input('do you wish to continue: (y/n) ')
    if c != 'y':
        break
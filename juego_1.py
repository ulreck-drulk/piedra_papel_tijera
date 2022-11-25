import random
print("""  
Hola juega un clasico

Prueba tu suerte contra el PC

Juguemos Piedra Papel o Tijeras!!!

""")



user = input('A quien derrotare hoy??, introduce tu nombre ==>  ')
user = user.capitalize()
print(f'Bienvenido {user} estas a punto de ser derrotado, venga al que gane 2 seguidas primero ;)')
def choose_option():
    options = ('piedra', 'papel', 'tijera')
    user_option = input(f'Seleccione {options} => ')
    user_option = user_option.lower()
    if not user_option in options:
      print(f'Esa opcion no es valida, por favor elige {options}')
   

    computer_option = random.choice(options)

    print(f'Eleccion de {user} => {user_option}')
    print(f'Eleccion del Ordenador => {computer_option}')
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):    
    if user_option == computer_option:
        print('Empate!')    
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print(f'{user} gano!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('Computadora gano!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print(f'{user} gano')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('Computadora gano!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print(f'{user} gano!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('Computadora gano!')
            computer_wins += 1
    return user_wins, computer_wins

def ganador(user_wins, computer_wins):
    if computer_wins-user_wins ==2:
        print('El ganador es la computadora')
        print('AJA!! Otra Victima de mi grandeza!!!')
        exit()
    if user_wins-computer_wins == 2:
        print(f'El ganador es {user}')
        print('Vamos Arbitro eso No es justo!!!')
        exit()
    
        
def run_game():
    rounds = 1
    


    computer_wins = 0
    user_wins = 0
    while True:

        print('*' * 10)
        print('ROUND', rounds)        
        print('*' * 10)
        

        print('computer_victories', computer_wins)
        print(f'{user}_victories', user_wins)
        rounds +=1
        if rounds == 6:
            print(f'''
                    Hey {user}!! Calmate, se esta poniendo intenso
                            Vamos con calmita no??!!
                       ''')
        if rounds >= 10:
            print(f'Hey {user} Osea ya pierde no?')

        user_option, computer_option = choose_option()
        user_wins, computer_wins = check_rules(user_option, computer_option,user_wins, computer_wins)
        ganador(user_wins, computer_wins)
      

if __name__=="__main__":
    run_game()

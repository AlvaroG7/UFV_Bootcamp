# The challenge involves creating a bidding system.
# HINT: Think about how you can use dictionaries to solve this problem.

# Import the required modules. These modules are provided to you.
from art import logo
import os


def clear():
    # Using os.system() to execute the clear command specific to the operating system.
    os.system('cls' if os.name == 'nt' else 'clear')

    # DOS and Windows('nt'): Microsoft's DOS had the cls command to clear the screen. Windows, which initially started as a graphical layer over DOS, maintained a lot of command-line compatibility with DOS for ease of transition and backward compatibility. So, when Windows NT(New Technology) came about, it kept the cls command for clearing the screen.
    # Unix and Unix-like Systems: Unix is an OS that dates back to the 1970s. The command-line interface for Unix used the clear command. Many modern OSes, including Linux and macOS, are derived or inspired by Unix, so they keep the clear command for compatibility and tradition.


# Start by printing the provided logo.
#       print(logo)
#       import time
#       time.sleep(1)
#       clear()
#       


# Create a dictionary to hold the bids.
pujas = {    }


# TODO: Set an initial state for the bidding process.

pujas['precio_inicial'] = '100'
#       pujas['puja1'] = '120'
#       pujas['puja2'] = '150'
#       pujas['puja3'] = '170'
#       pujas['puja4'] = '200'
#       pujas['puja5'] = '250'

print('El precio de salida es: ', pujas['precio_inicial'])

#. INICIA LA PUJA

nuevas_pujas = 1



while nuevas_pujas:


    #_ Pedir el nombre del siguiente pujador 
    print('NUEVA PUJA!!!\n')
    nombre_pujador = input('Introduzca nombre de pujador: ')
    print('El nombre del nuevo pujador es:              ---------', nombre_pujador)
    valor_nueva_puja = input('Introduzca la cantidad a pujar: ')
    print('Nueva cantidad:                              ======>>>', valor_nueva_puja)
    pujas[nombre_pujador] = valor_nueva_puja
    #_ Imprimimos cómo van las pujas hasta el momento 
    #print('Las pujas van así:     ', pujas)
    print('Las pujas van así:')
    for clave, valor in pujas.items():
        print(f'        {clave}: {valor}')

    
    #_Comprobar si hay nuevas pujas 
    decision = input('Hay nuevas pujas?????:   ')
    if decision == 'si':
        nuevas_pujas = True
        clear()
    else:
        nuevas_pujas = False

#?   Las pujas van así:             
#?           precio_inicial: 100    
#?           AAA: 222               
#?           BBB: 333               
#?           CCC: 20               


def buscar_mayor_puja (pujas):
    print('El RESUMEN de las pujas es:   ', pujas)
    
    puja_previa = 0 
    for i in pujas:
        puja_comprobada = int(pujas[i])

        
        if puja_comprobada > puja_previa:
            puja_previa = puja_comprobada
            print('Nueva puja mayor:   ---',puja_previa)
        else:
            print('No se ha encontrado una puja mayor, sigo buscando...')

    return puja_previa
    
print('La mayor puja encontrada es:', buscar_mayor_puja(pujas))


print('============================\n============================')





# TODO: Create a function to determine the highest bidder.


def find_highest_bidder(bidding_record):
    # Initialize the necessary variables to determ
    # ine the winner.

    # Loop through the dictionary to determine the highest bid.

    # Print out the highest bidder.

    # TODO: Use a loop to continue receiving bids until there are no more bidders.

    # Remember to clear the console after each bid to keep the current bid private.
    pass

